import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os

newsapi = os.getenv("NEWS_API_KEY")

def speak(text):
    print("Jarvis says:", text)

    # Use a fresh engine for each response to avoid audio issues
    # encountered in this environment.
    voice = pyttsx3.init("sapi5")
    voices = voice.getProperty("voices")
    voice.setProperty("voice", voices[0].id)
    # Set the volume
    voice.setProperty("volume", 1.0)
    voice.setProperty("rate", 150)

    voice.say(text)
    voice.runAndWait()
    voice.stop()

def speakNew(text):
    # Optional online TTS using Google Text-to-Speech (gTTS).
    tts = gTTS(text)
    tts.save('temp.mp3')
    import pygame

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def aiProcess(command):
    client = OpenAI()

    completion = client.chat.completions.create(
    model="gpt-6-astra",
    messages=[
        {
            "role": "system",
            "content": (
                "You are Jarvis, a helpful virtual assistant. "
                "Answer questions clearly and concisely. "
                "You can explain concepts, help with coding, "
                "and assist with general tasks. Give short responses please."
            )
        },
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")

    elif c.lower().startswith("play"):
        parts = c.lower().split(maxsplit=1)

        if len(parts) < 2:
            speak("Please tell me which song to play.")
            return

        song = parts[1].strip()

        # Correct a common speech-recognition error for this song.
        if song == "baby":
            song = "wavy"

        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry, this song is not in your music library.")

    elif "news" in c.lower():
        if not newsapi:
            speak("News API key is not configured.")
            return

        try:
            # Keep your existing NewsAPI request and response handling here.
            r = requests.get(
                "https://newsapi.org/v2/top-headlines",
                params={
                    "sources": "google-news-in",
                    "apiKey": newsapi,
                    "pageSize": 5
                },
                timeout=10
            )
            if r.status_code == 200:
                # Parse the JSON response
                data = r.json()

                # Extract the articles
                articles = data.get('articles', [])

                if not articles:
                    speak("No news articles found.")
                else:
                    count = 0

                    for article in articles:
                        title = article.get("title", "").strip()

                        if title and title not in ("Google News", "[Removed]"):
                            speak(title)
                            count += 1

                        if count == 5:
                            break

                    if count == 0:
                        speak("No valid news headlines found.")
            else:
                print("News API error:", r.status_code, r.text)
                speak("Sorry, I couldn't fetch the news.")

        except requests.RequestException as e:
            print("Request error:", e)
            speak("I couldn't connect to the news service.")
    
    else:
        try:
            answer = aiProcess(c)
            speak(answer)

        except Exception as e:
            print("OpenAI API error:", e)
            speak("Sorry, I couldn't process that request.")
    print(c)


if __name__ == "__main__":
    speak("Initializing Jarvis....")

    while True:
        # Listen for the wake word "jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()

        print("recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening for Jarvis...")
                audio = r.listen(source, timeout=3, phrase_time_limit=2)

            word = r.recognize_google(audio).lower().strip()

            if word == "jarvis":
                speak("Yeah!")

                with sr.Microphone() as source:
                    print("Jarvis Active... Speak your command.")
                    audio = r.listen(source, timeout=3, phrase_time_limit=2)

                command = r.recognize_google(audio, language="en-US")
                print("You said:", command)
                processCommand(command)

                # result = r.recognize_google(
                # audio,
                # language="en-US",
                # show_all=True
                # )
                # print(result)

        except sr.WaitTimeoutError:
            print("No speech detected. Listening again...")

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")

        except sr.RequestError as e:
            print("Speech recognition error:", e)

        except KeyboardInterrupt:
            print("Jarvis stopped.")
            break
