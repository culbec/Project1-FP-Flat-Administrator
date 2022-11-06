from domain.apartment import create_apartment, get_apartment_number, get_expense_dict, set_expense_value, \
    set_expense_dict
from domain.apartment_manager import create_apartment_manager, update_apartment_manager, get_current_list, \
    get_undo_list, undo_manager
from repository.repository_apartment import add_apartment_to_list, apartment_list_by_sum, total_sum_expense, \
    total_expense_for_apartment, filter_expense_by_sum, filter_expense_by_type, modify_apartment_expense, \
    delete_all_expenses, sorted_apartment_by_expense_value, delete_all_expenses_for_consecutive_apartments, \
    search_apartment_expense
from service.service_apartment import add_apartment_to_list_service, apartment_list_by_sum_service, \
    total_sum_expense_service, \
    total_expense_for_apartment_service, filter_expenses_by_sum_service, filter_expense_by_type_service, \
    modify_apartment_expense_service, delete_all_expenses_service, sorted_apartment_by_expense_value_service, \
    delete_all_expenses_for_consecutive_apartments_service, search_apartment_expense_service
from validation.validation_apartment import apartment_validation, sum_validation, expense_validation, \
    apartment_number_validation, \
    value_validation, apartment_in_apartment_list, expense_in_apartment_expenses, positive_integer, \
    lower_than_list_length_minus_one, lower_than_or_equal_indexes


def test_create_apartment():
    apartment_number = 4
    expense_dict = {'gaz': 42.1, 'apa': 51.4, 'curent': 100.43}
    apartment = create_apartment(apartment_number, expense_dict)
    assert apartment_number == get_apartment_number(apartment)
    assert expense_dict == get_expense_dict(apartment)
    # Testing set_expense_dict
    set_expense_dict(apartment, {'apa': 100.5, 'internet': 300.1})
    assert get_expense_dict(apartment) == {'apa': 100.5, 'internet': 300.1}
    # Testing the set_expense_value
    set_expense_value(apartment, 'apa', 100.1)
    assert get_expense_dict(apartment) == {'apa': 100.1, 'internet': 300.1}
    try:
        set_expense_value(apartment, 'TV', 300.1)
        assert False
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata acestui apartament!"


