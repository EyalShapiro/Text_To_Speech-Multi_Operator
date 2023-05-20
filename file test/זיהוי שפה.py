from googletrans import *

translator = Translator()

text = "ddשש"

lang = translator.detect(text)

print(lang)  # Output: fr
