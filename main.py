import os
import time

import openai
import whispercpp
from dotenv import load_dotenv
from yt_dlp import YoutubeDL

load_dotenv()

openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_KEY")

Whisper = whispercpp.Whisper
WhisperAPI = whispercpp.api

# Prompt for the video URL
# video_url = input("Please enter the video URL: ")

video_url = "https://www.youtube.com/watch?v=eF6asPd0KJs"

output_path = "output.%(ext)s"  # Output file template

file_name = "transcript.txt"
# Configure yt-dlp options
ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": output_path,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        },
    ],
    "postprocessor_args": [
        "-ar",
        "16000",
    ],
}

# Download and convert the audio
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])


def handle_segment(
    context: whispercpp.api.Context, n_new: int, user_data: None
) -> None:
    # Using write mode will automatically truncate the file, thus clearing it out
    with open(file_name, "w") as file:
        segment = context.full_n_segments() - n_new
        while segment < context.full_n_segments():
            start_time = time.strftime(
                "%H:%M:%S", time.gmtime(context.full_get_segment_start(segment) / 100)
            )
            end_time = time.strftime(
                "%H:%M:%S", time.gmtime(context.full_get_segment_end(segment) / 100)
            )
            output = (
                f"[{start_time} - {end_time}]: {context.full_get_segment_text(segment)}"
            )
            print(output)
            file.write(output + "\n")
            segment += 1


w = Whisper.from_pretrained("base.en")
p = w.params.with_language("en")
p.with_language("en")
p.with_no_speech_thold(
    0.1
)

p.on_new_segment(handle_segment, None)

audio = WhisperAPI.load_wav_file(os.path.abspath("output.wav"))

print("Transcribing...")
w.context.full(w.params, audio.mono)
print("Transcription complete!")
