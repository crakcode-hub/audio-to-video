import os
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.VideoClip import ImageClip

# Paths to your input files
audio_path = "audio.wav"
image_path = "thumbnail.png"
output_path = "output_video.mp4"

# Check if input files exist
if not os.path.exists(audio_path):
    raise FileNotFoundError(f"Audio file not found: {audio_path}")
if not os.path.exists(image_path):
    raise FileNotFoundError(f"Image file not found: {image_path}")

# Load the audio
audio = AudioFileClip(audio_path)

# Load the image and set duration
image = ImageClip(image_path).with_duration(audio.duration)

# Combine the image with the audio
video = image.with_audio(audio)

# Write the output video file
video.write_videofile(output_path, codec="libx264", fps=24, audio_codec="aac")

print(f"Video successfully created: {output_path}")