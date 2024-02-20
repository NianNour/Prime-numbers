# user input 
min_domain = int(input("Enter the min of your domian :"))
max_domain = int(input("Enter the max of your domian :"))
# an empty list to save prime numbers 
list_of_primes = []
# (min, ,max)
print(f"({min_domain}, {max_domain})")

# checking each number in our range 
# if they can be divided to the range of 2 to the previous number 
for i in range(min_domain + 1, max_domain + 1):
    for j in range(2, i):
        if i % j == 0:
            break
        if j == i - 1:
            list_of_primes.append(i)

print(list_of_primes)
