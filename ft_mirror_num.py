import ft_rev_num as rev, ft_len_num as f


def ft_mirror_num(a):
    if a < 0:
        a = -a
    n = f.ft_len_num(a)
    r = rev.ft_rev_num(a)
    k = 0
    if n == 1:
        return True
    for i in range(n):
        if a % 10 == r % 10:
            k += 1
        a //= 10
        r //= 10
    return True if k == n else False
