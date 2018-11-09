class DataObject:
    Data = []
    data_size = 0

    def __init__(self, data):
        self.Data = data

    def setsize(self, size):
        self.data_size = size

def parseData(lines):
    data_set = []
    for current_line in lines:
        split_line = current_line.split(",")
        new_object = DataObject(split_line)
        new_object.setsize(len(split_line))
        data_set.append(new_object)
    return data_set


def convetToNumber(string):
    return int(string)

