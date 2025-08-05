def sort_words_in_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sentence = ' '.join(words)
    return sorted_sentence
sentence = "This is a man world"
sort_result = sort_words_in_sentence(sentence)
print("Sorted sntence:",sort_result)
