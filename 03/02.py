pasword = input()
pasword1 = input()
if len(pasword1) < 8:
    print('Короткий!')
elif pasword != pasword1:
    print('Различаются!')
else:
    print('ОК')
