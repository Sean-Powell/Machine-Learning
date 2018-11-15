import ReadFile
import DataParsing
import Graphing
import Clustering


def _askUser(length):
    print("Please input what fields you would like to use")
    print("you can enter up to 3 with there being ", (length - 1), " fields from 1 -", (length - 1))
    print("The fields being 1. Sepal Length, 2. Sepal Width, 3. Petal Length, 4. Petal Width")
    user_in = input("Please separate your inputs of the fields you want via a space\n")
    split_user = user_in.split(" ")
    return split_user


def _run():
    data_names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
    data_set = DataParsing.parseData(ReadFile.readFile("irisData.txt"))
    user_input = _askUser(data_set[0].data_size)
    amount_of_fields = len(user_input)
    converted_input = []
    for i in user_input:
        converted_input.append(DataParsing.convetToNumber(i))
    Graphing.drawGraph(amount_of_fields, converted_input, data_set, data_names)
    clusters = Clustering.formClusters(Clustering.randomlySelectClusters(data_set, converted_input), data_set, converted_input)
    final_clusters = Clustering.recalculateClusters(clusters, converted_input)
    print("final clusters:")
    length_1 = len(final_clusters[0].list_of_points)
    length_2 = len(final_clusters[1].list_of_points)
    length_3 = len(final_clusters[2].list_of_points)
    print("cluster 1 length: ", length_1, ", cluster 2 length: ", length_2,
          ", cluster 3 length: ", length_3, ", total length", (length_1 + length_2 + length_3))

    Graphing.plot3DClustering(final_clusters, converted_input, data_names)
_run()
