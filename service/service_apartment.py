from domain.apartment import create_apartment
from repository.repository_apartment import add_apartment_to_list, apartment_list_by_sum, total_sum_expense, \
    total_expense_for_apartment, filter_expense_by_sum, filter_expense_by_type, modify_apartment_expense, \
    delete_all_expenses, sorted_apartment_by_expense_value, delete_all_expenses_for_consecutive_apartments
from validation.validation_apartment import apartment_validation, sum_validation, expense_validation, \
    apartment_number_validation, \
    value_validation, apartment_in_apartment_list, expense_in_apartment_expenses, lower_than_list_length_minus_one, \
    positive_integer, lower_than_or_equal_indexes


def add_apartment_to_list_service(apartment_list, apartment_number, expense_dict, permitted_expenses):
    """
    Based on apartment_number and expense_dict, this will try to create and validate the new apartment,
    then append the new created apartment with the apartment_number and expense_dict.

    :param apartment_list: list
    :param apartment_number: int
    :param expense_dict: dict
    :param permitted_expenses: list
    :return: - (if the apartment was added successfully)
    :raises ValueError: - if the apartment_number is not an integer > 0 with the string "Numar de apartament invalid!"
                       - if the expenses in the expense_dict are not in the permitted_expenses
                          with the string "Tipul de cheltuiala nu este permis!"
                        - if the apartment exists and already has that type of expense added
                          with the string "Acest tip de cheltuiala deja exista!"
    """
    apartment = create_apartment(apartment_number, expense_dict)
    apartment_validation(apartment, permitted_expenses)
    add_apartment_to_list(apartment_list, apartment)


def delete_all_expenses_service(apartment_list, apartment_number):
    """
        Deletes all the expenses of the entity apartment defined by apartment_number
    :param apartment_list: list
    :param apartment_number: int
    :return: - (just modifies the expense list of the entity apartment defined by apartment_number)
    :raises ValueError: - if the apartment is not in the apartment_list
                        - the associated string is: "Apartamentul nu exista!"
                        - if the expense list is already clear
                        - the associated string is: "Lista de cheltuieli este deja goala!"
    """
    apartment_in_apartment_list(apartment_list, apartment_number)
    delete_all_expenses(apartment_list, apartment_number)


def delete_all_expenses_for_consecutive_apartments_service(apartment_list, start_index, stop_index):
    """
    Deletes the expenses for the apartments in apartments list which are in range [start_index, stop_index]
    :param apartment_list: list
    :param start_index: integer
    :param stop_index: integer
    :return: - (just modifies the apartment_list by deleting all the expenses for the apartments in [start_index, stop_index]
    :raises ValueError: - if start_index or stop_index < 0
                        - the associated string is: "Valoare invalida!"
                        - if start_index or stop_index > len(apartment_list)
                        - the associated string is: "Valoarea nu este mai mica decat limita impusa!"
                        - if start_index > stop_index
                        - the associated string is: "Valoarea de inceput nu poate fi mai mare decat cea de final!"
                        - if the expense list of every apartment in [start_index, stop_index] is already clear
                        - the associated string is: "Listele de cheltuieli ale acestor apartamente sunt deja goale!"
    """
    positive_integer(start_index)
    lower_than_list_length_minus_one(apartment_list, start_index)
    positive_integer(stop_index)
    lower_than_list_length_minus_one(apartment_list, stop_index)
    lower_than_or_equal_indexes(start_index, stop_index)
    delete_all_expenses_for_consecutive_apartments(apartment_list, start_index, stop_index)


def apartment_list_by_sum_service(apartment_list, sum_searched):
    """
    Returns a list based on apartment_list of entities of type apartment which have
    their expense sum greater than the float sum_searched

    :param apartment_list: list
    :param sum_searched: float
    :return: list of apartments which have their expense sum greater than sum_searched
    :raises ValueError: - if in apartment_list doesn't exist at least on entity of type apartment which has the
                        total expense sum greater than the float sum.
                        - the associated message will be the string:
                        "Nu a fost gasit niciun apartament cu aceasta proprietate!"
    """
    sum_validation(sum_searched)
    return apartment_list_by_sum(apartment_list, sum_searched)


