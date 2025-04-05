# Audio to Video Converter

This Python script converts an audio file (`.wav`) and a static image (`.png`) into a video file (`.mp4`). The script uses MoviePy to create a video where the image serves as a static visual while the audio plays.

## Features
- Combine an audio file (`.wav`) with a static image (`.png` or `.jpg`) to create a video
- Supports video output in `.mp4` format using H.264 codec
- Audio encoding using AAC codec
- 24 FPS video output
- Automatic duration matching with audio length
- File existence validation
- Error handling for missing files
- Easy to use with Python
- Progress bar during conversion

## Prerequisites

- Python 3.x (Recommended version: 3.6 or higher)

## Installation

### Step 1: Install Python
Download and install Python from [python.org](https://www.python.org/downloads/).

### Step 2: Install Required Dependencies
```bash
python -m pip install --upgrade pip
pip install moviepy Pillow
```


### Step 3: Prepare Your Files
Place your audio file (e.g., audio.wav) and image file (e.g., thumbnail.png) in the same directory as the script.

### Step 4: Running the Script
Run the Python script to generate the video:

This will create an output_video.mp4 file in the same directory, combining the audio with the image.
pip install moviepy
If you're using a Windows machine, you might need to install additional dependencies like ffmpeg. You can download it from FFmpeg.org, and ensure it's added to your system's PATH.


Stay tuned for more open-source projects and educational content from CrakCode!


## Contributing
We welcome contributions to this project! If you'd like to improve the code or add new features, feel free to fork the repository and submit a pull request.

To report issues or request features, please open an issue on the GitHub repository.

## About CrakCode
This project is maintained by CrakCode. For more information about CrakCode and our mission to provide quality educational resources, visit www.crakcode.in .

CrakCode is a platform dedicated to empowering individuals through coding, tech education, and career development. Our vision is to help students and professionals upskill and find job opportunities in the tech industry.

### Connect With Us
- Website: www.crakcode.in
- Email: contact@crakcode.in
- GitHub: CrakCode-hub


