import json
import argparse

# For this code we want to go through each question and have 
# a voice recite the question.

# Then, we record the interviewee giving their answer.
# That person would have their eyes tracked and their diction
# evaluated and later scored.

# Create the parser
parser = argparse.ArgumentParser(description="Run an interview session with questions from a JSON file.")

# Add the --file argument
parser.add_argument('--file', type=str, default='../list-of-interview-questions.json',
                    help='Path to the JSON file containing interview questions.')

# Parse the arguments
args = parser.parse_args()

# Import the list of interview questions
with open(args.file, "r") as file:
    data = json.load(file)

def iterate_through_questions(interview_question_list):
    a = 1
    
