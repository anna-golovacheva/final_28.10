def iss(obj_1, obj_2):
    if obj_1 is obj_2:
        address = 'один и тот же адрес'
    else:
        address = 'разные адреса'

    if obj_1 == obj_2:
        value = 'одинаковые'
    else:
        value = 'разные'

    print(f'Две переменные ссылаются на {address} в памяти, имеют {value} значения.')
    print(f'Id первой переменной: {id(obj_1)}.\nId первой переменной: {id(obj_2)}.')
    print(f'Значение первой переменной: {obj_1}.\nЗначение первой переменной: {obj_2}.')


x = y = [1, [2]]
iss(x, y)

# x, y = [1, [2]], [1, [2]]
# iss(x, y)
#
# x = [1, [2]]
# y = x.copy()
# y[1] = 2
# iss(x, y)
#
# A = 'spam'
# B = A
# B = 'shrubbery'
# iss(A, B)
#
# A = ['spam']
# B = A
# B[0] = 'shrubbery'
# iss(A, B)
#
# A = ['spam']
# B = A[:]
# B[0] = 'shrubbery'
# iss(A, B)
#
# iss([], [])
# iss('', '')
# iss({}, {})
#
# x = y = [1, True, [1, 2]]
# y[2] = [-1, -2]
# iss(x, y)
#
# x = 5
# y = 5
# iss(x, y)
