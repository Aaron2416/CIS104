sc = input('inter score ')
try:
    sc = float(sc)
    if sc<0.0 or sc>1.0:
        print('error')
    elif sc >= 0.9:
        print('A')
    elif sc >= 0.8:
        print('B')
    elif sc >= 0.7:
        print('C')
    elif sc >= 0.6:
        print('D')
    elif sc < 0.6:
        print('F')
except:
    print("use a number")
