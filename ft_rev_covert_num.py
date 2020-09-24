import ft_pow as pw
import ft_len_num as f


def ft_rev_covert_num(a, ss):
    kc = f.ft_len_num(a)
    k = 0
    for i in range(kc):
        k += a % 10 * pw.ft_pow(ss, i)
        a //= 10
    return k
