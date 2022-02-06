import random


def insert_num():
    empty_cells = []
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 0:
                empty_cells.append((i, j))

    if len(empty_cells) == 0:
        return False
    insert_at = random.choice(empty_cells)
    i = insert_at[0]
    j = insert_at[1]
    matrix[i][j] = random.choice([2, 4])


def can_merge():
    for i in range(size):
        for j in range(size - 1):
            if matrix[i][j] == matrix[i][j + 1]:
                return True

    for i in range(size - 1):
        for j in range(size):
            if matrix[i][j] == matrix[i + 1][j]:
                return True
    return False


def merge_left():
    for i in range(size):
        for j in range(size - 1):
            if matrix[i][j] != 0 and matrix[i][j] == matrix[i][j + 1]:
                matrix[i][j] *= 2
                matrix[i][j + 1] = 0


def merge_right():
    for i in range(size):
        for j in range(size - 1, 0, -1):
            if matrix[i][j] != 0 and matrix[i][j] == matrix[i][j-1]:
                matrix[i][j] *= 2
                matrix[i][j-1] = 0


def transpose():
    global matrix
    matrix = [list(t) for t in zip(*matrix)]


def shift_right():
    for i in range(size):
        zero = size - 1
        for j in range(size - 1, -1, -1):
            if matrix[i][j] != 0:
                matrix[i][j], matrix[i][zero] = matrix[i][zero], matrix[i][j]
                zero -= 1


def shift_left():
    for i in range(size):
        zero = 0
        for j in range(size):
            if matrix[i][j] != 0:
                matrix[i][j], matrix[i][zero] = matrix[i][zero], matrix[i][j]
                zero += 1


over = False
valid_ip = True
print("2048 GAME")
size = int(input("Enter size of the grid: "))
matrix = [[0 for i in range(size)] for j in range(size)]


insert_num()
insert_num()
for i in range(size):
    print(matrix[i])
print("Instructions: \nPress 1 for sliding UP or \nPress 4 for sliding DOWN or "
      "\nPress 2 for sliding LEFT or \nPress 3 for sliding RIGHT\n")

while not over:
    command = int(input("Enter direction: "))

    # up
    if command == 1:
        transpose()
        shift_left()
        merge_left()
        shift_left()
        transpose()

    # down
    elif command == 4:

        transpose()
        shift_right()
        merge_right()
        shift_right()
        transpose()

    # left
    elif command == 2:
        shift_left()
        merge_left()
        shift_left()

    # right
    elif command == 3:
        shift_right()
        merge_right()
        shift_right()

    else:
        valid_ip = True
        print("Enter valid input")

    if valid_ip:
        if insert_num() == False:
            over = True
            print("Wrong move. Game Over!!")
        else:
            for i in range(size):
                print(matrix[i])

    found = False
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == 2048:
                found = True
                break
    if found:
        over = True
        print("Congratulation! You won.")

    else:
        empty = False
        for i in range(size):
            for j in range(size):
                if matrix[i][j] == 0:
                    empty = True
                    break
        if not (empty or can_merge()):
            over = True
            print("Game Over!!")
