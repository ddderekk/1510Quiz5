def calculate_pay(hours, wage):
    """
    Calculate weekly pay.

    :param hours: a real number
    :param wage: a positive real number
    :precondition: hours must be a real number
    :precondition: wage must be a real number
    :postcondition: calculates total weekly pay
    :return: return weekly pay as a float
    >>> calculate_pay(10, 10)
    100
    >>> calculate_pay(50, 10)
    600
    """
    if hours <= 0 or wage <= 0:
        return 0

    overtime_hours = 0
    if hours > 40:
        overtime_hours = hours - 40

    base_pay = (hours - overtime_hours) * wage
    over_time_pay = overtime_hours * 2 * wage

    total_pay = float(base_pay + over_time_pay)
    return total_pay


def main():
    """
    Drive the program.
    """


if __name__ == "__main__":
    main()