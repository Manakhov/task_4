def show_base(str):
    value = 0
    for st in str:
        value_ascii = ord(st)
        if value_ascii < 48 or 57 < value_ascii < 65 or 90 < value_ascii < 97 or value_ascii > 122:
            return False
        if value_ascii > value:
            value = value_ascii
    if 47 < value < 58:
        return value - 47
    elif 64 < value < 91:
        return value - 54
    elif 96 < value < 123:
        return value - 60


def to_dec(str, base):
    value = 0
    if base is False:
        return "Ошибка. Код содержит недопустимые символы."
    for i in range(len(str)):
        value_ascii = ord(str[i])
        if value_ascii < 58:
            value_symbol = value_ascii - 48
        elif value_ascii < 91:
            value_symbol = value_ascii - 55
        else:
            value_symbol = value_ascii - 61
        value += base**(len(str) - i - 1) * value_symbol
    if value == 32:
        return "Пробел"
    elif 32 < value < 127:
        return chr(value)
    return "Ошибка. Код не соответствует таблице ASCII."


str_user = input()
print(to_dec(str_user, show_base(str_user)))
