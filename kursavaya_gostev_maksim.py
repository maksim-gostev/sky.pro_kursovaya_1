#импортируем библиотеку рандома
from random import randint
#создаём словари азбуки морзе
morse_code_dictionary_eng ={'a': '.-',
                            'b': '-...',
                            'c': '-.-.',
                            'd': '-..',
                            'e': '.',
                            'f': '..-.',
                            'g': '--.',
                            'h': '....',
                            'i': '..',
                            'j': '.---',
                            'k': '-.-',
                            'l': '.-..',
                            'm': '--',
                            'n': '-.',
                            'o': '---',
                            'p': '.--.',
                            'q': '--.-',
                            'r': '.-.',
                            's': '...',
                            't': '-',
                            'u': '..-',
                            'v': '...-',
                            'w': '.--',
                            'x': '-..-',
                            'y': '-.--',
                            'z': '--..',
                            '1': '.----',
                            '2': '..---',
                            '3': '...--',
                            '4': '....-',
                            '5': '.....',
                            '6': '-....',
                            '7': '--...',
                            '8': '---..',
                            '9': '----.',
                            '0': '-----',
                            }

morse_code_dictionary_ru = {'а': '.-' ,
                         'б': '-...' ,
                         'в': '.--' ,
                         'г': '--.' ,
                         'д': '-..' ,
                         'е': '.' ,
                         'ж' : '...-' ,
                         'з': '--..' ,
                         'и': '..' ,
                         'й': '.---' ,
                         'к': '-.-' ,
                         'л': '.-..' ,
                         'м': '--' ,
                         'н': '-.' ,
                         'о':'---' ,
                         'п': '.--.' ,
                         'р': '.-.' ,
                         'с': '...' ,
                         'т': '-' ,
                         'у': '..-' ,
                         'ф': '..-.' ,
                         'х': '....' ,
                         'ц': '-.-.' ,
                         'ч': '---.' ,
                         'ш': '----' ,
                         'щ': '--.-' ,
                         'ъ': '.--.-.' ,
                         'ы': '-.--' ,
                         'ь': '-..-' ,
                         'э': '..-..' ,
                         'ю': '..--' ,
                         'я': '.-.-',
                         '1': '.----',
                         '2': '..---',
                         '3': '...--',
                         '4': '....-',
                         '5': '.....',
                         '6': '-....',
                         '7': '--...',
                         '8': '---..',
                         '9': '----.',
                         '0': '-----',
                                        }

#создаём списки слов
words_of_list_ru = ['папа', 'мама', 'мир', 'тобот', 'трансформер', 'питон', 'учиться']

words_of_list_eng =['dad', 'mom', 'world', 'tobot', 'transformer', 'python', 'learn']

# словарь заменяемых символов
character_replacement_dictionary = {
                                    ',': '',
                                    '.': '',
                                    '!': '',
                                    '?': '',
                                    '(': '',
                                    ')': '',
                                    ';': '',
                                    ':': '',
                                    '"': '',
}

# словарь перевода с азбуки морзе
morse_code_translation_dictionary = {}

#создаём соловарь правельных ответов
counting_responses = {}


def runer():
    choosing_an_action = input('Что вы хотите сделать\n'
                               'если перевести текст нажмите "1"\n'
                               'если проверить знания азбуки морзе нажмите "2"\n')
    if choosing_an_action == '1':
        text = input('Ввебите текст: \n')
        return turning_text_into_a_list(text, character_replacement_dictionary)
    elif choosing_an_action == '2':
        input('Сегодня мы потренируемся расшифровывать азбуку Морзе.\n'
              'Нажмите Enter и начнем')
        return choosing_the_testing_language()
    else:
        print(f'Неверный ввод\n{"-" * 14}')
        return runer()


def choosing_the_testing_language():
    """
    выбор языка
    """
    language_selection = input('Выберите язык(select a language)(ru, eng):\n')
    if language_selection == 'ru':
        language = 'ru'
        return questions_and_answer_processing(language)
    elif language_selection == 'eng':
        language = 'eng'
        return questions_and_answer_processing(language)
    else:
        print('непонятный выбор, попробуйте снова(unclear choice, try again)'
              '____________________________________________________________\n')
        choosing_the_testing_language()


def questions_and_answer_processing(language):
    """
    вопросы и обработки ответов
    """
    #переменная в которой будет зашифровонное слово
    collected_word = ''
    # нумирация слов
    count = 1
    if language == 'ru':
        print('Начинаем игру')
        while len(words_of_list_ru) > 0:
            random_index = randint(0, len(words_of_list_ru) - 1)
            random_word = words_of_list_ru[random_index]
            for i in random_word:
                collected_word += morse_code_dictionary_ru[i] + ' '
            answer = input(f'Слово {count} – "{collected_word}" - ')
            if answer == random_word:
                print(f'Верно, {random_word}')
            else:
                print(f'Ответ неверный. Верный ответ – {random_word}')

            counting_responses[random_word] = answer == random_word
            del words_of_list_ru[random_index]
            collected_word = ''
            count += 1
    else:
        print('Starting the game')
        while len(words_of_list_eng) > 0:
            random_index = randint(0, len(words_of_list_eng) - 1)
            random_word = words_of_list_eng[random_index]
            for i in random_word:
                collected_word += morse_code_dictionary_eng[i] + ' '
            answer = input(f'Word {count}"{collected_word}" - ')
            if answer == random_word:
                print(f'Right, {random_word}')
            else:
                print(f'The answer is incorrect. The correct answer – {random_word}')
            counting_responses[random_word] = answer == random_word
            del words_of_list_eng[random_index]
            collected_word = ''
            count += 1
    return counting_results(language)


