from termcolor import colored
from domain.apartment import get_apartment_number, get_expense_dict
from service.service_apartment import add_apartment_to_list_service, apartment_list_by_sum_service, \
    total_sum_expense_service, \
    total_expense_for_apartment_service, filter_expenses_by_sum_service, filter_expense_by_type_service, \
    modify_apartment_expense_service, sorted_apartment_by_expense_value_service, delete_all_expenses_service, \
    delete_all_expenses_for_consecutive_apartments_service


def print_menu():
    print("1. Adaugare")
    print("2. Stergere")
    print("3. Cautare")
    print("4. Rapoarte")
    print("5. Filtru")
    print("6. Undo")
    print("'exit' pentru iesire")


def print_sub_menu_option(option):
    if option == '1':
        print("1. Adaugare cheltuieli apartament")
        print("2. Modificare cheltuiala apartament")
        print("Cheltuieli permise: 'gaz', 'apa', 'curent', 'salubrizare', 'TV', 'internet', 'chirie'")
    elif option == '2':
        print("1. Sterge toate cheltuielile unui apartament")
        print("2. Sterge cheltuieli pentru apartamente consecutive")
    elif option == '3':
        print("1. Cauta si tipareste toate apartamentele care au cheltuieli mai mari decat o suma impusa")
    elif option == '4':
        print("1. Tipareste suma totala pentru un tip de cheltuiala")
        print("2. Tipareste toate apartamentele sortate dupa un tip de cheltuiala")
        print("3. Tipareste totalul cheltuielilor pentru un apartament dat")
        print("Cheltuieli permise: 'gaz', 'apa', 'curent', 'salubrizare', 'TV', 'internet', 'chirie'")
    elif option == '5':
        print("1. Elimina toate cheltuielile de un anumit tip")
        print("2. Elimina toate cheltuielile mai mici decat o suma data")
    print("'exit' pentru reintoarcere la meniul principal")


