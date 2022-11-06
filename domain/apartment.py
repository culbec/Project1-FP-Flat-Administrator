def create_apartment(apartment_number, expense_dict):
    """
        Returns an entity of type apartment with it's unique integer identification apartment_number
        and with the expenses in expense_dict of type dict

    :param apartment_number: int
    :param expense_dict: dict
    :return: entity of type apartment with apartment_number integer as identification method and
             expense_dict as dictionary of expenses
    """
    return {apartment_number: expense_dict}


def get_apartment_number(apartment):
    """
        Returns the apartment_number of entity apartment
    :param apartment: apartment
    :return: apartment_number of entity apartment
    """
    return next(iter(apartment.keys()))


def get_expense_dict(apartment):
    """
        Returns the expense_dict of entity apartment
    :param apartment: apartment
    :return: expense_list of entity apartment
    """
    return next(iter(apartment.values()))


def set_expense_dict(apartment, expense_dict):
    """
    Sets the expense list of apartment to expense_dict
    :param apartment: apartment
    :param expense_dict: expense_dict
    :return: -
    """
    apartment_number = get_apartment_number(apartment)
    apartment[apartment_number] = expense_dict


def set_expense_value(apartment, expense, value):
    """
        Sets the value of the expense in the expense_dict of apartment to float value
    :param apartment: apartment
    :param expense: string
    :param value: float
    :return: - (just modifies the expense in the expense_dict of apartment to float value)
    :raises ValueError: - if the expense doesn't exist in the expense_dict of the apartment
                        - the associated string is "Cheltuiala nu este asociata acestui apartament!"
    """
    if expense not in get_expense_dict(apartment):
        raise ValueError("Cheltuiala nu este asociata acestui apartament!")
    get_expense_dict(apartment)[expense] = value


def expense_already_exists(apartment, expense):
    """
        Returns True if the expense already exists in the expense_dict of entity apartment
        False if it doesn't
    :param apartment: apartment
    :param expense: str
    :return: boolean: True if the expense already exists in the expense_dict of entity apartment
                      False if it doesn't
    """
    return expense in get_expense_dict(apartment).keys()
