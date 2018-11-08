def readFile(file_name):
    data_file = open(file_name, "r")
    lines = []
    temp_line = data_file.readline()
    while temp_line:
        lines.append(temp_line)
        temp_line = data_file.readline()
    return lines
    return lines