def do_action(apartment_list, permitted_expenses, option_main, option_second):
    if option_main == '1':
        if option_second == '1':
            apartment_number = int(input("Numarul apartamentului: "))
            expense_dict = {}
            while True:
                expense_name = input("Cheltuiala sau 'stop' pentru a opri citirea: ")
                if expense_name == 'stop':
                    print(colored("Citirea s-a sfarsit!", 'green'))
                    break
                elif expense_name in expense_dict.keys():
                    print(colored("Cheltuiala a fost deja asociata acestui apartament. Se face adaugarea!", 'yellow'))
                    break
                expense_value = float(input("Valoarea cheltuielli: "))
                expense_dict.update({expense_name: expense_value})
            try:
                add_apartment_to_list_service(apartment_list, apartment_number, expense_dict, permitted_expenses)
                print("Lista de apartamente: ")
                for apartment in apartment_list:
                    print(f"Numar apartament: {get_apartment_number(apartment)}. "
                          f"Lista de cheltuieli: {get_expense_dict(apartment)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
        elif option_second == '2':
            apartment_number = int(input("Numarul apartamentului: "))
            expense = input("Cheltuiala pe care doriti sa o modificati: ")
            value = float(input("Valoarea cu care doriti sa modificati cheltuiala: "))
            try:
                modify_apartment_expense_service(apartment_list, apartment_number, expense, value, permitted_expenses)
                print("Lista modificata: ")
                for apartment in apartment_list:
                    print(f"Numar apartament: {get_apartment_number(apartment)}. "
                          f"Lista de cheltuieli: {get_expense_dict(apartment)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
    elif option_main == '2':
        if option_second == '1':
            apartment_number = int(input("Numarul apartamentului caruia doriti sa ii stergeti cheltuielile: "))
            try:
                delete_all_expenses_service(apartment_list, apartment_number)
                print("Lista modificata: ")
                for apartment in apartment_list:
                    print(f"Numarul apartamentului: {get_apartment_number(apartment)}. "
                          f"Lista de cheltuieli: {get_expense_dict(apartment)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
        elif option_second == '2':
            if len(apartment_list) > 0:
                print(f"Puteti alege valori intre 0 si {len(apartment_list) - 1}.")
                start_index = int(input("Valoarea de inceput: "))
                stop_index = int(input("Valoarea de sfarsit: "))
                try:
                    delete_all_expenses_for_consecutive_apartments_service(apartment_list, start_index, stop_index)
                    print("Lista modificata: ")
                    for apartment in apartment_list:
                        print(f"Numar apartament: {get_apartment_number(apartment)}. "
                              f"Lista de cheltuieli: {get_expense_dict(apartment)}")
                except ValueError as ve:
                    print(colored(str(ve), 'red'))
            else:
                print("Lista de apartamente este goala!")
    elif option_main == '3':
        if option_second == '1':
            value = float(input("Valoare: "))
            try:
                new_apartment_list = apartment_list_by_sum_service(apartment_list, value)
                print("Lista modificata: ")
                for apartment in new_apartment_list:
                    print(f"Numar apartament: {get_apartment_number(apartment)}. "
                          f"Lista de cheltuieli: {get_expense_dict(apartment)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
    elif option_main == '4':
        if option_second == '1':
            expense = input("Cheltuiala cautata: ")
            try:
                print(f"Suma totala pentru cheltuiala {expense} este "
                      f"{total_sum_expense_service(apartment_list, expense, permitted_expenses)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
        elif option_second == '2':
            expense = input("Cheltuiala dupa care se va sorta: ")
            try:
                new_apartment_list = sorted_apartment_by_expense_value_service(apartment_list, expense, permitted_expenses)
                print("Lista sortata: ")
                for apartment in new_apartment_list:
                    print(f"Numar apartament: {get_apartment_number(apartment)}. "
                          f"Lista de cheltuieli: {get_expense_dict(apartment)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
        elif option_second == '3':
            apartment_number = int(input("Numarul apartamentului: "))
            try:
                print(f"Totalul cheltuielilor pentru apartamentul {apartment_number} = "
                      f"{total_expense_for_apartment_service(apartment_list, apartment_number)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
    elif option_main == '5':
        if option_second == '1':
            expense = input("Cheltuiala cautata: ")
            try:
                new_apartment_list = filter_expense_by_type_service(apartment_list, expense, permitted_expenses)
                print("Lista filtrata: ")
                for apartment in new_apartment_list:
                    print(f"Numar apartament: {get_apartment_number(apartment)}. "
                          f"Lista de cheltuieli: {get_expense_dict(apartment)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))
        elif option_second == '2':
            value = float(input("Valoarea cautata: "))
            try:
                new_apartment_list = filter_expenses_by_sum_service(apartment_list, value)
                print("Lista filtrata: ")
                for apartment in new_apartment_list:
                    print(f"Numar apartament: {get_apartment_number(apartment)}. "
                          f"Lista de cheltuieli: {get_expense_dict(apartment)}")
            except ValueError as ve:
                print(colored(str(ve), 'red'))


def run_ui():
    apartment_list = []
    permitted_expenses = ['gaz', 'apa', 'curent', 'salubrizare', 'TV', 'internet', 'chirie']
    available_options = ['1', '2', '3', '4', '5']
    available_options_list = {'1': ['1', '2'], '2': ['1', '2'], '3': ['1'], '4': ['1', '2', '3'], '5': ['1', '2']}
    while True:
        print_menu()
        option_main = input("Optiunea dumneavoastra?: ")
        if option_main == 'exit':
            print("Bye!")
            return
        if option_main not in available_options:
            print("Optiune invalida!")
            continue
        print_sub_menu_option(option_main)
        option_second = input("Optiunea dumneavoasta?: ")
        if option_second == 'exit':
            continue
        if option_second not in available_options_list[option_main]:
            print("Optiune invalida!")
            continue
        do_action(apartment_list, permitted_expenses, option_main, option_second)
