import ReadFile
import DataParsing
import Graphing
import Clustering
import random


def _askUser():
    print("Please input what fields you would like to use")
    print("you can enter up to 3 with there being 4 fields from 1 - 4")
    print("The fields being 1. Sepal Length, 2. Sepal Width, 3. Petal Length, 4. Petal Width")
    user_in = input("Please separate your inputs of the fields you want via a space\n")
    split_user = user_in.split(" ")
    return split_user


def _generateTestSet(data_set):
    data_indexes = []
    testing_set = []

    current_class = data_set[0].get_class()

    i = 0
    for data in data_set:
        if data.data_class != current_class:
            data_indexes.append(i)
            current_class = data.data_class
        i += 1
    lower_bound = 1

    data_indexes.append(len(data_set))

    x = 0
    index = 0
    while index < 3:
        rand_bound = random.randint(1, 10)
        for j in range(rand_bound):
            rand_num = -1
            while rand_num in testing_set or rand_num == -1:
                rand_num = random.randint(lower_bound, data_indexes[index]) - 1 # so it starts at 0 not 1
            testing_set.append(rand_num)
            x += 1
        lower_bound = data_indexes[index]
        index += 1

    return testing_set



def _run():
    data_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
    user_input = _askUser()
    converted_input = []
    for i in user_input:
        converted_input.append(DataParsing.convetToNumber(i) - 1)

    data_set = DataParsing.parseData(ReadFile.readFile("irisData.txt"), converted_input)

    testing_indexes = _generateTestSet(data_set)
    testing_indexes.sort(reverse=True)
    print(testing_indexes)

    # write a method to keep some data back as a testing data

    used_names = []
    for current_input in converted_input:
        used_names.append(data_names[current_input])

    # part 1
    Graphing.newDrawGraph(data_set, used_names)

    # part 2
    clusters = Clustering.chooseStartingClusterCenters(data_set)
    Graphing.newPlot3DClustering(clusters, used_names)

    # part 3
    test_set = []
    for index in testing_indexes:
        test_data = data_set[index]
        test_set.append(test_data)
        data_set.remove(test_data)

    Clustering.testClustering(clusters, test_set)

_run()
