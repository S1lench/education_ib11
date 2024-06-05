def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def larger_root(p, q):
    d = discriminant(1, p, q)
    return (-p + d ** 0.5) / 2


def smaller_root(p, q):
    d = discriminant(1, p, q)
    return (-p - d ** 0.5) / 2


def main():
    p = float(input("Введите значение p: "))
    q = float(input("Введите значение q: "))

    d = discriminant(1, p, q)
    smaller = smaller_root(p, q)
    larger = larger_root(p, q)

    print(d)
    print(smaller, larger)


if __name__ == "__main__":
    main()
