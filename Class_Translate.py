"""ספריות"""
from googletrans import *
from googletrans import LANGUAGES

###########################################
translator = Translator()
global_langaes = LANGUAGES

###########################################


class Class_Translate_Language:
    def __init__(self, text):
        '''
        פעולה בונה 
        text (str): טקס לקריאה
        '''
        self.text = text

    def __iter__(self):
        '''
        פשוט כדי לחזיר את תחונות של ספריה
        '''
        return self

    def Translator_Text(self, language='en'):
        """
            הפעולה מחקבלת שפה ומתרגמת את טקסט
            הוא מחזר את טקסט מתוגם לאותו שפה
            """
        global translator
        source_lang = translator.detect(self.text)
        text_translate = translator.translate(
            self.text, src=source_lang.lang, dest=language)
        return text_translate.text

    def Dictionary_All(self):
        global global_langaes
        return global_langaes

    def Key_Languages(self):
        global global_langaes
        return global_langaes.keys()

    def List_Languages(self):
        global global_langaes
        return global_langaes.values()

ה   
if __name__ == "__main__":
    text = 'שלום'
    ctl = Class_Translate_Language(text)
    print(ctl.Dictionary_All())
    translator = ctl.Translator_Text('French')
    print(translator)
