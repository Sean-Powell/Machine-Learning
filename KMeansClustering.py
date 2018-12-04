import math
import sys

import Cluster
import random


def _formCluster(index, data_set):
    data = data_set[index]
    x = data.get_x()
    y = data.get_y()
    z = data.get_z()
    cluster = Cluster.ClusterCenter(x, y, z, x, y, z, data.get_class())
    return cluster


def chooseStartingClusterCenters(data_set):
    class_indexes = []

    current_class = data_set[0].get_class()
    i = 0
    for data in data_set:
        if data.get_class() != current_class:
            class_indexes.append(i)
            current_class = data.get_class()
        i += 1

    cluster_list = [_formCluster(random.randint(1, class_indexes[0]) - 1, data_set),
                    _formCluster(random.randint(class_indexes[0], class_indexes[1]) - 1, data_set),
                    _formCluster(random.randint(class_indexes[1], len(data_set)) - 1, data_set)]

    return _clusterForming(cluster_list, data_set)


def _clusterForming(clusters, data_set):
    index = 0
    for data in data_set:
        print("Data Point:", index)
        found = 0
        # for cluster in clusters:
        #     if cluster.cluster_center_x == data.get_x() and cluster.cluster_center_y == data.get_y() \
        #             and cluster.cluster_center_z == data.get_z():
        #         found = 1
        if found == 0:
            distance_to_closest = sys.maxsize
            closest_index = -1
            i = 0
            for cluster in clusters:
                euclidean_distance = math.sqrt(math.pow(float(data.get_x()) - float(cluster.get_x()), 2) +
                                               math.pow(float(data.get_y()) - float(cluster.get_y()), 2) +
                                               math.pow(float(data.get_z()) - float(cluster.get_z()), 2))
                print(euclidean_distance, "to point", i)
                if euclidean_distance < distance_to_closest:
                    print(i, "is closest")
                    distance_to_closest = euclidean_distance
                    closest_index = i
                i += 1
            clusters[closest_index].add_to_list(data)
    index += 1

    return _refactorClusters(clusters)


def _refactorClusters(clusters):
    # change so when x_pos is updated the original location is not lost
    new_clusters = []
    for cluster in clusters:
        num_of_data_points = 1
        x_total = float(cluster.get_x())
        y_total = float(cluster.get_y())
        z_total = float(cluster.get_z())

        for data_point in cluster.get_list():
            x_total += float(data_point.get_x())
            y_total += float(data_point.get_y())
            z_total += float(data_point.get_z())
            num_of_data_points += 1

        x_average = x_total / num_of_data_points
        y_average = y_total / num_of_data_points
        z_average = z_total / num_of_data_points
        new_clusters.append(Cluster.ClusterCenter(x_average, y_average, z_average, cluster.get_original_x(),
                                                  cluster.get_original_y(), cluster.get_original_z(),
                                                  cluster.get_class()))

    num_of_changes = 0
    for i in range(3):
        for data_point in clusters[i].get_list():
            closest_cluster = 0
            closest_distance = sys.maxsize
            for j in range(3):
                euclidean_distance = math.sqrt(math.pow(float(data_point.get_x()) - new_clusters[j].get_x(), 2) +
                                               math.pow(float(data_point.get_y()) - new_clusters[j].get_y(), 2) +
                                               math.pow(float(data_point.get_z()) - new_clusters[j].get_z(), 2))

                if euclidean_distance < closest_distance:
                    closest_distance = euclidean_distance
                    closest_cluster = j
            new_clusters[closest_cluster].add_to_list(data_point)
            if i != closest_cluster:
                num_of_changes += 1

    if num_of_changes >= 3:
        return _refactorClusters(new_clusters)
    else:
        return new_clusters


def testClustering(clusters, test_set):
    correct = 0
    for test_data in test_set:
        closest_index = 0
        closest_distance = sys.maxsize
        for i in range(3):
            euclidean_distance = math.sqrt(math.pow(float(test_data.get_x()) - clusters[i].get_x(), 2) +
                                           math.pow(float(test_data.get_y()) - clusters[i].get_y(), 2) +
                                           math.pow(float(test_data.get_z()) - clusters[i].get_z(), 2))
            if euclidean_distance < closest_distance:
                closest_index = i
                closest_distance = euclidean_distance

        if test_data.get_class() == clusters[closest_index].get_class():
            correct += 1

    print("The network got", correct, "right out of", len(test_set))
