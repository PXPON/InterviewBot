# Creating this file to extract text from interviews
# NOTE: This must run in Linux or iOS

import datetime
import whisper
# from datetime import datetime
import ffmpeg

# We need to check for the GPU as a future feature

model = whisper.load_model('base.en')
option = whisper.DecodingOptions(language='en', fp16=False)

file_path = input("Please enter the path to the video file: ")

result = model.transcribe(file_path)

print(result)
print(result['text'])

# timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
save_target = f"transcription-{timestamp}.vtt"


with open(save_target, 'w') as file:
    for i, segment in enumerate(result['segments']):
        file.write(str(i + 1) + '\n')
        file.write(str(datetime.timedelta(seconds=segment['start'])) + ' --> ' + str(datetime.timedelta(seconds=segment['end'])) + '\n')
        file.write(segment['text'].strip() + '\n')
        file.write('\n')

result['segments'][0]
