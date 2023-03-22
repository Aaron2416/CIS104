list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
counter = 0
for n in list:
    counter = counter + 1
    if counter < 3: 
        print(n)

print ('final report: ', list[2], list[5], list[7])