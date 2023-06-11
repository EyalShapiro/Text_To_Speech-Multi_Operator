import sounddevice as sd
import wavio as wv

class Speech_To_Text:
    def __init__(self, location='C:\Eyal\Codes\Text_To_Speech-Multi_Operator\\', file_name='say.wav'):
        '''
            location(str): מיקום הקובץ
            file_name(str): שם הקובץ
            full__file_location(str):מיקום הקובץ המלא
            '''
        # self.language = language  # אין פעולה לזהוי כאן כי היא מזוה לפני הכניסה לספריה
        self.file_name = file_name
        self.location = location
        self.full__file_location=self.Get_Full_file_location()
    def Get_Full_file_location(self):
        """
        מחזיר את מיקום הקבוץ המלא
        """
        full_file=''
        if(self.location=='\\'):
            full_file=self.location+self.file_name
        else:
            full_file=self.location+'\\'+self.file_name
        return full_file



    def Recording_Speech(self,duration_time=5,sample_rate=48000):
        '''
        duration_time(int):משך זמן מייצג את משך ההקלטה בשניות 
        sample_rate(int):קצב/תדירות הדגימה #sampling frequency

        '''
        print("Recording start")
        recording = sd.rec(int(duration_time * sample_rate), samplerate=sample_rate, channels=2)
        sd.wait()  # Wait until recording is finished
        print("Recording finished.")
        wv.write("recording.wav", recording, sample_rate, sampwidth=2)
        print("Audio saved to", self.file_name)


if __name__ == '__main__':
    pass
    

