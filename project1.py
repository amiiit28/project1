import speech_recognition as sr

# Use the 'r' prefix and make sure the username (amitg vs dhara) is correct!
filename = "C:\codes\internship project\STT_sttdemo.wav"
r = sr.Recognizer()

def transcribe_from_audiofile(path):
    try:
        with sr.AudioFile(path) as source:
            # Adjusts for background noise for a clearer read
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.record(source)
            
            # Perform the recognition
            text = r.recognize_google(audio)
            return text
            
    except sr.UnknownValueError:
        return "Error: Could not understand audio."
    except sr.RequestError as e:
        return f"Error: API Request failed; {e}"
    except FileNotFoundError:
        return "Error: File not found."

# Usage
result = transcribe_from_audiofile(filename)
print(f"Transcription: {result}")