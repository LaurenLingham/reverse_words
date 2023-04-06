def spin_words(sentence):
    
    words = sentence.split(" ")
    changed_words = []

    for word in words:
        if len(word) >= 5:
            changed_words.append(word[::-1])
        else:
            changed_words.append(word)

    return " ".join(changed_words)

assert spin_words('Hello my name is Timothy') == 'olleH my name is yhtomiT'
