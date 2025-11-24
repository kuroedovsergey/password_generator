import random

################################################
# словарь и числа
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '1234567890'
special_characters = '@#$%^&*!?+-*/}{][()'
result_pass = ''

answer_yes = 'да'
answer_no = 'нет'


def main(*args):
    print(f'''Генератор пароля. Укажите требуемые настройки для создания пароля. ''')
    ask_count_letters = input("Введите количество символов: ")

    if not ask_count_letters.isdigit():
        print("Введите число")
        return

    ask_count_letters = int(ask_count_letters)

    ask_lowercase_letters = input("Строчные буквы (да/нет): ")
    
    if ask_lowercase_letters not in (answer_no, answer_yes):
        print("Введите дa или нет")
        return

    ask_digits = input("Цифры (да/нет): ")
    
    if ask_digits not in (answer_no, answer_yes):
        print("Введите да или нет")
        return

    ask_uppercase_letters = input("Заглавые буквы (да/нет): ")
    
    if ask_uppercase_letters not in (answer_no, answer_yes):
        print("Введите да или нет")
        return

    available_choice_pass(ask_count_letters=ask_count_letters,
                          ask_lowercase_letters=ask_lowercase_letters,
                          ask_digits=ask_digits,
                          ask_uppercase_letters=ask_uppercase_letters)




def available_choice_pass(**answers):
    result_pass = ''
    chararacters_enumerate, count_pass = answer_worker(answers)

    for answer in range(count_pass):

        chararacters_list = list(chararacters_enumerate)
        random.shuffle(chararacters_list)

        result_pass += random.choice(chararacters_list)

    print(result_pass)


def answer_worker(answers):
    chararacters_enumerate = ''
    if answers['ask_lowercase_letters'] == "да" and answers["ask_digits"] == "да" and answers["ask_uppercase_letters"] == "да":
        chararacters_enumerate = lowercase_letters + uppercase_letters + digits

    elif answers['ask_lowercase_letters'] == "да" and answers["ask_digits"] == "да" and answers["ask_uppercase_letters"] == "нет":
        chararacters_enumerate = lowercase_letters + digits

    elif answers['ask_lowercase_letters'] == "да" and answers["ask_digits"] == "нет" and answers["ask_uppercase_letters"] == "нет":
        chararacters_enumerate = lowercase_letters

    elif answers['ask_lowercase_letters'] == "нет" and answers["ask_digits"] == "нет" and answers["ask_uppercase_letters"] == "нет":
        print("Введите хотя бы одно 'да'.")
        return

    elif answers['ask_lowercase_letters'] == "да" and answers["ask_digits"] == "нет" and answers["ask_uppercase_letters"] == "да":
        chararacters_enumerate = uppercase_letters + lowercase_letters

    elif answers['ask_lowercase_letters'] == "нет" and answers["ask_digits"] == "да" and answers["ask_uppercase_letters"] == "да":
        chararacters_enumerate = uppercase_letters + digits

    elif answers['ask_lowercase_letters'] == "нет" and answers["ask_digits"] == "да" and answers["ask_uppercase_letters"] == "нет":
        chararacters_enumerate = digits

    elif answers['ask_lowercase_letters'] == "да" and answers["ask_digits"] == "нет" and answers["ask_uppercase_letters"] == "да":
        chararacters_enumerate = uppercase_letters + lowercase_letters

    elif answers['ask_lowercase_letters'] == "нет" and answers["ask_digits"] == "нет" and answers["ask_uppercase_letters"] == "да":
        chararacters_enumerate = uppercase_letters

    return chararacters_enumerate, answers["ask_count_letters"]


if __name__ == "__main__":
    main()
    print()