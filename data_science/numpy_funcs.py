import numpy as np


def mean_time_for_paid_students(time_spent, days_to_cancel):
    """
    Fill in this function to calculate the mean time spent in the classroom
    for students who stayed enrolled at least (greater than or equal to) 7 days.
    Unlike in Lesson 1, you can assume that days_to_cancel will contain only
    integers (there are no students who have not canceled yet).

    The arguments are NumPy arrays. time_spent contains the amount of time spent
    in the classroom for each student, and days_to_cancel contains the number
    of days until each student cancel. The data is given in the same order
    in both arrays.
    """

    # looks in time_spent
    # but only the values where cancellation happened starting at 7 days
    # then take the mean of the smaller section of values
    return time_spent[days_to_cancel >= 7].mean()


def std_from_mean():
    employment = np.array([
        55.70000076, 51.40000153, 50.5, 75.69999695,
        58.40000153, 40.09999847, 61.5, 57.09999847,
        60.90000153, 66.59999847, 60.40000153, 68.09999847,
        66.90000153, 53.40000153, 48.59999847, 56.79999924,
        71.59999847, 58.40000153, 70.40000153, 41.20000076
    ])

    mean = employment.mean()
    sd = employment.std()  # 9.338% is one standard deviation from the mean

    print(mean)
    print(sd)

    mean_deviation = employment - mean
    sd_from_mean = mean_deviation / sd

    print(mean_deviation)
    print(sd_from_mean)
