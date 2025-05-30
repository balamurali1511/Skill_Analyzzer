import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from transformers import pipeline
from wikipedia import Wikipedia

# Load the NLTK data needed for tokenization and stop words
nltk.download('punkt')
nltk.download('stopwords')

# Initialize the question generation pipeline
generator = pipeline('text-generation')

# Initialize the Wikipedia API
wiki = Wikipedia(eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiJhMTFjM2Q5YzBiMjBlYjkzOGM4N2FkNzRiYmMwZGE2ZSIsImp0aSI6IjBlNDQ0OGE1NDRjYTY0NWExYzg5ZGY5MWI1MGE2MGZkOWIyZjMwZDYyYTAzMmQwYmU3YmZjZmQyOTAyYjRlODQ0NzY0ZWFmYzU4NjJjMjk4IiwiaWF0IjoxNzI1MjQ3NTkwLjg1Nzc4NiwibmJmIjoxNzI1MjQ3NTkwLjg1Nzc4OSwiZXhwIjozMzI4MjE1NjM5MC44NTUxNSwic3ViIjoiNzY0MDg1NTEiLCJpc3MiOiJodHRwczovL21ldGEud2lraW1lZGlhLm9yZyIsInJhdGVsaW1pdCI6eyJyZXF1ZXN0c19wZXJfdW5pdCI6NTAwMCwidW5pdCI6IkhPVVIifSwic2NvcGVzIjpbImJhc2ljIiwiY3JlYXRlZWRpdG1vdmVwYWdlIl19.AJ8kL-JvYXhVYsZjSAi2BxQnxLAhB6vTvJvEdV9VXJ0nd2YJ3i7SJlM4NgtqakEG74Bq0ALVPq8fNQoVZNmKIvEjvzQKS1XtBFFzp_vfSxJq8oyCoJrGFnrc9nstMuEeX7fr45P4BdD1ZZi7B4eiHmccP_MaZJtvz5Xi9LDLdGKvpP4qKA1R3UQ7OCXPA2-YfdTOAZ9Uc43DPnZGJBqyVAyF1s3C5cUdM8IAwo-JNUlymlB7gRG-9QtQRvKucMcDseEaxrOvRsLaGZUgsh-i3oLa0AeXSliHktpbh6Ta6flR5DDtY5osI0Co2n2PTkk9bo-cAfBw1dScggZfLfSi--BcOqTteRcs6oMTnvhG0E-qgNBr6jQK5QCkFSK-xg2XxUs_nVO3zJtqLeIg-880bApQxXh4TeAQOVSkr3gTufvYX-7uTyNwuqS1d9cmpwqm5_dx-MKO8-nFhYJACAnJ3Vw-kei62enbCbfN0d9VPOW5jr5JIwUvQqcWFOniWd8OX8kXeYnXRDctfXYvH-4dwAKcW43R5HcbuS96-kOOvb4ixJCJivI2gai5Qk3GOuRq1qZWtjMbwm0Hv290Y1ZsJ8mgW4e60eG53CwolG33f-zrIlEMmmO0_CkZvJHAUOCVyvBXGdSGehP6Wvs3AIfGqz3uoQdOYNSxrZwlPfRPWWc)

# Function to get information on a specific topic from Wikipedia
def get_topic_info(topic):
    page = wiki.page(topic)
    text = page.content
    return text

# Function to generate a new question on a specific topic
def generate_question(topic):
    text = get_topic_info(topic)
    sentences = nltk.sent_tokenize(text)
    random_sentence = random.choice(sentences)
    words = nltk.word_tokenize(random_sentence)
    stop_words = set(stopwords.words('english'))
    keywords = [word for word in words if word.lower() not in stop_words]
    keyword = random.choice(keywords)
    prompt = f"What is the {keyword} of {topic}?"
    output = generator(prompt, max_length=50, num_return_sequences=1)
    question = output[0]['generated_text']
    return question

# Function to generate options for a question
def generate_options(question, topic):
    text = get_topic_info(topic)
    sentences = nltk.sent_tokenize(text)
    options = []
    for sentence in sentences:
        if question.lower() in sentence.lower():
            words = nltk.word_tokenize(sentence)
            stop_words = set(stopwords.words('english'))
            keywords = [word for word in words if word.lower() not in stop_words]
            for keyword in keywords:
                if keyword.lower() not in question.lower():
                    options.append(keyword)
    random.shuffle(options)
    return options[:4]

# Function to ask a new question
def ask_question(topic):
    question = generate_question(topic)
    options = generate_options(question, topic)
    correct_answer = random.choice(options)
    print(f"Question: {question}")
    print("Options:")
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    answer = input("Enter the number of your answer: ")
    if options[int(answer)-1] == correct_answer:
        print("Correct!")
    else:
        print(f"Sorry, the correct answer is {correct_answer}.")

# Main function
def main():
    print("Welcome to the quiz application!")
    topic = input("Please select a topic (e.g. history, science, sports): ")
    
    while True:
        ask_question(topic)
        cont = input("Do you want to continue? (yes/no): ")
        if cont.lower() != "yes":
            break

if __name__ == "__main__":
    main()