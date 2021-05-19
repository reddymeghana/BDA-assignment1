import random
file = open('input1.txt', 'w')
for x in range(1000000000):
    n = random.randint(1,100000000)
    file.write(str(n))
file.close()
    


