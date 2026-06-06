def word_count(sentence):
    j = 0
    word = None
    length = len(sentence)
    frequency_counter = {}

    for i in range(length + 1):
        if i == length or sentence[i] == " ":
            word = sentence[j:i]
            if word:
                frequency_counter[word] = frequency_counter.get(word, 0) + 1
            j = i + 1
    return frequency_counter


print(word_count("the cat sat on the mat"))
