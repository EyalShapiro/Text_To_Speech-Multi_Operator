import sounddevice as sd
import wavio as wv
#https://www.geeksforgeeks.org/create-a-voice-recorder-using-python/
duration = 5  # Duration of recording in seconds#משתנה משך הזמן מייצג את משך ההקלטה בשניות
sample_rate = 98000  # Sampling rate#הוא קצב הדגימה

print("Recording start")

# Record audio
recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=2)
sd.wait()  # Wait until recording is finished

print("Recording finished.")

# Save the recorded audio to a WAV file
output_filename = "recording.wav"
wv.write("recording.wav", recording, sample_rate, sampwidth=2)
print("Audio saved to", output_filename)
