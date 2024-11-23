import os
import json
from module1 import TransLate


def get_text_stats(file_path):
    """Отримати статистику тексту з файлу."""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    num_chars = len(text)
    num_words = len(text.split())
    num_sentences = text.count('.') + text.count('!') + text.count('?')
    return text, num_chars, num_words, num_sentences


def main():
    # Зчитування конфігураційного файлу
    config_file = "C:/Users/gzare/PycharmProjects/lab3/config.json"
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            config = json.load(file)

        input_file = config["file"]
        lang_code = config["language"]
        output = config["output"]
        char_limit = config.get("char_limit", float('inf'))
        word_limit = config.get("word_limit", float('inf'))
        sentence_limit = config.get("sentence_limit", float('inf'))

        if not os.path.isfile(input_file):
            print("Error: File not found.")
            return

        text, num_chars, num_words, num_sentences = get_text_stats(input_file)

        if num_chars > char_limit or num_words > word_limit or num_sentences > sentence_limit:
            print(f"File: {input_file}")
            print(f"Size: {num_chars} chars")
            print(f"Words: {num_words}")
            print(f"Sentences: {num_sentences}")
            print(f"Text exceeds specified limits.")
            return

        print(f"File: {input_file}")
        print(f"Size: {num_chars} chars")
        print(f"Words: {num_words}")
        print(f"Sentences: {num_sentences}")

        translated_text = TransLate(text, 'auto', lang_code)

        if output == "screen":
            print(f"Translated Text:\n{translated_text}")
        elif output == "file":
            output_file = f"{os.path.splitext(input_file)[0]}_{lang_code}.txt"
            with open(output_file, "w", encoding='utf-8') as file:
                file.write(translated_text)
            print("Ok")
        else:
            print("Error: Invalid output option.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
