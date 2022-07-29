# Реализуйте RLE алгоритм: реализуйте модуль
# сжатия и восстановления данных.


def code_compession(list):
    my_list = ""
    i = 0
    while i < len(list):
        count = 1
        while i + 1 < len(list) and list[i] == list[i+1]:
                count += 1
                i += 1
        my_list += str(count) + list[i]
        i += 1
    return my_list
list = 'WWWWWWBBBBBWWWBBBWWWWWWWWWBBB'
my_list = code_compession(list)
print(f'Результат сжатия: ', code_compession(list))

# сжатие получилось, но в восстановлении остановилась 
# на цикле 37-41 строки, не знаю, как вывести буквы
def code_recovery(list1):
       
    word_list = list1.split()
    my_list1 = []
    my_list2 = []
    for word in word_list:
        if word.isnumeric():
            my_list1.append(int(word))
        else:
            my_list2.append(str(word))
    print(my_list1)
    print(my_list2)

    list3 = []
    a = ''
    for j in my_list2:
        for i in my_list1:
            a = (j * i)
            list3.append(a)
        i += 1
    print(a)
    return list3
list1 = input('Введите числа и буквы через пробел: ')
list3 = code_recovery(list1)
print(code_recovery)
   



# так проще вытащить числа из списка (это для себя)
# import re
# string = '2W3I4G'
# numbers = r"\d"
# result = re.findall(numbers, string)
# print(result) 

