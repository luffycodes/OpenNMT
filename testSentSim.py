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
    with open("pred.txt", "r") as fileObj:
        for line in fileObj:
            word = line.split()[0]
            word = str(word)
            line = list(map(float, line.split()[1:]))
            W1[word] = normalize(line)
    print("Loaded sentence vectors. Fire in the hole.")


W1 = {}


def main():
    initialise()
    for key1 in W1.keys():
        for key2 in W1.keys():
            print(key1, " ", key2, " ", cosine_sim(W1[key1], W1[key2]))


if __name__ == "__main__":
    main()
