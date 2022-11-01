from domain.apartment import get_expense_dict, get_apartment_number, expense_already_exists, set_expense_value


def add_apartment_to_list(apartment_list, apartment):
    """
        Tries to add the entity apartment to the apartment_list
    :param apartment_list: list
    :param apartment: apartment
    :return: - (if the apartment was added successfully)
    :raises ValueError: - if the apartment already exists in apartment_list, but at least one expense
                          that we want to add already exists for that apartment
                        - the string that will append to the ValueError will be:
                            "Una dintre cheltuieli deja exista!"
    """
    for _apartment in apartment_list:
        if get_apartment_number(_apartment) == get_apartment_number(apartment):
            for expense_apartment in get_expense_dict(apartment).keys():
                if expense_already_exists(_apartment, expense_apartment):
                    raise ValueError("Una dintre cheltuieli deja exista!")
    apartment_list.append(apartment)


def modify_apartment_expense(apartment_list, apartment_number, expense, value):
    """
        Tries to modify the expense of entity apartment with apartment_number in apartment_list by the strictly positive
        float value
    :param apartment_list: list
    :param apartment_number: int
    :param expense: string
    :param value: float > 0.0
    :return: - ( just modifies the apartment in apartment_list with the modified expense)
    :raises ValueError: - if the expense doesn't exist in the apartment's expense list
                        - the associated string is "Cheltuiala nu este asociata acestui apartament!"
    """
    for apartment in apartment_list:
        if apartment_number == get_apartment_number(apartment):
            if expense in get_expense_dict(apartment):
                set_expense_value(apartment, expense, get_expense_dict(apartment)[expense] + value)
                value = -1.0
                break
    if value > -1.0:
        raise ValueError("Cheltuiala nu este asociata acestui apartament!")


def delete_all_expenses(apartment_list, apartment_number):
    """
        Deletes the entire expense list of the entity apartment defined by apartment_number
    :param apartment_list: list
    :param apartment_number: int
    :return: - ( just modifies the expense list of the entity apartment defined by apartment_list)
    :raises ValueError: - if the expense list is already clear
                        - the associated string is: "Lista de cheltuieli este deja goala!"
    """
    for apartment in apartment_list:
        if apartment_number == get_apartment_number(apartment):
            if len(get_expense_dict(apartment)) == 0:
                raise ValueError("Lista de cheltuieli este deja goala!")
            else:
                get_expense_dict(apartment).clear()
                return


def delete_all_expenses_for_consecutive_apartments(apartment_list, start_index, stop_index):
    """
    Deletes the expenses for the apartments in apartments list which are in range [start_index, stop_index]
    :param apartment_list: list
    :param start_index: integer > 0
    :param stop_index: integer > 0
    :return: - (just modifies the apartment_list by deleting all the expenses for the apartments in [start_index, stop_index]
    :raises ValueError: - if the expense list of every apartment in [start_index, stop_index] is already clear
                        - the associated string is: "Listele de cheltuieli ale acestor apartamente sunt deja goale!"
    """
    number_of_clear_expense_lists = 0
    for apartment in apartment_list:
        if start_index <= apartment_list.index(apartment) <= stop_index:
            if len(get_expense_dict(apartment)) > 0:
                get_expense_dict(apartment).clear()
                number_of_clear_expense_lists += 1
    if number_of_clear_expense_lists == 0:
        raise ValueError("Listele de cheltuieli ale acestor apartamente sunt deja goale!")


def apartment_list_by_sum(apartment_list, sum_searched):
    """
        Returns a list of apartments based on apartment_list,
        which have the total expense sum greater than the float sum_searched.
    :param apartment_list: list
    :param sum_searched: float
    :return: list of apartments based on apartment_list,
             which have the total expense sum greater than the float sum_searched, which is >= 0.0
    :raises ValueError: - if in apartment_list doesn't exist at least on entity of type apartment which has the
                        total expense sum greater than the float sum.
                        - the associated message will be the string:
                         "Nu a fost gasit niciun apartament cu aceasta proprietate!"
    """
    apartment_list_greater_than_sum = []
    for apartment in apartment_list:
        if sum(get_expense_dict(apartment).values()) > sum_searched:
            apartment_list_greater_than_sum.append(apartment)
    if len(apartment_list_greater_than_sum) == 0:
        raise ValueError("Nu a fost gasit niciun apartament cu aceasta proprietate!")
    return apartment_list_greater_than_sum


