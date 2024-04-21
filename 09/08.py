soup_of_the_day = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]

num_days = int(input())

for i in range(num_days):
    day_index = i % len(soup_of_the_day)
    print(soup_of_the_day[day_index])
