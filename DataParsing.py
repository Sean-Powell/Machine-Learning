class DataObject:
    Data = []
    data_length = 0
    data_class = 0

    def __init__(self, data, dataclass):
        self.Data = data
        self.data_class = dataclass.rstrip()

    def setsize(self, size):
        self.data_length = size

    def get_class(self):
        return self.data_class

    def get_x(self):
        return self.Data[0]

    def get_y(self):
        return self.Data[1]

    def get_z(self):
        return self.Data[2]

    def get_size(self):
        return self.data_length


def parseData(lines, user_input):
    data_set = []
    for current_line in lines:
        selected_data = []
        appended_amount = 0
        split_line = current_line.split(",")

        for current_input in user_input:
            selected_data.append(split_line[current_input])

        while len(selected_data) < 3:
            selected_data.append(0)
            appended_amount += 1

        new_object = DataObject(selected_data, split_line[4])
        size = len(selected_data) - appended_amount
        new_object.setsize(size)
        data_set.append(new_object)
    return data_set


def convetToNumber(string):
    return int(string)