def total_sum_expense(apartment_list, expense):
    """
    Returns the total sum of the expense which resides in the apartments of apartment_list
    :param apartment_list: list
    :param expense: string
    :return: the total sum of type float for the expense which resides in the apartments of apartment_list
    :raises ValueError: - if the total sum is equal to 0.0, which means that the expense doesn't exist in any of the
                          apartments of apartment_list
                        - the associated string is: "Nu s-a putut calcula suma, deoarece cheltuiala nu este asociata
                                                     niciunui apartament!"
    """
    total_sum = 0.0
    for apartment in apartment_list:
        expense_dict = get_expense_dict(apartment)
        if expense in expense_dict.keys():
            total_sum += expense_dict[expense]
    if total_sum == 0.0:
        raise ValueError("Nu s-a putut calcula suma, deoarece cheltuiala nu este asociata niciunui apartament!")
    return total_sum


def sorted_apartment_by_expense_value(apartment_list, expense):
    """
    Returns a new apartment list sorted by the values of expense
    :param apartment_list: list
    :param expense: string
    :return: new_apartment_list - list of apartments sorted by the passed expense
    :raises ValueError: - if the new_apartment_list is the same as the apartment_list
                        - the associated string is: "Cheltuiala nu este asociata niciunui apartament!"
    """
    new_apartment_list = []
    for apartment in apartment_list:
        if expense in get_expense_dict(apartment):
            new_apartment_list.append(apartment)
    for i in range(0, len(new_apartment_list) - 1):
        expense_dict_i = get_expense_dict(new_apartment_list[i])
        for j in range(i + 1, len(new_apartment_list)):
            expense_dict_j = get_expense_dict(new_apartment_list[j])
            if expense_dict_i[expense] > expense_dict_j[expense]:
                temp = new_apartment_list[i]
                new_apartment_list[i] = new_apartment_list[j]
                new_apartment_list[j] = temp
    for apartment in apartment_list:
        if expense not in get_expense_dict(apartment):
            new_apartment_list.append(apartment)
    if new_apartment_list == apartment_list:
        raise ValueError("Cheltuiala nu este asociata niciunui apartament!")
    return new_apartment_list


def total_expense_for_apartment(apartment_list, apartment_number):
    """
    Returns the total sum of the expenses of an apartment in apartment_list based on apartment_number

    :param apartment_list: list
    :param apartment_number: int
    :return: the total sum of the expenses for the apartment in apartment_list based on apartment_number
    :raises ValueError: - if the apartment with apartment_number is not in apartment_list
                        - the associated string is "Apartamentul nu exista!"
    """
    total_sum = 0.0
    for apartment in apartment_list:
        if get_apartment_number(apartment) == apartment_number:
            for expense_value in get_expense_dict(apartment).values():
                total_sum += expense_value
    if total_sum == 0.0:
        raise ValueError("Apartamentul nu exista!")
    return total_sum


def filter_expense_by_sum(apartment_list, value):
    """
    Modifies the entities of type apartment in apartment_list by removing their expenses which have
    the value smaller than the float value

    :param apartment_list: list
    :param value: float
    :return: new list that represents the filtered apartment_list
    :raises ValueError: - if the apartment_list wasn't modified
                        - the associated string is ("Valoarea este prea mica!")
    """
    new_apartment_list = []
    for apartment in apartment_list:
        new_expense_dict = {k: v for k, v in get_expense_dict(apartment).items() if v >= value}
        new_apartment_list.append({get_apartment_number(apartment): new_expense_dict})
    if new_apartment_list == apartment_list:
        raise ValueError("Valoarea este prea mica!")
    return new_apartment_list


def filter_expense_by_type(apartment_list, expense):
    """
    Removes the passed expense from all the apartments from apartment_list that have it.
    :param apartment_list: list
    :param expense: string
    :return: new list that represents the filtered apartment_list
    :raises ValueError: - if the apartment_list wasn't modified
                        - the associated string is ("Cheltuiala nu a fost gasita!")
    """
    new_apartment_list = []
    for apartment in apartment_list:
        new_expense_dict = {k: v for k, v in get_expense_dict(apartment).items() if k != expense}
        new_apartment_list.append({get_apartment_number(apartment): new_expense_dict})
    if apartment_list == new_apartment_list:
        raise ValueError("Cheltuiala nu a fost gasita!")
    return new_apartment_list
