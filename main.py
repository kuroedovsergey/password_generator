import random

################################################
# словарь и числа
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '1234567890'
special_characters = '@#$%^&*!?+-*/}{][()'
result_pass = ''

# input_answers = {
#     'да': 'да',
#     'нет':'нет'
# }

answer_yes = 'да'
answer_no = 'нет'


def main(*args):
    print(f'''Генератор пароля. Укажите требуемые настройки для создания пароля. ''')
    ask_count_letters = input("Введите количество символов: ")

    if not ask_count_letters.isdigit():
        answer_error('Укажите количество цифр для длины пароля')

    ask_lowercase_letters = input("Строчные буквы (да/нет): ")
    if ask_lowercase_letters not in (answer_no, answer_yes):
        answer_error()

    ask_uppercase_letters = input("Заглавные буквы (да/нет): ")
    if ask_uppercase_letters not in (answer_no, answer_yes):
        answer_error()

    ask_digits = input("Цифры (да/нет): ")
    if ask_digits not in (answer_no, answer_yes):
        answer_error()

    ask_special_letters = input("Специальные символы (да/нет): ")
    if ask_special_letters not in (answer_no, answer_yes):
        answer_error()

    available_choice_pass(ask_count_letters=ask_count_letters,
                          ask_lowercase_letters=ask_lowercase_letters,
                          ask_digits=ask_digits,
                          ask_uppercase_letters=ask_uppercase_letters,
                          ask_special_letters=ask_special_letters)


def available_choice_pass(**answers):
    result_pass = ''
    input_anwsers, input_answer_count_pass = answer_worker(answers)
    chararacters_enumerate = characters_preparation(input_anwsers)

    for answer in range(input_answer_count_pass):

        chararacters_list = list(chararacters_enumerate)
        random.shuffle(chararacters_list)

        result_pass += random.choice(chararacters_list)

    print(result_pass)


def answer_worker(answers):
    input_answers_list = []

    for i in answers.values():
        if i.isalpha():
            input_answers_list.append(i)
        if i.isdigit():
            input_answer_count_pass = int(i)

    return input_answers_list, input_answer_count_pass


def characters_preparation(input):
    result_character = ''
    characters_enumerate = ''
    alphabet = all_option_answers()
    input_value = {
        'да': '1',
        'нет': '0'
    }


    for key in input:
        characters_enumerate += str(input_value[key])
    
    if callable(alphabet[characters_enumerate]):
        alphabet[characters_enumerate]('Укажите хотя бы одно из значений')
    else:
        result_character = alphabet[characters_enumerate]

    return result_character

##################################
# Логиа выбора полученного ответа
#
# нет нет нет нет // ошибка ввода
# нет нет нет да // только специальные символы
# нет нет да нет // только цифры
# нет нет да да // цифры и специальные символы
# нет да нет нет // только заглавные буквы
# нет да нет да // заглавные буквы + специальные символы
# нет да да нет // заглавные буквы + цифры
# нет да да да // заглвные буквы + цифры + специальные символы
# да нет нет нет // только строчные буквы
# да нет нет да // строчные буквы + специальные символы
# да нет да нет // строчные буквы + цифры
# да нет да да  // строчные буквы + цифры + специальные символы
# да да нет нет // строчные буквы + заглавные буквы
# да да нет да // строчные буквы + заглавные буквы + специальные символы
# да да да нет // строчные буквы + заглавные буквы + цифры
# да да да да // строчные буквы + заглавные буквы + цифры + специальные символы
#
#
def all_option_answers():

    alphabet_variables = {
        '0000': answer_error,
        '0001': special_characters,
        '0010': digits,
        '0011': digits + special_characters,
        '0100': uppercase_letters,
        '0101': uppercase_letters + special_characters,
        '0110': uppercase_letters + digits,
        '0111': uppercase_letters + digits + special_characters,
        '1000': lowercase_letters,
        '1001': lowercase_letters + special_characters,
        '1010': lowercase_letters + digits,
        '1011': lowercase_letters + digits + special_characters,
        '1100': lowercase_letters + uppercase_letters,
        '1101': lowercase_letters + uppercase_letters + special_characters,
        '1110': lowercase_letters + uppercase_letters + digits,
        '1111': lowercase_letters + uppercase_letters + digits + special_characters,
    }

    return alphabet_variables


def answer_error(answer='Введите да или нет'):
    print("-------------------------------------------------")
    print(f'''{answer}''')
    exit()


if __name__ == "__main__":
    main()
    print()
