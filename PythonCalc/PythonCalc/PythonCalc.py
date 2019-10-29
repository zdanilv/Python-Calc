def Add(x, y):
    result = int(x) + int(y)
    print('Результат: ' + str(result))

def Subtract(x, y):
    result = int(x) - int(y)
    print('Результат: ' + str(result))

def Multiply(x, y):
    result = int(x) * int(y)
    print('Результат: ' + str(result))

def Divide(x, y):
    result = int(x) / int(y)
    print('Результат: ' + str(result))

def Mod(x, y):
    result = int(x) % int(y)
    print('Результат: ' + str(result))

def Square(x, y):
    result = int(x) ** int(y)
    print('Результат: ' + str(result))

def main():
    while True:
        inp = input('Возможные операции с ДВУМЯ числами:\n "+", "-", "*", "/", "%", "^".\n')
        listinput = inp.split()

        try:
            x = listinput[0]
            key = listinput[1]
            y = listinput[2]
        except Exception: 
            print('Ошибка при вводе!')
            continue
        
        if key == '+':
            Add(x, y)
        elif key == '-':
            Subtract(x, y)
        elif key == '*':
            Multiply(x, y)
        elif key == '/':
            Divide(x, y)
        elif key == '%':
            Mod(x, y)
        elif key == '^':
            Square(x, y)
        else: continue

main()
