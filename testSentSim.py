import math


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def normalize(a):
    length = 0
    for x in a:
        length += x * x
    length **= 0.5
    if length == 0:
        return a
    b = [x / length for x in a]
    return b


def cosine_sim(a, b):
    summation = 0
    for i in range(len(a)):
        summation += a[i] * b[i]
    return summation


def initialise():
    print("Loading sentence vectors...")
    with open("./sts-data/sts-" + task + "-vec.txt", "r") as fileObj:
        for line in fileObj:
            word = line.split()[0]
            word = str(word)
            line = list(map(float, line.split()[1:]))
            W1[word] = normalize(line)
            keys_index.append(word)
    print("Loaded sentence vectors. Fire in the hole.")


W1 = {}
keys_index = []
task = "headlines"


def main():
    initialise()
    for i in range(0, len(keys_index), 2):
        print(int(cosine_sim(W1[keys_index[i]], W1[keys_index[i + 1]]) * 100))


if __name__ == "__main__":
    main()
