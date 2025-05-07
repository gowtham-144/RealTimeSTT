Real-Time Speech-to-Text System for Automation

Overview

This project implements a real-time speech recognition system designed for customer support automation. It listens continuously to microphone input, transcribes spoken words into text using Google's Speech Recognition API, and triggers automation responses based on detected keywords.

This project corresponds to Unit 5 of the NMU syllabus and supports use cases such as call summarization, keyword detection, and agent performance analysis.



Features

- Real-time transcription using live microphone input
- Continuous listening loop with no need to restart the script
- Detection of keywords (e.g., "refund", "complaint") for triggering automation
- Auto-logging of all transcriptions to a text file



Requirements

- Python 3.x
- speechrecognition
- pyaudio

Installation

```bash
pip install -r requirements.txt
```

You may also need:

```bash
pip install pipwin
pipwin install pyaudio
```



Usage

To start the real-time transcription:

```bash
python main/project2_real_time_srt.py
```

Speak into your microphone. Say a keyword like "stop" or "refund" to test the trigger mechanism.



Output

All transcriptions are saved in the `/output/transcripts.txt` file. You can open this file to view all lines captured during the session.

Optional: Add screenshots of terminal output into the `output/` folder.



Example

```text
Listening...
You said: I would like a refund please
⚠️ Keyword 'refund' detected. High-priority alert triggered
