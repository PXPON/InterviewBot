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

# Initialize camera
cap = cv2.VideoCapture(0) # 0 for default camera

if not cap.isOpened():
    print("Error: Could not open video device.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 20 # Default to 20 FPS if camera doesn't report it

# Define the codec and create VideoWriter object
# For Linux, 'XVID' or 'MJPG' are common. 'MP4V' might also work if ffmpeg is installed.
fourcc = cv2.VideoWriter_fourcc(*'XVID') # You might need to change this codec depending on your system
out = cv2.VideoWriter('interview_recording.avi', fourcc, fps, (frame_width, frame_height))

recording = True

def iterate_through_questions(interview_question_list):
    global recording
    for item in interview_question_list:
        # Read frame from camera for live display or processing
        ret, frame = cap.read()
        if ret:
            # Write the frame to the output file
            out.write(frame)

            # Optional: Display the live camera feed (press 'q' to quit the display)
            cv2.imshow('Live Feed', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                recording = False # Set flag to stop recording
                break
        else:
            print("Error: Could not read frame from camera.")
            recording = False
            break

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

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()

    
