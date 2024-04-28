import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

def performanceTime(start_time, end_time) -> float:
    return end_time - start_time

# **kwargs and *args
def drawAttributes(*attributeToDraw, **attributes) -> None:
    for drawable_attributes in attributeToDraw:
        for attribute in attributes.keys():
            if attribute == drawable_attributes:
                print(attribute + ": " + attributes.get(attribute))


drawAttributes(
    "color", "display", "font_size",
    background_color="red",
    color="green",
    font_size="20px",
    display="flex"
)


def perform() -> float:
    start = perf_counter()
    my_dict: dict = {}
    with open("RandomIntegerLists.txt", 'r') as myFile:
        for item in myFile.readlines():
            if my_dict.get(item) is None:
                my_dict.update({item: 1})
            else:
                my_dict.update({item: my_dict.get(item) + 1})

    for item in my_dict.items():
        print(item)
    end = perf_counter()
    return performanceTime(start, end)


# lis1 = []
# lis2 = []
#
# for i in range(100):
#     lis1.append(i + 1)
#     lis2.append(perform())
#
# x = np.array(lis1)
# y = np.array(lis2)
#
# plt.plot(x, y)
# plt.show()


print(__name__())
