from middle import ft_len_num as f


def ft_max_num(a):
    n = f.ft_len_num(a)
    k = 0
    if a < 0:
        a = -a
    for i in range(n):
        if k < a % 10:
            k = a % 10
        a //= 10
    return k
