n = int(input("Введите количество тестируемых людей: "))

prev_avg_iq = 0

for i in range(n):
    iq = int(input("Введите IQ: "))
    if i == 0:
        print("0")
    else:
        if iq > prev_avg_iq:
            print(">")
        elif iq < prev_avg_iq:
            print("<")
        else:
            print("0")
    prev_avg_iq = (prev_avg_iq * i) / (i + 1) + iq / (i + 1) if i > 0 else iq
