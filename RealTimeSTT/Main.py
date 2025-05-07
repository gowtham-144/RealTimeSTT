import speech_recognition as sr
from textblob import TextBlob
from datetime import datetime
import os

# Set of keywords to trigger automation
KEYWORDS = {"refund", "stop", "complaint", "cancel", "issue"}

# Output log file
OUTPUT_DIR = "output"
LOG_FILE = os.path.join(OUTPUT_DIR, "transcripts.txt")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

def log_transcription(text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")

def detect_keywords(text):
    found_keywords = [word for word in KEYWORDS if word in text.lower()]
    return found_keywords

def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # Range: -1 (negative) to +1 (positive)

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise...")
        recognizer.adjust_for_ambient_noise(source)
        print("🎤 Listening for speech... (say 'stop' to end)")

        while True:
            try:
                print("🔊 Speak now...")
                audio = recognizer.listen(source, timeout=5)

                # Transcribe audio using Google Speech API
                transcript = recognizer.recognize_google(audio)
                print(f"📝 You said: {transcript}")

                # Log to file
                log_transcription(transcript)

                # Check for keywords
                keywords_found = detect_keywords(transcript)
                if keywords_found:
                    print(f"⚠️ Keyword(s) detected: {', '.join(keywords_found)}. Trigger automation!")

                # Sentiment analysis
                sentiment_score = analyze_sentiment(transcript)
                if sentiment_score < -0.3:
                    print("😠 Negative sentiment detected.")
                elif sentiment_score > 0.3:
                    print("😊 Positive sentiment detected.")

                # Stop condition
                if "stop" in transcript.lower():
                    print("🛑 Stop command received. Exiting.")
                    break

            except sr.WaitTimeoutError:
                print("⏱️ Listening timeout. No speech detected.")
            except sr.UnknownValueError:
                print("🤔 Could not understand audio.")
            except sr.RequestError as e:
                print(f"❌ Could not request results from API: {e}")
            except KeyboardInterrupt:
                print("\n🛑 Interrupted by user.")
                break

if __name__ == "__main__":
    main()
