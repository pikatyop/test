
def calc (a,b,symbol):
    if symbol == 1:
        return str(a+b)
    elif symbol == 2:
        return str(a-b)
    elif symbol == 3:
        if b ==0:
            return "Vasya"
        else:
            return str(a/b)
    elif symbol == 4:
        return str(a*b)


a = b = symbol = 0
while True:
    symbol = int(input("Що делаєм: 1+,2-,3/,4*,5 - exit"))
    if symbol == 5:
        break
    a = int(input("first num"))
    b = int(input("second num"))
    print("Answer:",calc(a,b,symbol))
