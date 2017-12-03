import statistics
import matplotlib.pyplot as plt



def initialise():
    print("Loading gs file")
    with open(sts_dataset_path + "STS2016.gs.answer-answer.txt", "r") as fileObj:
        lineNum = 1
        for line in fileObj:
            word = str(line.strip())
            if len(word) != 0:
                W.add(lineNum)
            lineNum = lineNum + 1
    print("Loaded gs file")


def getSentences():
    g = open(".././sts-data/STS2016.input.answer-answer.txt", "w+")
    print("Loading input file")
    with open(sts_dataset_path + "STS2016.input.answer-answer.txt", "r") as fileObj:
        lineNum = 1
        for line in fileObj:
            line = str(line.strip())
            lineParts = line.split('\t')
            if lineNum in W:
                g.write(lineParts[0] + "\n")
                g.write(lineParts[1] + "\n")
            lineNum = lineNum + 1
    g.close()
    print("Loaded input file")


def analysis():
    with open(".././sts-data/sts-ans-ans-adj-no-sigmoid.txt", "r") as fileObj:
        for line in fileObj:
            part = line.split()
            part = list(map(int, part))
            if part[1] in sim_values.keys():
                sim_values[part[1]].append(part[0])
            else:
                sim_values[part[1]] = [part[0]]

    for key in sorted(sim_values.keys()):
        print(key, " ", statistics.stdev(sim_values[key]), statistics.mean(sim_values[key]))
        plt.hist(sim_values[key], bins=30)
        plt.ylabel(key)
        plt.show()


W = set()
sim_values = dict()
count = dict()
sts_dataset_path = "/home/zoro/Documents/local_ss164gd/Sem_2/ELEC599/Data/Dataset/sts2016-english-with-gs-v1.0/"


def main():
    # initialise()
    # getSentences()
    analysis()


if __name__ == "__main__":
    main()
