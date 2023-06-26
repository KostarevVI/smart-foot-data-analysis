from typing import Tuple

import numpy as np
from matplotlib.patches import Ellipse
from numpy import ndarray
from skimage.measure import EllipseModel
import matplotlib.pyplot as plt


# Толщина и прозрачность линии центра давления на графике
line_thickness = 0.5
line_alpha = 0.5


def read_data() -> ndarray:
    data = []
    with open("data.txt", "r") as f_in:
        for line in f_in:
            x, y = line.split(",")
            data.append([int(x), int(y)])

    return np.array(data)


def calculate_EA(points: ndarray) -> (float, Tuple[float]):
    ell = EllipseModel()
    ell.estimate(points)
    xc, yc, a, b, theta = ell.params
    EA = 2 * np.pi * np.sqrt(a * b)
    return EA, (xc, yc, a, b, theta)


def calculate_RMS_AP(points: ndarray) -> ndarray:
    dy = np.diff(points[:, 1])
    rms_ap = np.sqrt(np.mean(dy ** 2))
    return rms_ap


def calculate_RMS_ML(points: ndarray) -> ndarray:
    dx = np.diff(points[:, 0])
    rms_ml = np.sqrt(np.mean(dx ** 2))
    return rms_ml


def plot_trajectory(points: ndarray):
    fig, ax = plt.subplots()
    ax.set_xlim(-100, 100)
    ax.set_ylim(-100, 100)

    # Строим линии, соединяющие точки с заданной толщиной
    ax.plot(points[:, 0], points[:, 1], 'g-', linewidth=line_thickness, alpha=line_alpha)

    # Рассчитываем и отображаем аппроксимирующий эллипс
    EA, ell_params = calculate_EA(points)
    (xc, yc, a, b, theta) = ell_params

    ellipse = Ellipse((xc, yc), 2 * a, 2 * b, theta * 180 / np.pi, edgecolor='blue', facecolor='none')
    ax.add_patch(ellipse)

    ax.text(80, -75, f'EA: {EA:.2f}', fontsize=10, ha='right')
    print(f"EA: {EA}")

    # Рассчитываем метрики RMS
    rms_ap = calculate_RMS_AP(points)
    ax.text(80, -85, f'RMS A/P: {rms_ap:.2f}', fontsize=10, ha='right')
    print(f"RMS A/P: {rms_ap}")

    rms_ml = calculate_RMS_ML(points)
    ax.text(80, -95, f'RMS M/L: {rms_ml:.2f}', fontsize=10, ha='right')
    print(f"RMS M/L: {rms_ml}")

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Trajectory')
    ax.grid(True)

    plt.show()


if __name__ == '__main__':
    # Получение входного массива точек (x, y)
    points = read_data()

    # Строим график траектории с аппроксимирующим эллипсом (EA) и выводом показателей RMS
    plot_trajectory(points)
