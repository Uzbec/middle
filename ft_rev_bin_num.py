from middle import ft_pow as pw, ft_len_num as f


def ft_rev_bin_num(a):
    kc = f.ft_len_num(a)
    k = 0
    for i in range(kc):
        k += a % 10 * pw.ft_pow(2, i)
        a //= 10
    return k
