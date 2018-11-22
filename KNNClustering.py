import math
import sys
class EuclidianObj:
    distance = 0
    original_index = 0

    def __init__(self, distance, index):
        self.distance = distance
        self.original_index = index

    def get_distance(self):
        return self.distance

    def get_index(self):
        return self.original_index


def calculateKNN(data_set, testing_data, k):
    print("maybe works who knows")
    correct = 0
    for test_data in testing_data:
        euclidean_distances = []
        for i in range(len(data_set)):
            e_obj = EuclidianObj(_calculateEuclideanDistance(test_data, data_set[i]), i)
            euclidean_distances.append(e_obj)
        euclidean_distances.sort(key=lambda c: EuclidianObj.distance, reverse=False)

        k_points = []
        for i in range(k):
            k_points.append(data_set[euclidean_distances[i].get_index()])

        class_counts = [0, 0, 0]
        for point in k_points:
            point_class = point.get_class()
            if 'Iris-setosa' in point_class:
                class_counts[0] += 1
            elif 'Iris-versicolor' in point_class:
                class_counts[1] += 1
            elif 'Iris-virginica' in point_class:
                class_counts[2] += 1

        max = sys.maxsize
        max_index = 0
        for i in range(3):
            if class_counts[i] < max:
                max = class_counts[i]
                max_index = i

        predicted_class = 0
        if max_index == 0:
            predicted_class = 'Iris-setosa'
        elif max_index == 1:
            predicted_class = 'Iris-versicolor'
        else:
            predicted_class = 'Iris-virginica'

        if predicted_class in test_data.get_class():
            correct += 1

    print("KNN got ", correct, " out of ", len(testing_data))


def _calculateEuclideanDistance(point_one, point_two):
    return math.sqrt(math.pow(float(point_one.get_x()) - float(point_two.get_x()), 2) +
                     math.pow(float(point_one.get_y()) - float(point_two.get_y()), 2) +
                     math.pow(float(point_one.get_z()) - float(point_two.get_z()), 2))
