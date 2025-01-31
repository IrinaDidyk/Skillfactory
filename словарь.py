telephone = {'Миша':'8999', 'Даша':'3455', 'Opa':'1234'}
print(f'Имена моих друзей: {telephone.keys()}')
print(f'Номера телефонов моих друзей: {telephone.values()}')
print(f'Телефонная книга: {telephone.items()}')
telephone['Кто_то']='5634'
telephone['Катя']='9999'
print(f'Книга с новой записью: {telephone}')
telephone['Даша']='2222'
print(f'Книга с новой записью: {telephone}')
a = input('Введите имя друга: ')
if a in telephone:
    del telephone[a]
else:
    telephone[a]= int(input('Введите номер телефона: '))
print(f'Книга с новой записью: {telephone}')