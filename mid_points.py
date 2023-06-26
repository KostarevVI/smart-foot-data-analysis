import sys
from typing import List

import numpy as np


def read_data(filename):
    data = []
    with open(filename, "r") as f_in:
        for line in f_in:
            x, y, f = line.split(",")
            data.append([int(x), int(y), float(f)])

    return np.array(data)


def write_data(mid_points):
    with open("data.txt", "w") as f_out:
        for point in mid_points:
            f_out.write(f"{point[0]},{point[1]}\n")


def calc_midpoint(x_y_f_left: List[int], x_y_f_right: List[int]) -> List[int]:
    x_l, y_l, f_l = x_y_f_left
    x_r, y_r, f_r = x_y_f_right

    # средняя точка без учёта веса на каждой и ног
    x_cen = (x_l + x_r) / 2
    y_cen = (y_l + y_r) / 2

    # настоящая средняя точка
    x = ((x_l - x_cen) * f_l + (x_r - x_cen) * f_r) / (f_l + f_r) + x_cen
    y = ((y_l - y_cen) * f_l + (y_r - y_cen) * f_r) / (f_l + f_r) + y_cen

    point = [int(x), int(y)]
    return point


if __name__ == '__main__':
    left_data = read_data("data_left.txt")
    right_data = read_data("data_right.txt")

    if len(left_data) != len(right_data):
        print("Point arrays of left and right insoles are not equal")
        sys.exit()

    mid_points = []
    for i in range(len(left_data)):
        mid_point = calc_midpoint(left_data[i], right_data[i])
        mid_points.append(mid_point)

    write_data(mid_points)
