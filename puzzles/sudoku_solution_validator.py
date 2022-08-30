def valid_solution(board):
    # проверка на 0
    null_check = [elem if 0 not in elem else False for elem in board]
    if False in null_check:
        return False

    # Проверка построчно при помощи множества set()
    hset = set()
    for i in range(9):
        for j in range(9):
            if board[i][j] in hset:
                return False
            else:
                hset.add(board[i][j])
        print(hset)
        hset = set()

    # Проверка колонок
    hset = set()
    for i in range(9):
        for j in range(9):
            if board[j][i] in hset:
                return False
            else:
                hset.add(board[j][i])
        print(hset)
        hset = set()

    # Проверка блоков 3x3
    subs = [range(0, 3), range(3, 6), range(6, 9)]
    subboards = []
    for x in subs:
        for y in subs:
            subboards.append([x, y])

    for (row_range, column_range) in subboards:
        hset = set()
        for i in row_range:
            for j in column_range:
                print(board[i][j], end=' ')
                if board[i][j] in hset:
                    return False
                else:
                    hset.add(board[i][j])

    return True
