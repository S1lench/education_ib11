boris = input()
vova = input()
dima = input()

if boris > vova and vova > dima:
    print(boris)
    print(vova)
    print(dima)
elif boris > dima and dima > vova:
    print(boris)
    print(dima)
    print(vova)
elif vova > boris and boris > dima:
    print(vova)
    print(boris)
    print(dima)
elif vova > dima and dima > boris:
    print(vova)
    print(dima)
    print(boris)
elif dima > boris and boris > vova:
    print(dima)
    print(boris)
    print(vova)
elif dima > vova and vova > boris:
    print(dima)
    print(vova)
    print(boris)