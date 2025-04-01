import speech_recognition as sr
import pyttsx3
import wikipedia
import tkinter as tk
from tkinter import Label, Button
import requests
import openai  # Optional for AI-based responses

#Add this function to listen to voice commands
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        status_label.config(text="Listening...")  # Update GUI
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        status_label.config(text=f"You said: {command}")  # Update GUI
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I could not understand. Please try again.")
        status_label.config(text="Couldn't understand, try again!")  # Update GUI
        return None
    except sr.RequestError:
        print("Error with the speech recognition service.")
        status_label.config(text="Speech recognition error!")  # Update GUI
        return None

#Add this function to speak responses
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

#Wikipedia Search
def search_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        return result
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Too many results, be more specific: {e.options}"
    except wikipedia.exceptions.PageError:
        return "No information found."

#Fetch Weather Information
def get_weather(city):
    api_key = "your_openweathermap_api_key"  # Get API key from openweathermap.org
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    
    if response["cod"] != "404":
        weather = response["main"]
        temp = weather["temp"]
        description = response["weather"][0]["description"]
        return f"The temperature in {city} is {temp}°C with {description}."
    else:
        return "City not found."

#AI-Powered Response
openai.api_key = "your_openai_api_key"

def chat_with_ai(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

#This function will process commands
def process_command(command):
    if command is None:
        return  # Skip processing if no valid command is detected

    if "wikipedia" in command:
        speak("Searching Wikipedia...")
        query = command.replace("wikipedia", "").strip()
        result = search_wikipedia(query)
        print(result)
        speak(result)

    elif "weather" in command:
        speak("Which city?")
        city = listen()
        if city:  # Proceed only if city is recognized
            weather_report = get_weather(city)
            print(weather_report)
            speak(weather_report)

    elif "exit" in command or "bye" in command:
        speak("Goodbye!")
        root.destroy()  # Close the GUI
        exit()

    else:
        speak("I'm not sure how to respond to that.")
        status_label.config(text="Unknown command!")  # GUI update



#Add this after defining speak()
root = tk.Tk()
root.title("Voice Assistant")
root.geometry("400x300")

status_label = Label(root, text="Click 'Start Listening'", font=("Arial", 14))
status_label.pack(pady=20)

start_button = Button(root, text="Start Listening", font=("Arial", 12), command=lambda: process_command(listen()))
start_button.pack(pady=10)

exit_button = Button(root, text="Exit", font=("Arial", 12), command=root.destroy)
exit_button.pack(pady=10)
root.mainloop()

#Run the GUI Loop
if __name__ == "__main__":
    speak("Hello, how can I assist you?")
    while True:
        user_command = listen()
        process_command(user_command)

