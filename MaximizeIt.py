import itertools
line = input('What are your dimensions? ')
K = int(line.split()[0])
M = int(line.split()[1])

lists = []
for i in range (K): 
    numbers = input().split()   
    numbers = [int(x) for x in numbers]
    elements = numbers[1:]
    lists.append(elements)

combinations = list(itertools.product(*lists)) 
s_max = 0
for arr in combinations:
    summation = 0
    for x in arr:
        summation += x**2
    thisMax = summation % M
    s_max = max(thisMax,s_max)
print(s_max)