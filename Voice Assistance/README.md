# Voice Assistant

This is a simple **Voice Assistant** built using Python and Tkinter. It can listen to voice commands and perform tasks such as fetching information from Wikipedia, checking the weather, and more.

## Features

- **Voice Command Recognition**: Uses the `SpeechRecognition` library to recognize user voice commands.
- **Text-to-Speech**: Converts text responses to speech using the `pyttsx3` library.
- **Wikipedia Search**: Fetches information from Wikipedia based on user queries.
- **Weather Information**: Fetches weather details for a city using the OpenWeatherMap API.
- **Simple GUI**: Built using Tkinter, it includes a **microphone button** for starting listening and an **exit button** for closing the app.

## Installation

Follow these steps to set up and run the project:

### 1. Clone the Repository
git clone https://github.com/kowshi555/voice-assistant.git
cd voice-assistant

### 2. Install Dependencies
pip install -r requirements.txt
pip install speechrecognition pyttsx3 pyaudio wikipedia requests openai

### 3. Add the mic.png Image
Make sure you have a microphone image (e.g., mic.png) for the GUI. Place it in the root directory of the project.

### 4. Run the Application
python voice_assistant.py
