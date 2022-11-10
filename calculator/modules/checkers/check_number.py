from modules.checkers.check_first_number import check_first_number
from modules.checkers.check_complex_number import check_complex_number


def check_number(number):
    if number[-1] == "i":
        number = number.replace("-", "+-")
        if number[0] == "+":
            number = number[1:]
        if "+" not in number:
            number = "0+" + number
        answer = number.split("+")
        if len(answer) == 2:
            answer = (check_first_number(answer[0]), check_complex_number(answer[1]))
    else:
        answer = [check_first_number(number), int(0)]
    if answer[0] != "Ошибка" and answer[1] != "Ошибка":
        return answer
    return "Ошибка"
