def get_num_words(content: str):
    return len(content.split())


def get_character_count(content: str):
    num_chars = {"a" : 0}
    for char in content:
        if char.lower() in num_chars:
            num_chars[char.lower()] += 1
        else:
            num_chars[char.lower()] = 1

    return num_chars


def get_list_of_chars(char_dict):
    char_list = list(char_dict.items())
    char_list.sort()
    return char_list
