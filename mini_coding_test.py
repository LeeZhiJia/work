def phone_letter(digits):
    # 0 and 1 do not map to any letters.
    # when 0 and 1 return []
    digits = digits.replace(' ', '').replace('0', '').replace('1', '')

    if not digits.isdigit():
        return []
    keyboard = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    res = []
    if len(digits) == 0:
        return []
    if len(digits) == 1:
        return [keyboard[digits]]
    restult = phone_letter(digits[1:])
    for i in restult[0]:
        for j in keyboard[digits[0]]:
            res.append((j+i))
    return res


if __name__ == '__main__':
    print(phone_letter('23'))
    print(phone_letter('9'))
    for i in range(99):
        print(phone_letter(str(i)))