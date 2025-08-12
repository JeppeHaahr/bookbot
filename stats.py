def get_book_word_count(file):
    with open(file) as f:
        word_count = len(f.read().split())
    return word_count

def get_characters(file):
    with open(file) as f:
        list_of_characters = {}
        for character in f.read().lower():
            if character not in list_of_characters:
                list_of_characters.update({character: 1})
            elif character in list_of_characters:
                list_of_characters[character] += 1
    return list_of_characters

def sort_on(items):
    return items["num"]

def sort_list(dict_for_sorting):
    new_list = []
    for i in dict_for_sorting:
        if i.isalpha() == True:
            new_list.append({"char": i, "num": dict_for_sorting[i]})
    new_list.sort(reverse = True, key = sort_on)
    return new_list