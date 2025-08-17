def get_book_text(filePath):
    with open(filePath) as f:
        book_text = f.read()
    return book_text

def get_num_words(filePath):
    book_text = get_book_text(filePath)
    book_words = book_text.split()
    word_count = len(book_words)
    return word_count

def get_character_count(filePath):
    book_text = get_book_text(filePath)
    book_lower_case = book_text.lower()
    letter_count = {}
    for letter in book_lower_case:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(items):
    return items["num"]

def sort_character_list(filePath):
    letter_data = get_character_count(filePath)
    updated_dic = []
    for key in letter_data:
        num = letter_data[key]
        updated_pair = {'char': key, 'num': num}
        updated_dic.append(updated_pair)
    updated_dic.sort(key=sort_on,reverse=True)
    return updated_dic
        