def test_apartment_validation():
    apartment_list = []
    # checks if an  apartment if a valid one
    permitted_expenses = ['gaz', 'apa', 'curent', 'salubrizare', 'TV', 'internet', 'chirie']
    apartment_number = 4
    expense_dict = {'gaz': 42.1, 'apa': 51.4, 'curent': 100.43}
    apartment = create_apartment(apartment_number, expense_dict)
    apartment_validation(apartment, permitted_expenses)
    add_apartment_to_list(apartment_list, apartment)

    other_apartment_number = 0
    other_expense_dict = {'gaz': 500.0, 'gunoi': 67.1}
    other_apartment = create_apartment(other_apartment_number, other_expense_dict)
    try:
        apartment_validation(other_apartment, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Numar de apartament invalid! Tipul de cheltuiala nu este permis! "

    # checks if a sum is a valid one
    sum1 = 23.5
    sum_validation(sum1)
    sum2 = -54.1
    try:
        sum_validation(sum2)
        assert False
    except ValueError as ve:
        assert str(ve) == "Suma invalida!"

    # checks if an expense is a valid one
    expense1 = 'gaz'
    expense_validation(expense1, permitted_expenses)
    expense2 = 'gunoi'
    try:
        expense_validation(expense2, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Tipul de cheltuiala nu este permis!"

    # checks if an apartment number is a valid one
    v_apartment_number1 = 4
    apartment_number_validation(v_apartment_number1)
    v_apartment_number2 = -2
    try:
        apartment_number_validation(v_apartment_number2)
        assert False
    except ValueError as ve:
        assert str(ve) == "Numar de apartament invalid!"

    # checks if a passed value is a strictly positive float number
    value_validation(100.4)
    try:
        value_validation(-394.33)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoare invalida!"

    # checks if the apartment defined by apartment_number exists in apartment_list
    apartment_in_apartment_list(apartment_list, 4)
    try:
        apartment_in_apartment_list(apartment_list, 21)
        assert False
    except ValueError as ve:
        assert str(ve) == "Apartamentul nu exista!"

    # checks if the expense exists in the expense_dict of a apartment
    expense_in_apartment_expenses(apartment_list, 4, 'gaz')
    try:
        expense_in_apartment_expenses(apartment_list, 4, 'TV')
        assert False
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata acestui apartament!"
    # Testing positive_integer
    positive_integer(0)
    try:
        positive_integer(-1)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoare invalida!"
    # Testing lower_than_list_length
    lower_than_list_length_minus_one(apartment_list, 0)
    try:
        lower_than_list_length_minus_one(apartment_list, 200)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoarea nu este mai mica decat limita impusa!"
    # Testing lower_than_or_equal_indexes
    lower_than_or_equal_indexes(0, 3)
    try:
        lower_than_or_equal_indexes(4, 3)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoarea de inceput nu poate fi mai mare decat cea de final!"


def test_repository_apartment():
    # Testing the adding functionality
    apartment_list = []
    assert len(apartment_list) == 0

    apartment_number = 4
    expense_dict = {'gaz': 42.1, 'apa': 51.4, 'curent': 100.43}
    apartment = create_apartment(apartment_number, expense_dict)
    add_apartment_to_list(apartment_list, apartment)
    assert len(apartment_list) == 1

    same_apartment_number = 4
    other_expense_dict = {'TV': 400.1, 'internet': 112.0, 'gaz': 500.1}
    same_apartment_number_other_expense_dict = create_apartment(same_apartment_number, other_expense_dict)
    try:
        add_apartment_to_list(apartment_list, same_apartment_number_other_expense_dict)
        assert False
    except ValueError as ve:
        assert str(ve) == "Una dintre cheltuieli deja exista!"

    # Testing the searching functionality
    apartment_list = []

    apartment_number1 = 4
    expense_dict1 = {'gaz': 42.1, 'apa': 51.4, 'curent': 100.43}
    apartment_number2 = 23
    expense_dict2 = {'TV': 123.25, 'internet': 80.34, 'chirie': 160.27}
    apartment_number3 = 53
    expense_dict3 = {'gaz': 500.4, 'chirie': 200.3, 'curent': 200.1}
    apartment_number4 = 2
    expense_dict4 = {'gaz': 100.2, 'apa': 200.1, 'curent': 200.0}
    apartment1 = create_apartment(apartment_number1, expense_dict1)
    apartment2 = create_apartment(apartment_number2, expense_dict2)
    apartment3 = create_apartment(apartment_number3, expense_dict3)
    apartment4 = create_apartment(apartment_number4, expense_dict4)
    add_apartment_to_list(apartment_list, apartment1)
    add_apartment_to_list(apartment_list, apartment2)
    add_apartment_to_list(apartment_list, apartment3)
    add_apartment_to_list(apartment_list, apartment4)

    sum1 = 150.0
    assert len(apartment_list_by_sum(apartment_list, sum1)) > 0

    sum2 = 350.0
    try:
        assert len(apartment_list_by_sum(apartment_list, sum2)) > 0
    except ValueError as ve:
        assert str(ve) == "Nu a fost gasit nici un apartament cu aceasta proprietate!"
    assert total_sum_expense(apartment_list, 'gaz') == 642.7
    try:
        assert total_sum_expense(apartment_list, 'salubrizare')
    except ValueError as ve:
        assert str(ve) == "Nu s-a putut calcula suma, deoarece cheltuiala nu este asociata niciunui apartament!"
    # Testing total_expense_for_apartment
    assert total_expense_for_apartment(apartment_list, 2) == 500.3
    try:
        assert total_expense_for_apartment(apartment_list, 100)
    except ValueError as ve:
        assert str(ve) == "Apartamentul nu exista!"
    # Testing remove_expenses_apartment
    assert filter_expense_by_sum(apartment_list, 200.0) == [{4: {}},
                                                            {23: {}},
                                                            {53: {'gaz': 500.4, 'chirie': 200.3, 'curent': 200.1}},
                                                            {2: {'apa': 200.1, 'curent': 200.0}}]
    try:
        filter_expense_by_sum(apartment_list, 1.0)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoarea este prea mica!"
    # Testing filter_expense_by_type
    assert filter_expense_by_type(apartment_list, 'gaz') == [{4: {'apa': 51.4, 'curent': 100.43}},
                                                             {23: {'TV': 123.25, 'internet': 80.34, 'chirie': 160.27}},
                                                             {53: {'chirie': 200.3, 'curent': 200.1}},
                                                             {2: {'apa': 200.1, 'curent': 200.0}}]
    try:
        filter_expense_by_type(apartment_list, 'salubrizare')
        assert False
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu a fost gasita!"
    # Testing modify_apartment_expense
    modify_apartment_expense(apartment_list, 4, 'gaz', 24.5)
    try:
        modify_apartment_expense(apartment_list, 23, 'salubrizare', 1.1)
        assert False
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata acestui apartament!"
    # Testing delete_all_expenses
    assert delete_all_expenses(apartment_list, 4) == [{4: {}},
                                                      {23: {'TV': 123.25, 'internet': 80.34, 'chirie': 160.27}},
                                                      {53: {'gaz': 500.4, 'chirie': 200.3, 'curent': 200.1}},
                                                      {2: {'gaz': 100.2, 'apa': 200.1, 'curent': 200.0}}]
    set_expense_dict(apartment1, {})
    try:
        delete_all_expenses(apartment_list, 4)
        assert False
    except ValueError as ve:
        assert str(ve) == "Lista de cheltuieli este deja goala!"
    # Testing sorted_apartment_by_expense_value
    assert sorted_apartment_by_expense_value(apartment_list, 'gaz') == [{2: {'gaz': 100.2, 'apa': 200.1, 'curent': 200.0}},
                                                                        {53: {'gaz': 500.4, 'chirie': 200.3, 'curent': 200.1}},
                                                                        {4: {}},
                                                                        {23: {'TV': 123.25, 'internet': 80.34, 'chirie': 160.27}}]
    try:
        assert sorted_apartment_by_expense_value(apartment_list, 'salubrizare')
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata niciunui apartament!"
    # Testing delete_all_expenses_for_consecutive_apartments
    assert delete_all_expenses_for_consecutive_apartments(apartment_list, 1, 3) == [{4: {}},
                                                                                    {23: {}},
                                                                                    {53: {}},
                                                                                    {2: {}}]
    try:
        assert delete_all_expenses_for_consecutive_apartments(apartment_list, 1, 3)
    except ValueError as ve:
        assert str(ve) == "Listele de cheltuieli ale acestor apartamente sunt deja goale!"
    # Testing search_apartment_expense
    assert search_apartment_expense(apartment_list, 'gaz') == [{53: {'gaz': 500.4, 'chirie': 200.3, 'curent': 200.1}},
                                                               {2: {'gaz': 100.2, 'apa': 200.1, 'curent': 200.0}}]
    try:
        assert search_apartment_expense(apartment_list, 'salubrizare')
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata niciunui apartament!"


def test_service_apartment():
    # Testing add_apartment_to_list_service
    permitted_expenses = ['gaz', 'apa', 'curent', 'salubrizare', 'TV', 'internet', 'chirie']
    apartment_list = []
    assert len(apartment_list) == 0

    apartment_number = 4
    expense_dict = {'gaz': 42.1, 'apa': 51.4, 'curent': 100.43}
    add_apartment_to_list_service(apartment_list, apartment_number, expense_dict, permitted_expenses)
    apartment_number_1 = 23
    expense_dict_1 = {'gaz': 205.6, 'TV': 300.1, 'curent': 210.1}
    assert len(apartment_list) == 1
    add_apartment_to_list_service(apartment_list, apartment_number_1, expense_dict_1, permitted_expenses)

    same_apartment_number = 4
    other_expense_dict = {'TV': 400.1, 'internet': 112.0, 'gaz': 500.1}
    try:
        add_apartment_to_list_service(apartment_list, same_apartment_number, other_expense_dict, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Una dintre cheltuieli deja exista!"
    wrong_apartment_number = -5
    wrong_expense_dict = {'gunoi': 400.1, 'subsol': 300}
    try:
        add_apartment_to_list_service(apartment_list, wrong_apartment_number, wrong_expense_dict, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Numar de apartament invalid! Tipul de cheltuiala nu este permis! "
    other_wrong_apartment_number = -4
    try:
        add_apartment_to_list_service(apartment_list, other_wrong_apartment_number, other_expense_dict, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Numar de apartament invalid! "
    # Testing apartment_list_by_sum_service
    sum1 = 150.0
    assert len(apartment_list_by_sum_service(apartment_list, sum1)) > 0
    sum2 = 350.0
    try:
        assert len(apartment_list_by_sum_service(apartment_list, sum2)) > 0
    except ValueError as ve:
        assert str(ve) == "Nu a fost gasit niciun apartament cu aceasta proprietate!"
    # Testing total_sum_expense_service
    expense1 = 'gaz'
    assert total_sum_expense_service(apartment_list, expense1, permitted_expenses) - 247.7 < 0.0001
    expense2 = 'gunoi'
    try:
        assert total_sum_expense_service(apartment_list, expense2, permitted_expenses)
    except ValueError as ve:
        assert str(ve) == "Tipul de cheltuiala nu este permis!"
    expense3 = 'TV'
    try:
        assert total_sum_expense_service(apartment_list, expense3, permitted_expenses)
    except ValueError as ve:
        assert str(ve) == "Nu s-a putut calcula suma, deoarece cheltuiala nu este asociata niciunui apartament!"
    # Testing total_expense_for_apartment_service
    other_apartment_number = 5
    other_other_expense_dict = {'gaz': 315.2, 'TV': 150.3, 'salubrizare': 200.1, 'internet': 80.2}
    add_apartment_to_list_service(apartment_list, other_apartment_number, other_other_expense_dict, permitted_expenses)
    assert total_expense_for_apartment_service(apartment_list, 4) - 193.93 < 0.0001
    assert total_expense_for_apartment_service(apartment_list, 5) - 745.8 < 0.0001
    try:
        total_expense_for_apartment_service(apartment_list, 2)
        assert False
    except ValueError as ve:
        assert str(ve) == "Apartamentul nu exista!"
    try:
        total_expense_for_apartment_service(apartment_list, -1)
        assert False
    except ValueError as ve:
        assert str(ve) == "Numar de apartament invalid!"
    # Testing filter_expenses_by_sum_service
    assert filter_expenses_by_sum_service(apartment_list, 100.4) == [{4: {'curent': 100.43}},
                                                                     {23: {'gaz': 205.6, 'TV': 300.1, 'curent': 210.1}},
                                                                     {5: {'gaz': 315.2, 'TV': 150.3, 'salubrizare': 200.1, }}]
    try:
        assert filter_expenses_by_sum_service(apartment_list, -1.0)
    except ValueError as ve:
        assert str(ve) == "Valoare invalida!"
    # Testing filter_expense_by_type_service
    assert filter_expense_by_type_service(apartment_list, 'gaz', permitted_expenses) == [{4: {'apa': 51.4, 'curent': 100.43}},
                                                                                         {23: {'TV': 300.1, 'curent': 210.1}},
                                                                                         {5: {'TV': 150.3, 'salubrizare': 200.1, 'internet': 80.2}}]
    try:
        assert filter_expense_by_type_service(apartment_list, 'TV', permitted_expenses)
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu a fost gasita!"
    try:
        assert filter_expense_by_type_service(apartment_list, 'gunoi', permitted_expenses)
    except ValueError as ve:
        assert str(ve) == "Tipul de cheltuiala nu este permis!"
    # Testing modify_expense_apartment_service
    modify_apartment_expense_service(apartment_list, 4, 'gaz', 12.4, permitted_expenses)
    try:
        modify_apartment_expense_service(apartment_list, 4, 'apa', 0.0, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoare invalida!"
    try:
        modify_apartment_expense_service(apartment_list, 6, 'apa', 36.5, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Apartamentul nu exista!"
    try:
        modify_apartment_expense_service(apartment_list, 4, 'gunoi', 96.0, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Tipul de cheltuiala nu este permis!"
    try:
        modify_apartment_expense_service(apartment_list, 4, 'internet', 100.4, permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata acestui apartament!"
    # Testing delete_all_expenses_service
    assert delete_all_expenses_service(apartment_list, 4) == [{4: {}},
                                                              {23: {'gaz': 205.6, 'TV': 300.1, 'curent': 210.1}},
                                                              {5: {'gaz': 315.2, 'TV': 150.3, 'salubrizare': 200.1, 'internet': 80.2}}]
    try:
        delete_all_expenses_service(apartment_list, -4)
        assert False
    except ValueError as ve:
        assert str(ve) == "Apartamentul nu exista!"
    try:
        assert delete_all_expenses_service(apartment_list, 4)
    except ValueError as ve:
        assert str(ve) == "Lista de cheltuieli este deja goala!"
    # Testing sorted_apartment_by_expense_value_service
    assert sorted_apartment_by_expense_value_service(apartment_list, 'gaz', permitted_expenses) == [{4: {'gaz': 54.5, 'apa': 51.4, 'curent': 100.43}},
                                                                                                    {23: {'gaz': 205.6, 'TV': 300.1, 'curent': 210.1}},
                                                                                                    {5: {'gaz': 315.2, 'TV': 150.3, 'salubrizare': 200.1, 'internet': 80.2}}]
    try:
        assert sorted_apartment_by_expense_value_service(apartment_list, 'chirie', permitted_expenses)
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata niciunui apartament!"
    try:
        sorted_apartment_by_expense_value_service(apartment_list, 'gunoi', permitted_expenses)
        assert False
    except ValueError as ve:
        assert str(ve) == "Tipul de cheltuiala nu este permis!"
    # Testing delete_all_expenses_for_consecutive_apartments
    assert delete_all_expenses_for_consecutive_apartments_service(apartment_list, 0, 2) == [{4: {}},
                                                                                            {23: {}},
                                                                                            {5: {}}]
    try:
        assert delete_all_expenses_for_consecutive_apartments_service(apartment_list, 0, 2)
    except ValueError as ve:
        assert str(ve) == "Listele de cheltuieli ale acestor apartamente sunt deja goale!"
    try:
        delete_all_expenses_for_consecutive_apartments_service(apartment_list, -1, 2)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoare invalida!"
    try:
        delete_all_expenses_for_consecutive_apartments_service(apartment_list, 3, 2)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoarea nu este mai mica decat limita impusa!"
    try:
        delete_all_expenses_for_consecutive_apartments_service(apartment_list, 2, 1)
        assert False
    except ValueError as ve:
        assert str(ve) == "Valoarea de inceput nu poate fi mai mare decat cea de final!"
    # Testing search_apartment_expense_service
    assert search_apartment_expense_service(apartment_list, 'gaz', permitted_expenses) == [{4: {'gaz': 54.5, 'apa': 51.4, 'curent': 100.43}},
                                                                                           {23: {'gaz': 205.6, 'TV': 300.1, 'curent': 210.1}},
                                                                                           {5: {'gaz': 315.2, 'TV': 150.3, 'salubrizare': 200.1, 'internet': 80.2}}]
    try:
        assert search_apartment_expense_service(apartment_list, 'TV', permitted_expenses)
    except ValueError as ve:
        assert str(ve) == "Cheltuiala nu este asociata niciunui apartament!"
    try:
        assert search_apartment_expense_service(apartment_list, 'gunoi', permitted_expenses)
    except ValueError as ve:
        assert str(ve) == "Tipul de cheltuiala nu este permis!"


def test_apartment_manager():
    # Testing add_apartment_to_manager
    test_manager = create_apartment_manager()
    apartment_list = []
    permitted_expenses = ['gaz', 'apa', 'salubrizare', 'curent', 'TV', 'internet']
    apartment1 = create_apartment(4, {'gaz': 300.1, 'apa': 500.4, 'curent': 127.3})
    add_apartment_to_list_service(apartment_list, get_apartment_number(apartment1),
                                  get_expense_dict(apartment1), permitted_expenses)
    update_apartment_manager(test_manager, apartment_list)
    assert len(get_current_list(test_manager)) == 1

    apartment2 = create_apartment(5, {'TV': 100.3, 'apa': 200.0})
    add_apartment_to_list_service(apartment_list, get_apartment_number(apartment2),
                                  get_expense_dict(apartment2), permitted_expenses)
    update_apartment_manager(test_manager, apartment_list)
    assert len(get_current_list(test_manager)) == 2 and len(get_undo_list(test_manager)) == 2
    # Testing undo
    undo_manager(test_manager)
    assert len(get_current_list(test_manager)) == 1
    undo_manager(test_manager)
    assert len(get_current_list(test_manager)) == 0
    try:
        undo_manager(test_manager)
        assert False
    except ValueError as ve:
        assert str(ve) == "Nu se mai poate face undo!"


def run_all_tests():
    test_create_apartment()
    # print("Apartment creation test ended successfully!")
    test_apartment_validation()
    # print("Apartment validation test ended successfully!")
    test_repository_apartment()
    # print("Apartment repository test ended successfully!")
    test_service_apartment()
    # print("Apartment service test ended successfully!")
    test_apartment_manager()
