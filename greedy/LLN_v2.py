# n, m, k = input().split(' ')
n, m, k = 5, 8, 3

# data = list(map(int, input().split(' ')))
data = [6, 4, 2, 4, 5]

data.sort()
print(data)

idx_m = 0
result = 0

while(1):
    for i in range(k):
        if idx_m == m:
            break
        big_d = data[-1]
        result += big_d
        idx_m += 1
        
    if idx_m == m:
        break        
    big_d = data[-2]
    result += big_d
    idx_m += 1
    
print(result)