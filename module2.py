# translation_package/module2.py
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0
from googletrans import Translator, LANGUAGES


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = GoogleTranslator(source=scr, target=dest)
        return translator.translate(text)
    except Exception as e:
        return str(e)


def LangDetect(text: str, set: str) -> str:
    try:
        language = detect(text)
        if set == "lang":
            return language
        elif set == "confidence":
            # `langdetect` does not provide confidence score
            return "Confidence score not available"
        else:
            return f"Language: {language}"
    except Exception as e:
        return str(e)


def CodeLang(lang: str) -> str:
    try:
        if lang in LANGUAGES.values():
            return [code for code, name in LANGUAGES.items() if name == lang][0]
        elif lang in LANGUAGES.keys():
            return LANGUAGES[lang]
        else:
            return "Error: Language not found."
    except Exception as e:
        return str(e)


def LanguageList(out: str, text: str) -> str:
    try:
        translator = Translator()
        languages = LANGUAGES.items()
        lines = ["N Language ISO-639 code Text"]
        for idx, (code, lang) in enumerate(languages, start=1):
            translated_text = translator.translate(text, dest=code).text
            lines.append(f"{idx} {lang} {code} {translated_text}")

        result = "\n".join(lines)
        if out == "screen":
            print(result)
        elif out == "file":
            with open("languages.txt", "w") as file:
                file.write(result)
        else:
            return "Error: Invalid output option."

        return "Ok"
    except Exception as e:
        return str(e)