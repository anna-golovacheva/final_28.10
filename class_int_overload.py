class Int(int):
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        super().__add__(other)
        str_num_dict = {
            1: ['один', '1'],
            2: ['два', '2'],
            3: ['три', '3'],
            4: ['четыре', '4'],
            5: ['пять', '5'],
        }
        for num, strr in str_num_dict.items():
            if other in strr:
                return self.val + num
        if type(other) is str:
            raise TypeError("справа от знака '+' непонятный текст. Если что, я понимаю текстом цифры с 1 по 5.")
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Int' and {type(other)}")


x = Int(5)
print(x + '5')
print(x + 'один')
print(x + 'пять')
# print(x + 'шесть')
# print(x + (1,))
