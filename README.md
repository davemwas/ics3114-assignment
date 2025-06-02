# Amanda – JKUAT Chatbot (AIML + NLP)

Amanda is a lightweight rule-based chatbot built using Python and AIML, designed to assist students with common questions about Jomo Kenyatta University of Agriculture and Technology (JKUAT). It supports keyword-based matching, NLP-enhanced query processing, fallback responses, and command-style quick prompts.

---

## 🎯 Features

- AIML-based core with 40+ curated FAQ responses
- NLP preprocessing (stopword removal, synonym mapping)
- Fallback handler with custom default response

---

## Project Structure

<pre>
<b>ics3114-assignment/</b>
├── <b>amanda.py</b>               → Main chatbot script  
├── <b>preprocess.py</b>           → NLP preprocessor with stopword & synonym handling  
│
├── <b>aiml_files/</b>  
│   └── <b>core_nlp.aiml</b>       → AIML knowledge base (patterns + templates)  
│
├── <b>data/</b>  
│   └── <b>faqs_nlp.csv</b>        → Original CSV source of Q&A pairs  

</pre>


---

## Getting Started

### 1. Clone the Project

```bash
git clone https://github.com/davemwas/ics3114-assignment.git
cd amanda-chatbot
```

### 2. Create Virtual Environment

```
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

If requirements.txt is missing, install manually:
```
pip install aiml nltk
python -c "import nltk; nltk.download('stopwords')"
```

⸻

### Running Amanda

```
python amanda.py
```
You’ll see:

Amanda: Hi! I'm Amanda, your JKUAT assistant. Type 'exit' to quit.

You: Type questions like:

	•	“How do I apply to JKUAT?”
	•	“Can I defer studies?”
	•	“How to get admission letter?”

⸻

NLP Logic

In preprocess.py, Amanda:

	•	Cleans punctuation and converts text to lowercase
	•	Removes common English stopwords
	•	Expands synonyms like:
		•	“school fees” → “tuition”
		•	“enroll” → “admission”
		•	“dorm” → “accommodation”

This allows flexible input matching against AIML patterns.

⸻

How to Customize

	•	Edit aiml_files/core_nlp.aiml to add more Q&A patterns
	•	Add new synonyms in preprocess.py

⸻

Sample Q&A Patterns

| Question                          | Response Summary                             |
|----------------------------------|----------------------------------------------|
| Can I get an admission letter?   | Provides link to admission portal            |
| What is the school fee?          | Tuition explanation (via synonym: school fees → tuition) |
| Are there hostels?               | Hostel availability and priority info        |
| What school programs are available? | Overview of academic programs offered     |

⸻

Notes

	•	Amanda does not use machine learning — it is a rule-based system enhanced with lightweight NLP
	•	Matching is case-insensitive but still pattern-driven
	•	You can extend Amanda to use Rasa, spaCy, or HuggingFace for future improvements

⸻

Author

David Mwangi
Built as part of a university Web Technology project (JKUAT, 2025)