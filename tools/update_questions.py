import json

with open("../simple-interview-questions.json", "r") as file:
    data = json.load(file)

print("This is an Interview Question Manager")
print("Type Ctrl+C to exit and save all questions")
print("-" * 50)

# Putting in the loop
try:
    while True:
        # Show the last interview question to stay on track
        last_id = data["questions"][-1]["id"]
        last_question = data["questions"][-1]['question']

        print("The last question is ", last_question)

        # Prompt a user for a question
        new_question_string = input("Please enter a new interview question: ")

        # Prompt the user for the question type
        question_type = input("Please enter the question type (behavioral, technical, etc): ")
                                        
        # TODO: Add subtype and difficulty level fields


        new_question = {
            "id": str(int(last_id) + 1),
            "type": question_type,
            "question": new_question_string
        }

        data["questions"].append(new_question)

except KeyboardInterrupt:
    print("\nExiting the application...")

# Append the last question

# Save thew new questions to the file
with open("../simple-interview-questions.json", "w") as file:
    json.dump(data, file, indent=2)

print("The file simple-interview-questions.json has been updated.")
