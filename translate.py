from googletrans import Translator


def translate_from_eng_to_ru(source:str) -> str:
    '''Функция перевода строки с английского на русский'''
    translated = Translator().translate(text=source, src='en', dest='ru')
    return translated.text
