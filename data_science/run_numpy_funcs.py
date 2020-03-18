import numpy as np
import importlib

numpy_funcs = importlib.import_module("numpy_funcs")


def run_mean_time_for_paid_students():
    # Time spent in the classroom in the first week for 20 students
    time_spent = np.array([
        12.89697233, 0., 64.55043217, 0.,
        24.2315615, 39.991625, 0., 0.,
        147.20683783, 0., 0., 0.,
        45.18261617, 157.60454283, 133.2434615, 52.85000767,
        0., 54.9204785, 26.78142417, 0.
    ])

    # Days to cancel for 20 students
    days_to_cancel = np.array([
        4, 5, 37, 3, 12, 4, 35, 38, 5, 37, 3, 3, 68,
        38, 98, 2, 249, 2, 127, 35
    ])

    print(numpy_funcs.mean_time_for_paid_students(time_spent, days_to_cancel))


def main():
    run_mean_time_for_paid_students()


main()