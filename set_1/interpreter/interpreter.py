def main():
    expression = input("Expression: ")
    print(interpret(expression))


def interpret(express):
    x, y, z = express.split()
    match y:
        case '+':
            return float(int(x) + int(z))
        case '-':
            return float(int(x) - int(z))
        case '*':
            return float(int(x) * int(z))
        case '/':
            if int(z) == 0:
                z = int(z) + 1
            return float(int(x) / int(z))
        case _:
            return 0


main()
