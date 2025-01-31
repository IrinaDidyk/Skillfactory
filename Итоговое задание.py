import random
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина', 'Борис', 'Ирина']
students.sort()
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}
for student in students:
    students_marks[student] = {}
    for class_ in classes:
        marks = [random.randint(1,5) for i in range(3)]
        students_marks[student][class_] = marks
for student in students:
    print(f'''{student}{students_marks[student]}''')
    print('''
            Список команд:
            1. Добавить оценки ученика по предмету
            2. Вывести средний балл по всем предметам по каждому ученику
            3. Вывести все оценки по всем ученикам
            4. Удалить оценки ученика по предмету
            5. Редактировать данные по предметам и ученикам
            6. Вывести все оценки для определенного ученика
            7. Вывод среднего балла по каждому предмету по определенному ученику
            8. Выход из программы
            ''')
while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        for student in students:
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum//marks_count}')
                print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        for student in students:
            print(student)
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
                print()
    elif command == 4:
        print('4.Удалить оценки ученика по предмету')
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            mark = int(input('Введите оценку, которую хотите удалить: '))
            if mark in students_marks[student][class_]:
                students_marks[student][class_].remove(mark)
                print(f'Оценка {mark} ученика {student} по предмету {class_} удалена.')
            else:
                print(f'Оценка {mark} не найдена у ученика {student} по предмету {class_}.')
    elif command == 5:
        print('5. Редактировать данные по предметам и ученикам')
        student = input('Введите имя ученика: ')
        student1 = input('Введите новое имя ученика: ')
        class_ = input('Введите предмет: ')
        class_1 = input('Введите новое название предмета: ')
        if student in students and class_ in classes:
            index1 = students.index(student)
            print(f'Индекс элемента "{student}": {index1}')
            index2 = classes.index(class_)
            print(f'Индекс элемента "{class_}": {index2}')
            students[index1] = student1
            classes[index2] = class_1
        print(f'Обновленные данные: Студенты: {students}, \n Предметы: {classes}')
    elif command == 6:
        print('6. Вывести все оценки для определенного ученика')
        for student in students:
            student = input('Введите имя ученика: ')
            print(student)
            print(f'Список предметов с оценками: {students_marks[student]}')
            print()
            break
    elif command == 7:
        print('7. Вывод среднего балла по каждому предмету по определенному ученику')
        for student in students:
            student = input('Введите имя ученика: ')
            print(student)
            for class_ in classes:
                marks_sum = sum(students_marks[student][class_])
                marks_count = len(students_marks[student][class_])
                print(f'{class_} - {marks_sum//marks_count}')
                print()
            break
    elif command == 8:
        print('8. Выход из программы')
        break