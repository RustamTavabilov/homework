root_word = 'rich'
other_word = ['RIch3', 'rich4']
root_word_low = root_word.lower()
print(root_word_low)
    same_words = []
    for i in range(len(other_word)):
        #other_word_low.append(other_word[i].lower())
        if other_word[i].lower().endswith(root_word_low):
            same_words.append(other_word[i])
    print(same_words)