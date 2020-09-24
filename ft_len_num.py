def ft_len_num(n):
    if n < 0:
        n = -n
    i = 0
    while n > 9:
        n = n // 10
        i += 1
    return i + 1
