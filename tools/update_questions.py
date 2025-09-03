import json

with open("../simple-interview-questions.json", "r") as file:
    data = json.load(file)

# Prompt a user for a question
new_question_string = input("Please enter a new interview question: ")

# Prompt the user for the question type
question_type = input("Please enter the question type (behavioral, technical, etc): ")

# Get the last id in the file
last_id = data["questions"][-1]["id"]

# TODO: Add subtype and difficulty level fields

new_question = {
    "id": last_id + 1,
    "type": question_type,
    "question": new_question_string
}

data["questions"].append(new_question)

# How can we get this file to loop?
