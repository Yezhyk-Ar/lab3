from googletrans import Translator, LANGUAGES
from langdetect import detect, detect_langs


def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        translated = translator.translate(text, src=scr, dest=dest)
        return translated.text
    except Exception as e:
        return str(e)


def LangDetect(txt):
    try:
        # Визначення мови тексту з рівнем впевненості
        detected_langs = detect_langs(txt)
        # Повертаємо першу мову з найбільшим рівнем впевненості
        return f"Detected(lang={detected_langs[0].lang}, confidence={detected_langs[0].prob})"
    except Exception as e:
        return f"Error: {str(e)}"


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