def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_characters = count_characters(text)
    sorted_characters = sort_on(num_characters)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for character in sorted_characters:
        if not character["character"].isalpha():
            continue
        print(f"The '{character["character"]}' character was found {character["count"]} times")
    print("--- End report ---")
    
def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters = {}
    lowered_text = text.lower()
    for character in lowered_text:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_on(characters):
    dict_list = []
    for character, count in characters.items():
        dict_list.append({'character': character, 'count': count})
    
    # Sort the list of dictionaries by the 'count' key in descending order
    dict_list.sort(key=lambda x: x['count'], reverse=True)
    
    return dict_list

main()