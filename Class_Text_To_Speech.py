from gtts import gTTS
###########################################


class Text_To_Speech:
    def __init__(self, text, language, location='C:\Eyal\Codes\Text_To_Speech-Multi_Operator\\', file_name='say.wav'):
        '''
            location(str): מיקום הקובץ
            text (str): טקס לקריאה
            language (str) : השפה/מפתח השפה
            file_name(str): שם הקובץ
            '''
        self.text = text
        self.language = language  # אין פעולה לזהוי כאן כי היא מזוה לפני הכניסה לספריה
        self.file_name = file_name
        self.location = location
        
    

if __name__ == "__main__":
    speech = Text_To_Speech('text', 'en')
    print(speech.text)
    speech.text = "help"
    print(speech.text)
 