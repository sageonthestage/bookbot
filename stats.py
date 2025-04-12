def count_words(text):
    words = text.split()
    return len(words)

def char_counts(text):
    char_count = {}

    for char in text:
        if not char.isalpha():
            continue
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def dictionary_list(dictionary):
    result = []
    for key, value in dictionary.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["count"] = value
        result.append(new_dict)
    result.sort(key=lambda x: x["char"])
    return result
