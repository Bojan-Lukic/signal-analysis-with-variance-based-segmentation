import statistics
import random
import numpy as np
from statistics import variance as var


def create_test_signal():
    arr = []
    rint = random.randint(0, 30)
    rint2 = random.randint(0, 30)
    if rint > rint2:
        temp = rint
        rint = rint2
        rint2 = temp
    arr = arr + [random.randint(rint, rint2) for _ in range(20)]
    for i in range(0, 2):
        rint = random.randint(50, 60)
        rint2 = random.randint(50, 60)
        if rint > rint2:
            temp = rint
            rint = rint2
            rint2 = temp
        arr = arr + [random.randint(rint, rint2) for _ in range(20)]
        rint = random.randint(10, 30)
        rint2 = random.randint(10, 30)
        if rint > rint2:
            temp = rint
            rint = rint2
            rint2 = temp
        arr = arr + [random.randint(rint, rint2) for _ in range(20)]
    arr = arr + [random.randint(rint, rint2)]

    return(arr)