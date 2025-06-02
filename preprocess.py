import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

# Define common synonym mappings
synonyms = {
    "school fees": "fees",
    "charges": "fees",
    "fee": "fees",
    "hostel": "accommodation",
    "hostels": "accommodation",
    "dorm": "accommodation",
    "apply": "admission",
    "application": "admission",
    "enroll": "admission",
    "sign up": "admission",
    "letter": "admission",
    "programs": "courses",
    "course": "program",
    "courses": "program",
    "study": "program",
    "jkua": "jkuat",
}

def expand_synonyms(text):
    text = text.lower()
    for key, value in synonyms.items():
        text = re.sub(rf'\b{key}\b', value, text)
    return text

def reduce_query(text):
    # Step 1: Lowercase and remove punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text.lower())

    # Remove the word "jkuat"
    text = text.replace("jkuat", "")

    # Step 2: Expand synonyms
    text = expand_synonyms(text)

    # Step 3: Tokenize and remove stopwords
    tokens = [word for word in text.split() if word not in stop_words]

    # Step 4: Join keywords
    return ' '.join(tokens)