# Jarvis — Python Voice Assistant

Jarvis is a Python-based voice assistant that listens for a wake word, recognizes voice commands, and performs tasks such as opening websites, playing songs from a custom music library, fetching news headlines, and answering general questions using the OpenAI API.

This project was built while learning Python and exploring speech recognition, text-to-speech, API integration, and automation.

## Features

- **Wake-word activation:** Activates when it recognizes “Jarvis”.
- **Website shortcuts:** Opens Google, Facebook, YouTube, LinkedIn, and Spotify through voice commands.
- **Music playback:** Opens songs from a custom music library.
- **News headlines:** Fetches and reads news headlines using NewsAPI.
- **AI-powered responses:** Uses the OpenAI API to answer general questions and assist with coding.
- **Text-to-speech:** Uses `pyttsx3` for spoken responses.
- **Optional online TTS:** Includes an alternative `gTTS`-based speech function.

## Tech Stack

- Python
- SpeechRecognition
- pyttsx3
- OpenAI API
- Requests
- gTTS
- Pygame
- Webbrowser

## Project Structure

```text
Jarvis_Py/
├── main.py
├── musicLibrary.py
├── README.md
└── .gitignore
```

## Requirements

- Python installed on your computer
- A working microphone and speakers
- An internet connection for speech recognition, news fetching, and AI responses
- An OpenAI API key with available API credits
- A NewsAPI key

## Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   cd Jarvis_Py
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv .venv
   ```

   On Windows Command Prompt:

   ```cmd
   .venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install SpeechRecognition pyttsx3 openai requests gTTS pygame pyaudio
   ```

   Microphone support may require additional setup depending on your operating system.

4. Configure your API keys as environment variables.

   On Windows Command Prompt:

   ```cmd
   setx OPENAI_API_KEY "your_openai_api_key"
   setx NEWS_API_KEY "your_newsapi_key"
   ```

   Replace the placeholders with your own keys. Restart your terminal after setting them.

   **Never commit API keys to your repository or share them publicly.**

## Usage

Run the assistant:

```bash
python main.py
```

Say **“Jarvis”** when prompted, then speak a supported command.

Example commands:

- “Open Google”
- “Open YouTube”
- “Open Spotify”
- “Play Wavy”
- “Tell me the news”
- “What is coding?”
- “Explain Python functions”

The AI assistant requires an internet connection and available OpenAI API credits. News fetching requires a valid NewsAPI key.

## Notes

- Music playback opens the configured song link in your browser; playback depends on the linked service.
- The optional `gTTS` function uses an online text-to-speech service.
- Speech recognition may occasionally misinterpret commands.
- API usage may incur charges depending on the services and plans used.

## Future Improvements

- Improve speech recognition and command handling.
- Add more website shortcuts and music commands.
- Improve error handling and configuration.
- Add support for additional assistant capabilities.

## Learning Goals

This project explores Python functions, conditional statements, dictionaries, exception handling, external APIs, speech recognition, text-to-speech, and basic automation.

---

**Author:** Meet Ummat

**Status:** Personal learning project
