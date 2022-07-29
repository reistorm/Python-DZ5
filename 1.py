# Напишите программу, удаляющую из текста 
# все слова, содержащие ""абв""

with open('text2.txt', 'w', encoding='UTF=8') as file:
    file.write('абвр, урк, праивб, абрп, вабвп, абв')

def delete_word():
    list1 = []
    with open('text2.txt', 'r') as file:
        for i in file:
            if 'абв' not in i:
                list1.append(i)
        print(list1)
    file.close()
delete_word()

# Основная часть программы получилась, но в методе 
# вывод списка без абв получился искаженный 

# list = ['абвр', 'урк', 'праивб', 'абрп', 'вабвп', 'абв']
# list1 = []
# for i in list:
#     if 'абв' not in i:
#         list1.append(i)
# print(list1)