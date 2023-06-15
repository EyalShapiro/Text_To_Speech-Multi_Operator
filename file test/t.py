import sounddevice as sd
import scipy.io.wavfile as wav

duration = 5  # Duration of recording in seconds#משתנה משך הזמן מייצג את משך ההקלטה בשניות
fs = 98000  # Sampling rate#הוא קצב הדגימה

print("Recording started...")

# Record audio
recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished

print("Recording finished.")

# Save the recorded audio to a WAV file
output_filename = "recording.wav"
wav.write(output_filename, fs, recording)

print("Audio saved to", output_filename)
# import required libraries
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
 
# Sampling frequency
freq = 44100
 
# Recording duration
duration = 5
 
# Start recorder with the given values
# of duration and sample frequency
recording = sd.rec(int(duration * freq),
                   samplerate=freq, channels=2)
 
# Record audio for the given number of seconds
sd.wait()
 
# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)
 
# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=2)
