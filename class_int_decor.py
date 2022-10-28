def int_decor(function):
    def inner(s, other):
        str_num_dict = {
            1: ['один', '1'],
            2: ['два', '2'],
            3: ['три', '3'],
            4: ['четыре', '4'],
            5: ['пять', '5'], }
        for num, strr in str_num_dict.items():
            if other in strr:
                result = function(s, num)
                return result
        if type(other) is str:
            raise TypeError("справа от знака '+' непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.")
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Int' and {type(other)}")
    return inner


class Int(int):
    def __init__(self, val):
        self.val = val

    @int_decor
    def __add__(self, other):
        return super().__add__(other)


x = Int(5)
print(x + '5')
print(x + 'один')
print(x + 'пять')
# print(x + 'шесть')
# print(x + (1,))
