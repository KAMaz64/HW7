# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  

def rhythm(poem: str, details: bool = True, vowels: str = 'аиеёоуыэюя') -> bool:
    list_poem = poem.lower().split()
    list_result = [{}] * len(list_poem)
    phrase_count = [0] * len(list_poem)

    for index, phrase in enumerate(list_poem):
        phrase_count[index] = 0
        list_result[index] = {}
        for char in vowels:
            char_count = phrase.count(char)
            if char_count:
                phrase_count[index] += char_count
                list_result[index][char] = char_count

    bool_result = True if len(set(phrase_count)) == 1 else False

    return (bool_result, list_result) if details else bool_result

str_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
if rhythm(str_1):
    print('Парам пам-пам')
else:
    print('Пам парам')