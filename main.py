

field = [ [" "] * 3 for i in range (3) ]
field

def show():
    print(f"   0 1 2")
    for i in range(3):
        print(f" {i} {field[i][0]} {field[i][1]} {field[i][2]}")


def goo():
    while True:
        cords = input("Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите две координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите число! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Координаты не верны! ")
            continue

        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y


def chemp():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл крестик")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл нолик")
            return True
    return False



field = [[" "] * 3 for i in range(3)]
count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит крестик!")
    else:
        print("Ходит нолик!")

    x, y = goo()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "0"

    if chemp():
        break

    if count == 9:
        print("Ничья!")
        break