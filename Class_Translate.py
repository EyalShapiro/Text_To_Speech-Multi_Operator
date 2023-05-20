"""ספריות"""
from googletrans import *
from googletrans import LANGUAGES

###########################################
global_langaes = LANGUAGES

###########################################


class Translate_Language:
    def __init__(self, text):
        '''
        פעולה בונה 
        text (str): טקס לקריאה
        '''
        self.text = text
        self.translator = Translator()

    # def __iter__(self):
    #     '''
    #     פשוט כדי לחזיר את תחונות של ספריה
    #     '''
    #     return self

    def Translator_Text(self, language='en'):
        """
        הפעולה מחקבלת שפה ומתרגמת את טקסט שבתוך ספרייה לאותו השפה
        """
        global translator
        source_lang = self.translator.detect(self.text)
        text_translate = self.translator.translate(
            self.text, src=source_lang.lang, dest=language)
        return text_translate.text

    def Language_Detection(self, text):
        """
        הפעולה מקבלת טקסט
        מזהה את שפת הדיבור שבה הטקסט רשום
        ומחזירה את מפתח השפה
        פעולה נימצת כאן רק בגלל שאני נזר בסיפר החיצונית
        """
        detection = self.translator.detect(text)
        return detection

    def Dictionary_All(self):
        global global_langaes
        return global_langaes

    def Key_Languages(self):
        global global_langaes
        return global_langaes.keys()

    def List_Languages(self):
        global global_langaes
        return global_langaes.values()


if __name__ == "__main__":
    text = 'שלום'
    ctl = Translate_Language(text)
    print(ctl.Dictionary_All())
    translator = ctl.Translator_Text('French')
    print(translator)
