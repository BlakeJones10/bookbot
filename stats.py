def get_word_count(text):
    words = text.split()
    return len(words)


def get_character_count(text):
    characters = {}
    for char in text.lower():
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_on(characters):
    char_list = []
    for char, count in characters.items():
        char_list.append({"char": char, "num": count})

    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list
