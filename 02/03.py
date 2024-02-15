people1 = 3
row = 140
if row // people1 // 2 == 0:
    brigada = row / people1
else:
    brigada = int(row // people1 // 2) + 1
print(brigada)
