nam = "price never got to 10"
import random
price = 0
for _ in range(random.randint(5.,15.)):
    price = price + 1
    if price == 10:
        print("price is 10")
        break
else:
    print(nam.capitalize())
    print("This is a for loop that rizes by 1 for a random amount and the else stament is if it ran throigh all its loops, i added the .capitalize sting to have the end be capitalize. but this is an intrseting concept  i came acrose on youtube and thught it was neat")
