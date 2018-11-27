import ReadFile
import DataParsing
import Graphing
import KMeansClustering
import KNNClustering
import random
import math


def _askUser():
    print("Please input what fields you would like to use")
    print("you can enter up to 3 with there being 4 fields from 1 - 4")
    print("The fields being 1. Sepal Length, 2. Sepal Width, 3. Petal Length, 4. Petal Width")
    user_in = input("Please separate your inputs of the fields you want via a space\n")
    split_user = user_in.split(" ")
    return split_user


def _generateTestSet(data_set, percentage):
    length = len(data_set)
    percent = math.ceil(length / 100)
    amount = percent * percentage

    testing_set = []

    for i in range(amount):
        generated_number = random.randint(1, length) - 1
        while generated_number in testing_set:
            generated_number = random.randint(1, length) - 1
        testing_set.append(generated_number)

    return testing_set


correct = []


def _run():
    data_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
    user_input = _askUser()
    converted_input = []
    for i in user_input:
        converted_input.append(DataParsing.convetToNumber(i) - 1)

    data_set = DataParsing.parseData(ReadFile.readFile("irisData.txt"), converted_input)

    testing_indexes = _generateTestSet(data_set, 10)
    testing_indexes.sort(reverse=True)
    print(testing_indexes)

    # write a method to keep some data back as a testing data

    used_names = []
    for current_input in converted_input:
        used_names.append(data_names[current_input])

    # part 1
    Graphing.newDrawGraph(data_set, used_names)

    # part 2
    clusters = KMeansClustering.chooseStartingClusterCenters(data_set)
    Graphing.DrawClustering(clusters, used_names)

    # part 3
    test_set = []
    for index in testing_indexes:
        test_data = data_set[index]
        test_set.append(test_data)
        data_set.remove(test_data)

    correct.append(KNNClustering.calculateKNN(data_set, test_set, 13))
    # KMeansClustering.testClustering(clusters, test_set)


_run()
