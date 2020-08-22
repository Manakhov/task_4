def to_dec(str):
    value = 0
    for i in range(len(str)):
        value += 2**(len(str) - i - 1) * int(str[i])
    if value == 32:
        return "Пробел"
    elif 32 < value < 127:
        return chr(value)
    else:
        return "Ошибка. Введенный код не соответствует таблице ASCII"


str_user = input()
print(to_dec(str_user))
