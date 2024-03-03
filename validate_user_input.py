import math
import numpy as np


def validate_linear(m, c, x_start, x_end):
    try:
        m = float(m)
        c = float(c)
        x_start = float(x_start)
        x_end = float(x_end)
        # steps = (x_end - x_start) / 10
        x_values = np.arange(x_start, x_end + 1, 1).round(2).tolist()
        y_values = [round((m * x) + c, 2) for x in x_values]
        return x_values, y_values

    except (TypeError, ValueError):
        return [], []


def validate_quadratic(a, b, c, x_start, x_end):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        x_start = float(x_start)
        x_end = float(x_end)
        steps = (x_end - x_start) / 10
        x_values = np.arange(x_start, x_end + steps, steps).round(2).tolist()
        y_values = [round(a * (x**2) + b * x + c, 2) for x in x_values]
        return x_values, y_values

    except (TypeError, ValueError):
        return [], []


def validate_cubic(a, b, c, d, x_start, x_end):
    try:
        a = float(a)
        b = float(b)
        c = float(c)
        d = float(d)
        x_start = float(x_start)
        x_end = float(x_end)
        steps = (x_end - x_start) / 10
        x_values = np.arange(x_start, x_end + steps, steps).round(2).tolist()
        y_values = [round(a * (x ** 3) + b * (x ** 2) + c * x + d, 2) for x in x_values]
        return x_values, y_values

    except (TypeError, ValueError):
        return [], []
    finally:
        pass


def validate_reciprocal(a, x_start, x_end):
    try:
        a = float(a)
        x_start = math.floor(float(x_start))
        x_end = float(x_end)

        x_values_1 = np.arange(x_start, 0, 1).round(2).tolist()
        y_values_1 = [round(a / x, 2) for x in x_values_1]

        x_values_2 = np.arange(1, x_end, 1).round(2).tolist()
        y_values_2 = [round(a / x, 2) for x in x_values_2]

        return x_values_1, x_values_2, y_values_1, y_values_2

    except (TypeError, ValueError):
        return [], [], [], []
    finally:
        pass


def validate_exponential(a, k, x_start, x_end):
    try:
        a = float(a)
        k = float(k)
        x_start = float(x_start)
        x_end = float(x_end)

        x_values = np.arange(x_start, x_end, 1).round(2).tolist()
        y_values = [round(a * (k ** x), 2) for x in x_values]
        return x_values, y_values

    except (TypeError, ValueError):
        return [], []
