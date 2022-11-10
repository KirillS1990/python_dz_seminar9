from modules.calculations.mult import mult


a = [2, 4]
b = [2, -2]


def div(number_1, number_2):
    if number_2 != [0, 0]:
        answer = [0, 0]
        denominator = [number_2[0], -(number_2[1])]
        number_1 = mult(number_1, denominator)
        number_2 = mult(number_2, denominator)
        answer[0] = number_1[0] / number_2[0]
        answer[1] = number_1[1] / number_2[0]
        return answer
    else:
        return number_1



