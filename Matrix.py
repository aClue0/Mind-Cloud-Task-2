import re

first_multiple_input = input('What are your dimenstions? ').rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

matrix = []
t = []
for i in range(n):
    matrix_item = [x for x in input('Fill matrix With : ')]
    matrix.append(matrix_item)
    
for j in range(m):  # columns 
    for i in range(n):  # then rows
        t.append(matrix[i][j])

s = ''.join(t)

path = re.compile(r'[ !@#$%&]+', re.M)
k = re.sub(path, ' ', s)
print(k)