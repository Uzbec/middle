from middle import ft_mirror_num as mir


def ft_mirror_count(a):
    sc = 0
    for i in range(1, a + 1):
        if mir.ft_mirror_num(i):
            sc += 1
    return sc
