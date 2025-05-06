def count_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    
    lowercase_char_counts = {}
    for char in text:
        lowercase_char= char.lower()
        lowercase_char_counts[lowercase_char] = lowercase_char_counts.get(lowercase_char,0)+1
    return lowercase_char_counts 

def sorted_list(character_count):
    sorted_counts_list = []
    for char, count in character_count.items():
      if char.isalpha():
        sorted_counts_list.append({"char": char, "num": count})
    sorted_counts_list.sort(key=lambda item: item["num"], reverse=True)
    return sorted_counts_list 