def modify_apartment_expense_service(apartment_list, apartment_number, expense, value, permitted_expenses):
    """
        Tries to modify the expense of entity apartment with apartment_number in apartment_list by the strictly positive
        float value
    :param apartment_list: list
    :param apartment_number: integer
    :param expense: string
    :param value: float > 0.0
    :param permitted_expenses: list
    :return: - (just modifies the expense of entity apartment by value)
    :raises ValueError: - if the value is not a strictly positive float number
                        - the associated string is "Valoare invalida!"
                        - if the apartment defined by apartment_number doesn't exist in apartment_list
                        - the associated string is "Apartamentul nu exista!"
                        - if the expense is not in permitted expenses
                        - the associated string is "Tipul de cheltuiala nu este permis!"
                        - if the expense doesn't exist in the expense_dict of the apartment
                        - the associated string is "Cheltuiala nu este asociata acestui apartament!"
    """
    value_validation(value)
    apartment_in_apartment_list(apartment_list, apartment_number)
    expense_validation(expense, permitted_expenses)
    expense_in_apartment_expenses(apartment_list, apartment_number, expense)
    modify_apartment_expense(apartment_list, apartment_number, expense, value)


def total_sum_expense_service(apartment_list, expense, permitted_expenses):
    """
    Returns the total sum for the expense which resides in apartments from apartment_list

    :param apartment_list: list
    :param expense: string
    :param permitted_expenses: list
    :return: the total sum for the expense which resides in apartments from apartment_list
    :raises ValueError: - if the total sum is equal to 0.0, which means the expense doesn't exist in any
                          of the apartments of apartment_list
                        - the associated string is: "Nu s-a putut calcula suma, deoarece cheltuiala nu este
                          asociata niciunui apartament!"
                        - if the expense is not in permitted_expenses
                        - the associated string is: "Tipul de cheltuiala nu este permis!"
    """
    expense_validation(expense, permitted_expenses)
    return total_sum_expense(apartment_list, expense)


def total_expense_for_apartment_service(apartment_list, apartment_number):
    """
    Returns the total sum of the expenses of an apartment in apartment_list based on apartment_number

    :param apartment_list: list
    :param apartment_number: int
    :return: the total sum of the expenses for the apartment in apartment_list based on apartment_number
    :raises ValueError: - if the apartment in apartment_number is not in apartment_list
                        - the associated string is "Apartamentul nu exista!"
                        - if the apartment_number is not a strictly positive integer
                        - the associated string is: "Numar apartament invalid!"
    """
    apartment_number_validation(apartment_number)
    return total_expense_for_apartment(apartment_list, apartment_number)


def sorted_apartment_by_expense_value_service(apartment_list, expense, permitted_expenses):
    """
    Returns a new apartment list sorted by the values of expense
    :param apartment_list: list
    :param expense: string
    :param permitted_expenses: list
    :return: new_apartment_list - list of apartments sorted by the passed expense
    :raises ValueError: - if the new_apartment_list is the same as the apartment_list
                        - the associated string is: "Cheltuiala nu este asociata niciunui apartament!"
                        - if the expense is not in permitted_expenses
                        - the associated string is: "Tipul de cheltuiala nu este permis!"
    """
    expense_validation(expense, permitted_expenses)
    return sorted_apartment_by_expense_value(apartment_list, expense)


def filter_expenses_by_sum_service(apartment_list, value):
    """
    Modifies the entities of type apartment in apartment_list by removing their expenses which have
    the value smaller than the float value

    :param apartment_list: list
    :param value: float
    :return: new list that represents the filtered apartment_list
    :raises ValueError: - if value is not a strictly positive float number
                        - the associated string is: "Valoare invalida!"
                        - if the apartment_list wasn't modified
                        - the associated string is ("Valoarea este prea mica!")

    """
    value_validation(value)
    return filter_expense_by_sum(apartment_list, value)


def filter_expense_by_type_service(apartment_list, expense, permitted_expenses):
    """
    Removes the passes expense from all the apartments from apartment_list that have it
    :param apartment_list: list
    :param expense: string
    :param permitted_expenses: list
    :return: new list that represents the filtered apartment_list
    :raises ValueError: - if the apartment_list wasn't modified
                        - the associated string is ("Cheltuiala nu a fost gasita!")
                        - if the expense is not in permitted_expenses
                        - the associated string is: "Tipul de cheltuiala nu este permis!
    """
    expense_validation(expense, permitted_expenses)
    return filter_expense_by_type(apartment_list, expense)

