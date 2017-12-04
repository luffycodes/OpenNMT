import statistics
import matplotlib.pyplot as plt


# Find line numbers which have gold standard scores
def initialise():
    print("Loading " + task + " gs file")
    with open(sts_dataset_path + "STS2016.gs." + task + ".txt", "r") as fileObj:
        lineNum = 1
        for line in fileObj:
            word = str(line.strip())
            if len(word) != 0:
                W.add(lineNum)
                gs_score[lineNum] = word
            lineNum = lineNum + 1
    print("Loaded " + task + " gs file")


# Find set of lines which have their score in gold standard file
def getSentences():
    g = open(".././sts-data/sts-" + task + "_gs_scores.txt", "w+")
    print("Loading " + task + " input file")
    with open(sts_dataset_path + "STS2016.input." + task + ".txt", "r") as fileObj:
        lineNum = 1
        for line in fileObj:
            line = str(line.strip())
            lineParts = line.split('\t')
            if lineNum in W:
                g.write(gs_score[lineNum] + " ")
                g.write(lineParts[0] + " ")
                g.write(lineParts[1] + "\n")
            lineNum = lineNum + 1
    g.close()
    print("Loaded  " + task + " input file")


# Given adjacent cosine score & gs score, plot histogram
def analysis():
    with open(".././sts-data/sts-" + task + "-adj-no-sigmoid.txt", "r") as fileObj:
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


task = "answer-answer"
W = set()
sim_values = dict()
count = dict()
gs_score = dict()
sts_dataset_path = "/home/zoro/Documents/local_ss164gd/Sem_2/ELEC599/Data/Dataset/sts2016-english-with-gs-v1.0/"


def main():
    initialise()
    getSentences()
    # analysis()


if __name__ == "__main__":
    main()
