import random

a = range(5)
b = random.sample(a, len(a))
print ("len(a): ", len(a))
print ("a is: " , a)
print ("b is: ", b)
print ("Are the two lists same? True or False? ", a == b)
test = ",".join(str(x) for x in b).replace(",","",len(",".join(str(x) for x in b)))

print(test)