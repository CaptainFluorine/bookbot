def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_of_characters(text):
    lower_text = text.lower()
    #rint(lower_text)
    alphabet_dict = {}
    for i in range(0, len(text) -1):
        if lower_text[i] in alphabet_dict and lower_text[i].isalpha() == True:
            alphabet_dict[lower_text[i]] = alphabet_dict[lower_text[i]] + 1
        elif lower_text[i].isalpha() == True:
            alphabet_dict[lower_text[i]] = 1
    #print(alphabet_dict)
    return alphabet_dict

def dict_with_two_keys(key, count)  :
    return {"key": key, "count": count}

def sort_on(dict):
    return dict["count"]



