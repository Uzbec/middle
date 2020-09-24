import ft_max_num as maxx
import ft_second_max_num as smm
import ft_min_num as mim


def ft_second_simple_max_num(a):
    m = maxx.ft_max_num(a)
    sm = smm.ft_second_max_num(a)
    mi = mim.ft_min_num(a)
    return sm if sm != mi else -1
