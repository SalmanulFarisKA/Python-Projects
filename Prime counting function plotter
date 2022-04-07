import matplotlib.pyplot as plt

ran = 100000

x = []

for i in range(0, ran+1):
    x.append(i)

y = [0, 0, 1]

primes = [2]

prime_count = 1

for i in range(3, ran+1):
    
    prime = True
    
    for j in primes:
        if i%j == 0:
            prime = False
            
    if not prime:
        y.append(prime_count)
            
    if prime:
        primes.append(i)
        prime_count += 1
        y.append(prime_count)
        
    i+=1

print(x)
print("length of x", len(x))
print(y)
print("length of y", len(y))

 
# plotting the points
plt.plot(x, y)
 
# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

plt.ylim(0, ran)
 
# giving a title to my graph
plt.title('My first graph!')
 
# function to show the plot
plt.show()
