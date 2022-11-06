from service.service_apartment import list_copy


def create_apartment_manager():
    """
    Creates an apartment_manager type entity
    :return: list of two elements that contain the current list and the undo list
    """
    current_list = []
    undo_list = []
    return [current_list, undo_list]


def get_current_list(apartment_manager):
    """
    Returns the current list of the entity apartment_manager.
    :param apartment_manager: apartment_manager
    :return: current list of apartment_manager
    """
    return apartment_manager[0]


def get_undo_list(apartment_manager):
    """
    Returns the undo list of the entity apartment_manager.
    :param apartment_manager: apartment_manager
    :return: undo list of apartment_manager
    """
    return apartment_manager[1]


def set_current_list(apartment_manager, new_list):
    """
    Sets the current list of apartment_manager to the passed new_list
    :param apartment_manager: apartment_manager
    :param new_list: list
    :return: -
    """
    apartment_manager[0] = new_list


def set_undo_list(apartment_manager, new_list):
    """
    Sets the undo list of apartment_manager to the passed new_list
    :param apartment_manager: apartment_manager
    :param new_list: list
    :return: -
    """
    apartment_manager[1] = new_list


def update_apartment_manager(apartment_manager, apartment_list):
    """
    Add the apartment to the apartment_manager
    :param apartment_manager: apartment_manager
    :param apartment_list: list
    :return: -
    """
    undo_list = get_undo_list(apartment_manager)
    crt_list = get_current_list(apartment_manager)

    undo_list.append(list_copy(crt_list))
    crt_list.clear()
    crt_list.extend(apartment_list)


def undo_manager(apartment_manager):
    """
    Sets the apartment_manager to it's previous state.
    :param apartment_manager: apartment_manager
    :return: -
    """
    undo_list = get_undo_list(apartment_manager)
    if len(undo_list) == 0:
        raise ValueError("Nu se mai poate face undo!")
    crt_list = undo_list[-1]
    set_current_list(apartment_manager, crt_list)
    set_undo_list(apartment_manager, undo_list[:-1])
