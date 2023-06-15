def is_safe(board, row, col):
    # Перевірка рядка зверху
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Перевірка головної діагоналі зверху
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Перевірка побічної діагоналі зверху
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens(board, col):
    # Базовий випадок: всі ферзі розміщені
    if col >= n:
        return True

    for i in range(n):
        if is_safe(board, i, col):
            # Розміщення ферзя на поле (i, col)
            board[i][col] = 1

            # Рекурсивний виклик для розміщення ферзів на наступних стовпцях
            if solve_n_queens(board, col + 1):
                return True

            # Якщо розміщення ферзів на наступних стовпцях не можливе,
            # скасовуємо поточне розміщення ферзя
            board[i][col] = 0

    # Якщо всі можливі варіанти перебрані, але немає розв'язку
    return False

def print_board(board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()

n = int(input("Введіть розмір шахівниці (n): "))

# Ініціалізуємо шахівницю розміром n x n з нулями
board = [[0] * n for _ in range(n)]

# Викликаємо функцію для знаходження розв'язку
if solve_n_queens(board, 0):
    print("Розв'язок існує:")
    print_board(board)
else:
    print("Розв'язок не існує")
