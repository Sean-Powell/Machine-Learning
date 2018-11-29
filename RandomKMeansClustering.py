import Cluster
import random
import sys
import math
import Graphing


class DimensionLimits:
    max_x = 0
    max_y = 0
    max_z = 0
    min_x = 0
    min_y = 0
    min_z = 0

    def __init__(self, ux, uy, uz, lx, ly, lz):
        self.max_x = ux
        self.max_y = uy
        self.max_z = uz
        self.min_x = lx
        self.min_y = ly
        self.min_z = lz

    def get_upper_x(self):
        return self.max_x

    def get_upper_y(self):
        return self.max_y

    def get_upper_z(self):
        return self.max_z

    def get_lower_x(self):
        return self.max_x

    def get_lower_y(self):
        return self.max_y

    def get_lower_z(self):
        return self.max_z


def _formRandomCluster(x, y, z, data_class):
    cluster = Cluster.RandomClusterCenter(x, y, z, data_class)
    return cluster


def randomlyChooseStartingCenters(data_set):
    max_x = sys.maxsize * -1
    min_x = sys.maxsize
    max_y = sys.maxsize * -1
    min_y = sys.maxsize
    max_z = sys.maxsize * -1
    min_z = sys.maxsize

    for data in data_set:
        x = float(data.get_x())
        y = float(data.get_y())
        z = float(data.get_z())

        if x < min_x:
            min_x = x

        if x > max_x:
            max_x = x

        if y < min_y:
            min_y = y

        if y > max_y:
            max_y = y

        if z < min_z:
            min_z = z

        if z > max_z:
            max_z = z

    # create one cluster for each of the classes
    dimensions = DimensionLimits(max_x, max_y, max_z, min_x, min_y, min_z)

    clusters = [_formRandomCluster(random.uniform(min_x, max_x), random.uniform(min_y, max_y),
                                   random.uniform(min_z, max_z), 'Iris-setosa'),
                _formRandomCluster(random.uniform(min_x, max_x), random.uniform(min_y, max_y),
                                   random.uniform(min_z, max_z), 'Iris-versicolor'),
                _formRandomCluster(random.uniform(min_x, max_x), random.uniform(min_y, max_y),
                                   random.uniform(min_z, max_z), 'Iris-virginica')]

    return _clusterForming(clusters, data_set, dimensions)


def _clusterForming(cluster_list, data_set, dimensions):
    print("form clusters")
    for data in data_set:
        closest_index = 0
        closest_distance = sys.maxsize
        i = 0
        for i in range(3):
            cluster = cluster_list[i]
            eucledian_distance = math.sqrt(math.pow((float(cluster.get_x()) - float(data.get_x())), 2) +
                                           math.pow((float(cluster.get_y()) - float(data.get_y())), 2) +
                                           math.pow((float(cluster.get_z()) - float(data.get_z())), 2))

            if eucledian_distance < closest_distance:
                closest_distance = eucledian_distance
                closest_index = i

        cluster_list[closest_index].append(data)

    return _refactorClusters(cluster_list, 0, dimensions)


def _checkLimits(to_check, upper_limit, lower_limit):
    if to_check > upper_limit:
        return upper_limit
    elif to_check < lower_limit:
        return lower_limit
    else:
        return to_check


def _refactorClusters(cluster_list, times_run, dimensions):
    print("Refactoring Clusters")
    new_clusters = []

    for cluster in cluster_list:
        x = float(cluster.get_x())
        y = float(cluster.get_y())
        z = float(cluster.get_z())

        for data in cluster.get_list():
            x += float(data.get_x())
            y += float(data.get_y())
            z += float(data.get_z())

        x_average = x / (len(cluster.get_list()) + 1)
        y_average = z / (len(cluster.get_list()) + 1)
        z_average = z / (len(cluster.get_list()) + 1)

        x_average = _checkLimits(x_average, dimensions.max_x, dimensions.min_x)
        y_average = _checkLimits(y_average, dimensions.max_y, dimensions.min_y)
        z_average = _checkLimits(z_average, dimensions.max_z, dimensions.min_y)

        new_clusters.append(_formRandomCluster(x_average, y_average, z_average, cluster.get_data_class()))

    num_of_changes = 0
    for i in range(3):
        for data in cluster_list[i].get_list():
            closest_index = 0
            closest_distance = sys.maxsize
            for j in range(3):
                euclidian_distance = math.sqrt(math.pow(float(data.get_x()) - float(new_clusters[j].get_x()), 2) +
                                               math.pow(float(data.get_y()) - float(new_clusters[j].get_y()), 2) +
                                               math.pow(float(data.get_z()) - float(new_clusters[j].get_z()), 2))
                if euclidian_distance < closest_distance:
                    closest_distance = euclidian_distance
                    closest_index = j
            new_clusters[closest_index].append(data)
            if i != closest_index:
                num_of_changes += 1

    if num_of_changes >= 3:
        if times_run < 5:
            print("Times run =", times_run)
            times_run = times_run + 1
            Graphing.DrawClustering(cluster_list, ['x', 'y', 'z'])
            return _refactorClusters(new_clusters, times_run, dimensions)
        else:
            print("Max clustering reached returning")
            return new_clusters
    else:
        return new_clusters
