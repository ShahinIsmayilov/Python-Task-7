import random
import math

def kvadrat_ededler():
    ədədlər = []
    while len(ədədlər) < 5:
        rəqəm = random.randint(20, 50)
        if rəqəm % 2 == 0:
            ədədlər.append(int(math.pow(rəqəm, 2)))
    return ədədlər

nəticə = kvadrat_ededler()
print(nəticə)
