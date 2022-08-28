import re
def arithmetic_arranger(problems, arg=False):
    upper = ""
    lower = ""
    result = ""
    seperator = ""
    if len(problems) > 5:
        return "Error: Too many problems."
    for i in problems:
        line = i.split(" ")
        if (re.search("[^\s0-9.+-]", i)):
            if (re.search("[/]", i) or re.search("[*]", i)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        if ((len(line[0]) >= 5) or (len(line[2]) >= 5)):
            return "Error: Numbers cannot be more than four digits."
        first = line[0]
        second = line[2]
        operator = line[1]
        range = max(len(first), len(second)) + 2
        Sum = ""
        if (operator == "+"):
            Sum = str(int(first) + int(second)).rjust(range)
        else:
            Sum = str(int(first) - int(second)).rjust(range)
        top = first.rjust(range)
        bottom = operator + second.rjust(range - 1)
        dashes = ("-" * range)
        if (i != problems[-1]):
            upper += top + "    "
            lower += bottom + "    "
            result += Sum + "    "
            seperator += dashes + "    "
        else:
            upper += top
            lower += bottom
            result += Sum
            seperator += dashes
    if arg:
        string = upper + "\n" + lower + "\n" + seperator + "\n" + result
    else:
        string = upper + "\n" + lower + "\n" + seperator
    return string
