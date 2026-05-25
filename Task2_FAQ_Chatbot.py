faq = {
    "what is ai": "AI means Artificial Intelligence",
    "what is python": "Python is a programming language",
    "what is machine learning":
    "Machine Learning helps computers learn from data",
    "what is data science":
    "Data Science is used to analyze data",
    "who created python":
    "Python was created by Guido van Rossum"
}

print("FAQ Chatbot Started")
print("Type 'exit' to stop chatbot")

while True:
    question = input("Ask Question: ").lower()

    if question == "exit":
        print("Chatbot closed")
        break

    elif question in faq:
        print("Answer:", faq[question])

    else:
        print("Sorry, answer not found")