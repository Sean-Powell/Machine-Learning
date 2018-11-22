from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


def _newPlot3DGraph(data_set, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    for data in data_set:
        data_class = data.get_class()
        x = float(data.get_x())
        y = float(data.get_y())
        z = float(data.get_z())

        color = 'r'
        if 'Iris-versicolor' in data_class:
            color = 'g'
        elif 'Iris-virginica' in data_class:
            color = 'b'

        ax.scatter(x, y, z, c=color, marker='o')

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])


    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    plt.legend(handles=[red_patch, green_patch, blue_patch])

    plt.show()


def newDrawGraph(data_set, labels):
    data_length = data_set[0].get_size()
    if data_length == 1:
        _newPlot1DGraph(data_set, labels)
    elif data_length == 2:
        _newPlot2DGraph(data_set, labels)
    elif data_length == 3:
        _newPlot3DGraph(data_set, labels)


def DrawClustering(clusters, labels):
    if clusters[0].get_y() != 0 and clusters[0].get_z() != 0:
        _newPlot3DClustering(clusters, labels)
    elif clusters[0].get_y() != 0:
        _plot2DClustering(clusters, labels)
    else:
        _plot1DClustering(clusters, labels)


def _newPlot3DClustering(clusters, labels):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    i = 0

    for cluster in clusters:
        color = 'r'
        if i == 1:
            color = 'g'
        elif i == 2:
            color = 'b'
        i += 1
        ax.scatter(float(cluster.get_original_x()), float(cluster.get_original_y()), float(cluster.get_original_z()),
                   c=color, marker='o')
        for data in cluster.get_list():
            x = float(data.get_x())
            y = float(data.get_y())
            z = float(data.get_z())
            ax.scatter(x, y, z, c=color, marker='o')

        ax.scatter(float(cluster.get_x()), float(cluster.get_y()), float(cluster.get_z()),
                   c='black', marker='o')

    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_zlabel(labels[2])

    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    black_patch = mpatches.Patch(color='black', label='Cluster Center')

    plt.legend(handles=[red_patch, green_patch, blue_patch, black_patch])

    plt.show()


def _newPlot2DGraph(data_set, labels):
    x = []
    y = []
    c = []

    for data in data_set:
        x.append(float(data.get_x()))
        y.append(float(data.get_y()))

        data_class = data.get_class()
        if 'Iris-setosa' in data_class:
            c.append('r')
        elif 'Iris-versicolor' in data_class:
            c.append('g')
        elif 'Iris-virginica' in data_class:
            c.append('b')

    plt.scatter(x, y, 3, c)

    plt.xlabel(labels[0])
    plt.ylabel(labels[1])

    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    plt.legend(handles=[red_patch, green_patch, blue_patch])

    plt.show()


def _plot2DClustering(clusters, labels):
    x = []
    y = []
    c = []

    for i in range(3):
        x.append(float(clusters[i].get_original_x()))
        y.append(float(clusters[i].get_original_y()))
        if i == 0:
            c.append('r')
        elif i == 1:
            c.append('g')
        elif i == 2:
            c.append('b')

        for data in clusters[i].get_list():
            x.append(float(data.get_x()))
            y.append(float(data.get_y()))
            if i == 0:
                c.append('r')
            elif i == 1:
                c.append('g')
            elif i == 2:
                c.append('b')

    plt.scatter(x, y, 3, c)
    plt.xlabel(labels[0])
    plt.ylabel(labels[1])

    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    plt.legend(handles=[red_patch, green_patch, blue_patch])

    plt.show()


def _newPlot1DGraph(data_set, labels):
    x = []
    y = []
    c = []

    for data in data_set:
        x.append(float(data.get_x()))
        y.append(0)

        data_class = data.get_class()
        if 'Iris-setosa' in data_class:
            c.append('r')
        elif 'Iris-versicolor' in data_class:
            c.append('g')
        elif 'Iris-virginica' in data_class:
            c.append('b')

    plt.scatter(x, y, 3, c)

    plt.xlabel(labels[0])

    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    plt.legend(handles=[red_patch, green_patch, blue_patch])

    plt.show()


def _plot1DClustering(clusters, labels):
    x = []
    y = []
    c = []

    for i in range(3):
        x.append(float(clusters[i].get_original_x()))
        y.append(0)

        if i == 0:
            c.append('r')
        elif i == 1:
            c.append('g')
        elif i == 2:
            c.append('b')

        for data in clusters[i].get_list():
            x.append(float(data.get_x()))
            y.append(0)
            if i == 0:
                c.append('r')
            elif i == 1:
                c.append('g')
            elif i == 2:
                c.append('b')

    plt.scatter(x, y, 3, c)
    plt.xlabel(labels[0])

    red_patch = mpatches.Patch(color='red', label='Iris-setosa')
    green_patch = mpatches.Patch(color='green', label='Iris-versicolor')
    blue_patch = mpatches.Patch(color='blue', label='Iris-virginica')
    plt.legend(handles=[red_patch, green_patch, blue_patch])

    plt.show()
