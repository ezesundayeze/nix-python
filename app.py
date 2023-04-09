import csv
import numpy as np


def read_file(filePath):
    with open(filePath, 'r') as f:
        wines = list(csv.reader(f, delimiter=";"))

    wines = np.array(wines[1:], dtype=np.float64)
    return wines.tolist()


def multiply(a, b):
    """
    Multiplies two numbers and returns the result
    """
    return a * b
