import json
import argparse
import random
import os
from gtts import gTTS

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

# Shuffle the questions to ensure random order
random.shuffle(data['questions'])

def iterate_through_questions(interview_question_list):
    for item in interview_question_list:
        # Add your logic for voice recitation and recording here
        # For now, we'll just print them
        question = item['question']

        question = item['question']
        print(f"Question: {question}")
        # Use gTTS to speak the question (e.g., 'en-uk' for British English)
        tts = gTTS(text=question, lang='en-uk') # You can change 'en-uk' to other language codes like 'en' (US English), 'es' (Spanish), 'fr' (French), etc.
        audio_file = "temp_question.mp3"
        tts.save(audio_file)
        os.system(f"mpg123 {audio_file}") # For Linux, you might need to install mpg123: sudo apt-get install mpg123
        # For Windows: os.system(f"start {audio_file}")
        # For macOS: os.system(f"afplay {audio_file}")
        os.remove(audio_file)

# Assuming the 'questions' key holds the list of questions
iterate_through_questions(data['questions'])

    
