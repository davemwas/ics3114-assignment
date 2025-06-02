import aiml
import os
import nltk

from preprocess import reduce_query

nltk.download('stopwords')



BRAIN_FILE = "amanda_brain.brn"

# Create AIML kernel
kernel = aiml.Kernel()

# Disable internal PyAIML logging/warnings
kernel._verboseMode = False

if os.path.exists(BRAIN_FILE):
    if os.path.getmtime(BRAIN_FILE) < os.path.getmtime("aiml_files/core_nlp.aiml"):
        kernel.learn("aiml_files/core_nlp.aiml")
        kernel.saveBrain(BRAIN_FILE)
    else:
        kernel.loadBrain(BRAIN_FILE)
else:
    kernel.learn("aiml_files/core_nlp.aiml")
    kernel.saveBrain(BRAIN_FILE)

# Start the chatbot
print("Amanda: Hi! I'm Amanda, your JKUAT assistant. Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Amanda: Goodbye!")
        break

    cleaned_input = reduce_query(user_input)
    response = kernel.respond(cleaned_input)

    if not response.strip():
        response = "I'm sorry, I don't understand that yet. Try asking about admissions, fees, hostels, or programs."

    print("Amanda:", response)