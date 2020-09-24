import ft_len_num as f


def ft_null_count(a):
    n = f.ft_len_num(a)
    k = 0
    for i in range(n):
        if a % 10 == 0:
            k += 1
        a //= 10
    return k
