import ReadFile
import DataParsing

def _drawGraph(amount_of_fields):
    if amount_of_fields <= 2:
       print("2D graph")
    elif amount_of_fields == 3:
        print("3D graph")
    else:
        print("too many fields selected")


def _askUser(length):
    print("Please input what fields you would like to use")
    print("you can enter up to 3 with there being ", (length - 1), " fields from 1 -", (length - 1))
    print("The fields being 1. Sepal Length, 2. Sepal Width, 3. Petal Length, 4. Petal Width")
    user_in = input("Please separate your inputs of the fields you want via a space\n")
    split_user = user_in.split(" ")
    return split_user


def _run():
    data_set = DataParsing.parseData(ReadFile.readFile("irisData.txt"))
    user_input = _askUser(data_set[0].data_size)
    amount_of_fields = len(user_input)
    _drawGraph(amount_of_fields)
    for input in user_input:
        print(input)


_run()
