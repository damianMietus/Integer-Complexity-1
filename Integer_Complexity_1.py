# By Damian Mietus
# Reddit Daily Programmer
# Challenge #354 [Easy] Integer Complexity 1
# Completed May 9 2019

print("Input a number : ")

a = input()
a = int(a)
b = 0
c = 0
d = 0
tempb = 0
tempC = 0
tempD = 0
count = 1

while(count <= a):
    if(a%count == 0):      
        tempB = count
        tempC =  a/count
        tempD = tempB+tempC
        if(d == 0):
            d = tempD
            c = tempC
            b = tempB
        elif(tempD < d):
            d = tempD
            c = tempC
            b = tempB                                
    count = count+1
    
print("The sum of the smallest pair of factors is:", d, "\nthe factors are:", c, " + ", b)
input('Press ENTER to exit')
