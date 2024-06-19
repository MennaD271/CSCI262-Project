words = []

with open("./SRC/rockyou.txt", "r", encoding='latin-1') as w:
    for line in w:
        word = w.readline()
        words.append(word)

words.sort()

length_8 = list(filter(lambda word: len(word.strip()) == 8, words))[:100]
length_10 = list(filter(lambda word: len(word.strip()) == 10, words))[:100]
length_12 = list(filter(lambda word: len(word.strip()) == 12, words))[:100]
    
with open("./SRC/datasets/dataset1.txt", "w") as w:
    for word in length_8:
        w.write(word + "\n")

with open("./SRC/datasets/dataset2.txt", "w") as w:
    for word in length_10:
        w.write(word + "\n")

with open("./SRC/datasets/dataset3.txt", "w") as w:
    for word in length_12:
        w.write(word + "\n")