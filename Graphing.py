from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as ply


def drawGraph(amount_of_fields, user_input, data_set, labels):
    if amount_of_fields == 1:
        _plat1DGraph(user_input, data_set, labels)
    elif amount_of_fields == 2:
        _plot2DGraph(user_input, data_set, labels)
    elif amount_of_fields == 3:
        _plot3DGraph(user_input, data_set, labels)
    else:
        print("too many fields selected")


def _plot3DGraph(user_input, data_set, labels):
    fig = ply.figure()
    ax = fig.add_subplot(111, projection='3d')

    for data in data_set:
        if data.Data[4] == 'Iris-setosa\n':
            x = float(data.Data[user_input[0] - 1])
            y = float(data.Data[user_input[1] - 1])
            z = float(data.Data[user_input[2] - 1])
            ax.scatter(x, y, z, c='r', marker='o')
        elif data.Data[4] == 'Iris-versicolor\n':
            x = float(data.Data[user_input[0] - 1])
            y = float(data.Data[user_input[1] - 1])
            z = float(data.Data[user_input[2] - 1])
            ax.scatter(x, y, z, c='g', marker='o')
        elif data.Data[4] == 'Iris-virginica\n':
            x = float(data.Data[user_input[0] - 1])
            y = float(data.Data[user_input[1] - 1])
            z = float(data.Data[user_input[2] - 1])
            ax.scatter(x, y, z, c='b', marker='o')

    ax.set_xlabel(labels[user_input[0] - 1])
    ax.set_ylabel(labels[user_input[1] - 1])
    ax.set_zlabel(labels[user_input[2] - 1])

    ply.show()


def _plot2DGraph(user_input, data_set, labels):
    x = []
    y = []
    c = []

    for data in data_set:
        x.append(float(data.Data[user_input[0] - 1]))
        # y.append(0)
        y.append(float(data.Data[user_input[1] - 1]))
        if 'Iris-setosa' in data.Data[4]:
            c.append('r')
        elif 'Iris-versicolor' in data.Data[4]:
            c.append('g')
        elif 'Iris-virginica' in data.Data[4]:
            c.append('b')

    ply.scatter(x, y, 3, c)
    ply.xlabel(labels[user_input[0] - 1])
    ply.ylabel(labels[user_input[1] - 1])
    ply.show()


def _plat1DGraph(user_input, data_set, labels):
    x = []
    y = []
    c = []

    for data in data_set:
        x.append(float(data.Data[user_input[0] - 1]))
        y.append(0)
        if 'Iris-setosa' in data.Data[4]:
            c.append('r')
        elif 'Iris-versicolor' in data.Data[4]:
            c.append('g')
        elif 'Iris-virginica' in data.Data[4]:
            c.append('b')

    ply.scatter(x, y, 3, c)
    ply.xlabel(labels[user_input[0] - 1])
    ply.show()
