def test_range(range_boundaries):
    for i in range_boundaries:
        if i > 10:
            print(f'Число {i} не попадает в диапазон')
        if i <1:
            print(f'Число {i} не попадает в диапазон')
user_input = input('Введите числа через пробел: ')
range_boundaries = list(map(int, user_input.split()))
test_range(range_boundaries)