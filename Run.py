import plotly.plotly as py


class DataObject:
    Data = []
    data_size = 0

    def __init__(self, data):
        self.Data = data

    def setsize(self, size):
        self.data_size = size


def _readFile(file_name):
    data_file = open(file_name, "r")
    lines = []
    temp_line = data_file.readline()
    while temp_line:
        lines.append(temp_line)
        temp_line = data_file.readline()
    return lines


def _parseData(lines):
    data_set = []
    for current_line in lines:
        split_line = current_line.split(",")
        new_object = DataObject(split_line)
        new_object.setsize(len(split_line))
        data_set.append(new_object)
    return data_set


def _askUser(length):
    print("Please input what fields you would like to use")
    print("you can enter up to 3 with there being ", length, " fields from 1 -", length)
    print("The fields being 1. Sepal Length, 2. Sepal Width, 3. Petal Length, 4. Petal Width, 5. Class")
    user_in = input("Please separate your inputs of the fields you want via a space\n")
    split_user = user_in.split(" ")
    return split_user


def _run():
    data_set = _parseData(_readFile("irisData.txt"))
    user_input = _askUser(data_set[0].data_size)
    for input in user_input:
        print(input)


_run()
