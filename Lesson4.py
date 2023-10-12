# # метод find
# word = 'Denis'
# text = 'Hi {}Denis'
# print(text.find(word))  #возвращает индекс найденного элемента в строке, возвращает '-1' если не найдёт.
# print(text.index(word)) # индекс прервёт выполнение метода
#
# #%d- (типы преобразования) % позволяет что-то подставить d - десятичный
# #%s - подстановка строки
# x = 'my favorite number is: %s(%d)' %('три', 3)
# #примичание по pep8 пробел нужен после %
# print(type(x)) # строка
# print(x)
#
# # интерполяция - точка подстановки определяется с помощью фигурных скобочек
# print(text)
# print(text.format('\n'))
#
# ned = f'Просто добавим сюда имя: {word}' # f-стрим
# print (ned) # Просто добавим сюда имя: Denis
#
## ==================== Программа ====================
#
# min_salary = 1_000_000
# min_expirance = 5
# salary = float(input('Write anual salary: '))
# years_job = int(input('Enter expirance: '))
# if salary >= min_salary: # минимальная зарплата больше или равно ( 1_000_000)
#     if years_job>= min_expirance:
#         print("Welcome to Us !")
#     else:
#         print('You unknow :(')
# else:
#     print('Again try someyaer')
#
# #
# and or not  - логические операторы

number = True
if number:          # точно так же: if number == True
    print('True')
                    # короткая форма записи, называется ещё синтаксический САХАР


number = set()
if number!=1 : # этот параметр оператора if называется ФЛАГ
    print('True')

sum = 0
sum = sum +1
sum += 1        # синтаксический САХАР

# Что есть истина ?????
# False приравнивается: False, 0, 0.0, '', [], (), set(), None ( спец. для питона разработан, No - в др. языках)
# Всё остальное True.

num = 3
if num := num-3:     # может сделать выражение и проверить условие на True + отработать МОРЖ из паскаля (num := 3)
    print('yes1')

number_1 = 5
if number_1 > 4 - 3: # можно сделать операцию сравнения
    print('yes2')

limit = 100
limit2 = 500

diffirance =  limit2 - limit
if diffirance >40:
    print('yes3')

if novaja_preremennaj :=  limit2 - limit: # МОРЖ может объявить сразу новую переменную
    print('yes4')
print (novaja_preremennaj)

#=================================
tex = 'Hello World'

tex_len = len(tex)
i = 0 # счётчик count
flag = True
while flag and i<= tex_len-1:
    print(tex[i])
    i+=1


# 2-ой вариант
# tex = 'Hello World'
#
# tex_len = len(tex)
# count = 0 # счётчик
# flag = True
# while flag:
#     while count<= tex_len-1:
#         print(tex[count])
#         count+=1
#     flag = False
# ======================== ДОМ ЗАДАНИЕ ======================
# Повторить вложенные циклы
# Вводишь число с клавятуры угадать число от 0 до 100
# библиотека sys что за методо sys.exit()
# while True + библиотека sys если с клавы введут слово exit то отработает метод sys.exit()
# игра камень ножницы бумага - если останется время
# ввод число с Клавятуры, чтобы подставлялось в цикл for и выводить чётные числа от 0 до введённого числа (от 0 до  100)
# с помощью contunius
