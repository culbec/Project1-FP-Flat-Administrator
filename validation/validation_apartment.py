from domain.apartment import get_apartment_number, get_expense_dict


def apartment_validation(apartment, permitted_expenses):
    """
        Validates the entity of type apartment:
        apartment_number: integer > 0
        expense_dict: dictionary of expenses which are in permitted_expenses list

    :param apartment: apartment
    :param permitted_expenses: list
    :return: - (if the apartment is a valid one)
    :raises: ValueError - if the apartment_number is not an integer > 0 with the string "Numar de apartament invalid!"
                        - if the expenses in the expense_dict are not in the permitted_expenses
                          with the string "Tipul de cheltuiala nu este permis!"
    """
    errors = ""
    if get_apartment_number(apartment) <= 0:
        errors += "Numar de apartament invalid! "
    expense_dict = get_expense_dict(apartment)
    for value in expense_dict.keys():
        if value not in permitted_expenses:
            errors += "Tipul de cheltuiala nu este permis! "
            break
    errors.strip()
    if len(errors) > 0:
        raise ValueError(errors)


def sum_validation(sum_searched):
    """
    Verifies if the float sum_searched is a positive float number

    :param sum_searched: float
    :return: - (if the sum_searched is a positive float number)
    :raises ValueError: - if the sum_searched is not a positive float number
                        - the associated string message is: "Suma invalida!"
    """
    if sum_searched < 0.0:
        raise ValueError("Suma invalida!")


def expense_validation(expense, permitted_expenses):
    """
    Checks if the passed expense is in permitted_expenses
    :param expense: string
    :param permitted_expenses: list
    :return: - (if the expense in in permitted_expenses)
    :raises ValueError: - if the expense is not in permitted_expenses
                        - the associated string is: "Tipul de cheltuiala nu este permis!"
    """
    if expense not in permitted_expenses:
        raise ValueError("Tipul de cheltuiala nu este permis!")


def apartment_number_validation(apartment_number):
    """
    Checks if the apartment_number is a strictly positive integer.

    :param apartment_number: int
    :return: - (if apartment_number is a strictly positive integer)
    :raises ValueError: - if the apartment_number is not a strictly positive integer
                        - the associated string is: "Numar de apartament invalid!"
    """
    if apartment_number <= 0:
        raise ValueError("Numar de apartament invalid!")


def value_validation(value):
    """
    Checks if value is a strictly positive float number
    :param value: float
    :return: - (if value is a strictly positive float number)
    :raises ValueError: - if value is not a strictly positive float number
                        - the associated string is: "Valoare invalida!"
    """
    if value <= 0.0:
        raise ValueError("Valoare invalida!")


def apartment_in_apartment_list(apartment_list, apartment_number):
    """
        Checks if the apartment defined by apartment_number is in apartment_list
    :param apartment_list: list
    :param apartment_number: integer
    :return: - (if the apartment defined by apartment_number is in apartment_list)
    :raises ValueError: - if the apartment defined by the apartment_number doesn't exist in apartment_list
                        - the associated string is: "Apartamentul nu exista!"
    """
    for apartment in apartment_list:
        if apartment_number == get_apartment_number(apartment):
            return
    raise ValueError("Apartamentul nu exista!")


def expense_in_apartment_expenses(apartment_list, apartment_number, expense):
    """
        Checks if the apartment defined by apartment_number contains the expense.
    :param apartment_list: apartment
    :param apartment_number: int
    :param expense: string
    :return: - (if the expense exists in expense_dict of the apartment defined by apartment_number)
    :raises ValueError: - if the expense doesn't exist in expense_dict of apartment
                        - the associated string is "Cheltuiala nu este asociata acestui apartament!"
    """
    for apartment in apartment_list:
        if apartment_number == get_apartment_number(apartment):
            if expense in get_expense_dict(apartment):
                return
    raise ValueError("Cheltuiala nu este asociata acestui apartament!")


def positive_integer(value):
    """
    Checks if the value is a positive integer
    :param value: integer
    :return: -(if the value is a positive integer)
    :raises ValueError: - if the value is not a positive integer
                        - the associated string is: "Valoare invalida!"
    """
    if value < 0:
        raise ValueError("Valoare invalida!")


def lower_than_list_length_minus_one(apartment_list, value):
    """
    Checks if the value is lower than the length of the apartment_list
    :param value: integer
    :param apartment_list: list
    :return: - (if the value is lower than the length of the list)
    :raises ValueError: - if the value is not lower than the length of the list
                        - the associated string is: "Valoarea nu este mai mica decat limita impusa!"
    """
    if value > len(apartment_list) - 1:
        raise ValueError("Valoarea nu este mai mica decat limita impusa!")


def lower_than_or_equal_indexes(start_index, stop_index):
    """
    Checks if start_index is lower than or equal to stop_index
    :param start_index: integer
    :param stop_index: integer
    :return: - (if start_index <= stop_index)
    :raises ValueError: - if start_index > stop_index
                        - the associated string is: "Valoarea de inceput nu poate fi mai mare decat cea de final!"
    """
    if start_index > stop_index:
        raise ValueError("Valoarea de inceput nu poate fi mai mare decat cea de final!")
