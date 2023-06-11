import sounddevice as sd
import soundfile as sf


def Voice_rec():
	fs = 44100
	# seconds
	duration = 5
	myrecording = sd.rec(int(duration * fs),
						samplerate=fs, channels=2)
	sd.wait()
	# Save as FLAC file at correct sampling rate
	return sf.write('my_Audio_file.wav', myrecording, fs)


if __name__ == "__main__":
    print("start rec")
    Voice_rec()
    print("finish")
