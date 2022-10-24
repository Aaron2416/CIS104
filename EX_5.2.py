max_num = None
min_num = None

while True:
    num = input('Enter number:' )
    if num == 'done':
        break
    try:
        num = int(num)
        if max_num is None or num > max_num:
            max_num = num
        if min_num is None or num < min_num:
            min_num = num
    except:
        print('Invalide input')

print("Max num: ",max_num)
print("Min num: ",min_num)