def counting_results(language):
    """
    подсчёт правельных и неправельных ответов
    """
    #переменная подсчёта количества вопросов
    counter = 0
    # переменная подсчёта количества правельных ответов
    counter_true = 0
    # переменная подсчёта количества правельных ответов
    counter_folse = 0

    for i, item in enumerate(counting_responses.values(), start=1):
        if item == True:
            counter_true += 1
        else:
            counter_folse += 1
        counter = i
    return the_answer(counter, counter_true, counter_folse, language)


def the_answer(counter, counter_true, counter_folse, language):
    """
    вывод результатов
    """
    #список склонения
    answer_ending = ['вопрос', 'вопроса', 'вопросов']
    print('________________________________')
    if language == 'ru':
        if counter > 100:
            counter_100d = counter % 100
            if counter_100d == 0:
                answer_ending = answer_ending[2]
            elif counter_100d == 1:
                answer_ending = answer_ending[0]
            elif 0 < counter_100d < 5:
                answer_ending = answer_ending[1]
            else:
                answer_ending = answer_ending[2]
        elif counter > 20:
            counter_d10 = counter % 10
            if counter_d10 == 0:
                answer_ending = answer_ending[2]
            elif counter_d10 == 1:
                answer_ending = answer_ending[0]
            elif 0 < counter_d10 < 5:
                answer_ending = answer_ending[1]
            else:
                answer_ending = answer_ending[2]
        else:
            if counter == 0:
                answer_ending = answer_ending[2]
            elif counter == 1:
                answer_ending = answer_ending[0]
            elif 0 < counter < 5:
                answer_ending = answer_ending[1]
            else:
                answer_ending = answer_ending[2]
            print(f'Вот и все! Вы ответили на {counter} {answer_ending}\n'
                  f'Правельных ответов : {counter_true}\n'
                  f'Неправельных ответов : {counter_folse}')
        print('Ваш ранг:')
        if counter_true == 0:
            print("Нулевой")
        elif 0.2 < counter_true / counter < 0.5:
            print("Так себе")
        elif 0.5 < counter_true / counter < 0.75:
            print("Норм")
        elif 0.75 < counter_true / counter < 0.9:
            print("Хорошо")
        else:
            print("Отлично")
        print('Всего доброго')
    else:
        print(f"That's it! You have answered to {counter} questions\n"
              f"Correct answers : {counter_true}\n"
              f"Incorrect answers : {counter_folse}")
        print('Your rank:')
        if counter_true == 0:
            print("is Zero")
        elif 0.2 < counter_true / counter < 0.5:
            print(" is So-so")
        elif 0.5 < counter_true / counter < 0.75:
            print("is Normal")
        elif 0.75 < counter_true / counter < 0.9:
            print("Is Good")
        else:
            print("is Excellent")
        print('Have a nice day')


def turning_text_into_a_list(text, character_replacement_dictionary):
    """
    убираем из текста все знаки припенания
    и превращаем строку в список
    """
    if text[0] == '.' or text[0] == '-':
        text_list = text.split()
        return choosingthe_language_to_translate_into(text_list)
    else:
        for key, item in character_replacement_dictionary.items():
            text = text.replace(key, item).lower()
        text_list = text.split()
        return defining_the_language(text_list)


def defining_the_language(text_list):
    """
    определяем язык текста
    """
    index = 0
    while text_list[index].isdigit() and len(text_list) - 1 > index:
        index += 1
    for letter in text_list[index]:
        if letter[0] in morse_code_dictionary_ru:
            return translation_russian_text(text_list)
        elif letter[0] in morse_code_dictionary_eng:
            return translation_english_text(text_list)


def translation_russian_text(text_list):
    """
    переводит текст с русского  языка
    в азбуку морзе
    """

    # переменная нового текста
    new_text = ''
    # переменная нового слова
    new_word = ''
    for word in text_list:
        for letter in word:
            new_word += morse_code_dictionary_ru[letter] + ' '
    new_text += new_word
    return print(new_text)


def translation_english_text(text_list):
    """
       переводит текст с английского  языка
       в азбуку морзе
       """
    # переменная нового текста
    new_text = ''
    # переменная нового слова
    new_word = ''
    for word in text_list:
        for letter in word:
            new_word += morse_code_dictionary_eng[letter] + ' '
    new_text += new_word
    return print(new_text)


def choosingthe_language_to_translate_into(text_list):

    language_selection = input('На какой язык вы хотите перевести текст(ru \ eng): \n')
    if language_selection == 'ru':
        return translation_from_morse_into_russian(text_list)
    elif language_selection == 'eng':
        return translation_from_morse_into_english(text_list)
    else:
        print(f'Непонятный ввод\n{"-" * 15 }')
        return choosingthe_language_to_translate_into(text_list)


def translation_from_morse_into_russian(text_list):
    new_text = ''
    for key, item in morse_code_dictionary_ru.items():
        morse_code_translation_dictionary[item] = key

    for word in text_list:
        new_text += morse_code_translation_dictionary[word]
    return print(new_text)


def translation_from_morse_into_english(text_list):
    new_text = ''
    for key, item in morse_code_dictionary_eng.items():
        morse_code_translation_dictionary[item] = key

    for word in text_list:
        new_text += morse_code_translation_dictionary[word]
    return print(new_text)

runer()