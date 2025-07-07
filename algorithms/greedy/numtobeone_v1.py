n, k = map(int, input().split())

idx = 0

while True:
    tmp_n = (n // k) * k
    idx += n - tmp_n
    n = tmp_n

    if n < k:
        break

    idx += 1
    n //= k
    
idx += (n - 1)
print(f'steps: {idx}')