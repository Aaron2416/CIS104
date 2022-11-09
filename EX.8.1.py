list_one = [1, 2, 3, 4, 5]
list_two = [1, 2, 3, 4, 5]

def chop(list_one):
    list_one.remove(1)
    list_one.remove(5)
    return None

def middle(list_two):
    new = list_one
    del new[-1]
    del new [0]
    return new

list_two = chop(list_two)
print(list_one)

list_two = middle(list_two)
print(list_two)
