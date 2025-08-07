
def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    lower_text = text.lower()
    character_dict = {}
    for charater in lower_text:
        if charater in character_dict:
            character_dict[charater] += 1
        else:
            character_dict[charater] = 1
    return character_dict

def sort_on(items):
    return items["num"]

def sorted_dict(char_count):
    unsorted_char = []
    for char in char_count:
        unsorted_char.append({"char": char, "num": char_count[char]})
    unsorted_char.sort(reverse=True, key=sort_on)
    return unsorted_char
    