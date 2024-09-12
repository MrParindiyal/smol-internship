import random


def user_input():
    try:
        password_length = int(input("Enter length of the password : "))
        difficulty_level = int(
            input(
                "Enter the level of difficulty\nLevel '1'\nLevel '2'\nLevel '3'\n<--->\n"
            )
        )

    except ValueError:
        print("Error: Use integer values only")
        exit()

    if difficulty_level not in [1, 2, 3] or password_length < 1:
        print("Error : Invalid Input, Please Try Again")
        difficulty_level = 0

    return password_length, difficulty_level


def printer(output):
    for i in output:
        print(i, end="")


def generator(length, complexity):
    seed = random.randint(0, 100)

    level1 = []
    level2 = []
    level3 = []
    out = []

    for i in range(10):
        level1.append(str(i))
        level2.append(str(i))
        level3.append(str(i))

    for j in range(26):
        level2.append(chr(97 + j))
        level3.append(chr(97 + j))

    for k in range(26):
        if chr(39 + k) not in level3:
            level3.append(chr(39 + k))

    if complexity == 1:
        for _ in range(length):
            r = random.randint(0, 100)
            out.append(level1[r % len(level1)])

    elif complexity == 2:
        for _ in range(length):
            r = random.randint(0, 100)
            if (r + seed) % 2 == 0:
                out.append(level2[r % len(level2)].upper())
            else:
                out.append(level2[r % len(level2)])

    elif complexity == 3:
        for _ in range(length):
            r = random.randint(0, 100)
            if (r + seed) % 2 == 0:
                out.append(level3[r % len(level3)].upper())
            else:
                out.append(level3[r % len(level3)])

    printer(out)
    print("")


def main():
    pw_len, lvl = user_input()

    if lvl:
        generator(pw_len, lvl)


main()
