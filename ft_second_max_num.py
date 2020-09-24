import ft_max_num as maxx
import ft_len_num as f


def ft_second_max_num(a):
    n = f.ft_len_num(a)
    k = 0
    mm = maxx.ft_max_num(a)
    if a < 0:
        a = -a
    for i in range(n):
        if a % 10 == mm:
            a //= 10
            continue
        if k < a % 10:
            k = a % 10
        a //= 10
    return k
