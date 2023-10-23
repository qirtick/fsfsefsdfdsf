# 1
def all_divisors(number):
    divisors = []
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            divisors.append(i)
            if i != number // i:
                divisors.append(number // i)
    divisors.sort()
    return divisors


numbers = [23436, 190187200, 380457890232]
for number in numbers:
    divisors = all_divisors(number)
    print(f"Делители числа {number}: {divisors}")


# 2
def three_args(*, var1=None, var2=None, var3=None):
    args = []
    if var1 is not None:
        args.append(f"var1 = {var1}")
    if var2 is not None:
        args.append(f"var2 = {var2}")
    if var3 is not None:
        args.append(f"var3 = {var3}")

    if args:
        print("Переданы аргументы:", ", ".join(args))
    else:
        print("Аргументы не были переданы.")


# Примеры вызова функции:
three_args(var1=2, var3=10)
three_args(var2="Hello")
three_args(var3=5, var1=None, var2=None)


# 3
def is_palindrome(s):
    s = s.replace(" ", "").lower()
    # Сравниваем строку с её перевёрнутой версией
    return s == s[::-1]


print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False
print(is_palindrome("A man a plan a canal Panama"))  # True


# 4
def most_common_and_longest_words(text):
    words = text.lower().split()
    words = [word.strip(".,!?") for word in words]

    word_counts = {}
    for word in words:
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1

    most_common_word = max(word_counts, key=word_counts.get)

    longest_word = max(words, key=len)

    return most_common_word, longest_word


text = input("Введите текст: ")

most_common, longest = most_common_and_longest_words(text)
print(f"Наиболее часто встречающееся слово: {most_common}")
print(f"Самое длинное слово: {longest}")


# 5
def generate_spiral_matrix(n, m):
    matrix = [[0] * m for _ in range(n)]
    num = 1

    top, bottom, left, right = 0, n - 1, 0, m - 1

    while num <= n * m:
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1

        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1

    return matrix


n = int(input("Введите количество строк: "))
m = int(input("Введите количество столбцов: "))

spiral_matrix = generate_spiral_matrix(n, m)

for row in spiral_matrix:
    for num in row:
        print(num, end="\t")
    print()
    # 6def is_magic_square(matrix):
    n = len(matrix)

    expected_sum = sum(matrix[0])

    for i in range(1, n):
        if sum(matrix[i]) != expected_sum:
            return False

    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != expected_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != expected_sum:
        return False

    if sum(matrix[i][n - i - 1] for i in range(n)) != expected_sum:
        return False

    return True

matrix = [
    [2, 7, 6],
    [9, 5, 1],
    [4, 3, 8]
]

if is_magic_square(matrix):
    print("Это магический квадрат.")
else:
    print("Это не магический квадрат.")