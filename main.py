
import pyttsx3
import os
from playsound import playsound


def text_to_speech(text, speed=160, volume=1.0):
    """Convert text to speech, save it, and play it."""
    filename = os.path.abspath("output.wav")
    engine = None

    try:
        engine = pyttsx3.init()
        engine.setProperty("rate", speed)
        engine.setProperty("volume", volume)

        voices = engine.getProperty("voices")
        if voices:
            engine.setProperty("voice", voices[0].id)

        print("Generating speech...")
        engine.save_to_file(text, filename)
        engine.runAndWait()
        engine.stop()
        engine = None

        if os.path.exists(filename) and os.path.getsize(filename) > 0:
            print("Audio saved successfully!")
            print("File location:", filename)

            print("Playing audio...")
            playsound(filename)
            print("Playback completed!")
        else:
            print("Audio file was not created.")

    except Exception as error:
        print("An error occurred:", error)

    finally:
        if engine is not None:
            engine.stop()


def choose_speed():
    """Ask the user to select speech speed."""
    while True:
        try:
            speed = int(input("Enter speed (100-250): "))
            if 100 <= speed <= 250:
                return speed
            print("Enter a value between 100 and 250.")
        except ValueError:
            print("Please enter a valid integer.")


def choose_volume():
    """Ask the user to select speech volume."""
    while True:
        try:
            volume = float(input("Enter volume (0.0-1.0): "))
            if 0.0 <= volume <= 1.0:
                return volume
            print("Volume must be between 0.0 and 1.0.")
        except ValueError:
            print("Enter a volume between 0.0 and 1.0.")


def main():
    print("=" * 40)
    print("     TEXT TO SPEECH CONVERTER")
    print("=" * 40)

    while True:
        user_text = input("Enter text to convert: ").strip()
        if user_text:
            break
        print("Please enter some text.")

    speed = choose_speed()
    volume = choose_volume()

    text_to_speech(user_text, speed, volume)

    print("Thank you for using the converter!")


if __name__ == "__main__":
    main()
