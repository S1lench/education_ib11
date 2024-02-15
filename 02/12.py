text = input()
symbol_count = len(text)
cost_symbol = 40
total_kopecks = symbol_count * cost_symbol
rub = total_kopecks // 100
kopeck = total_kopecks % 100
print(str(rub) + ' р.', str(kopeck) + ' коп.')
