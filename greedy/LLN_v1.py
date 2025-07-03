n, m, k = 5, 8, 3

data = [6, 4, 2, 4, 5]

data.sort()
print(data)

big_d = data[-1]
sec_d = data[-2]

first_term = big_d * k + sec_d

result = (m // (k + 1)) * first_term + (m % (k + 1)) * big_d
print(result)