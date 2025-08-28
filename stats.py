def get_num_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def get_character_counts(book_text):
    lowercase_text = book_text.lower()
    character_counts = {}
    for char in lowercase_text:
        if char not in character_counts:
            character_counts[char] = 1
        else:
            character_counts[char] += 1
    return character_counts

def sort_on(dictionary):
    return dictionary["num"]

def get_sorted_chars(character_counts_dict):
    
    sorted_list = []
    for char,count in character_counts_dict.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(key=sort_on, reverse=True)

    return sorted_list
   