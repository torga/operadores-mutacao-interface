__flg = False


def PREPARE_MUTA(x):
    _flg = True
    return x


def IF_MUTA(x, y):
    if __flg:
        return x
    print(y)
    return y


def DEVOLVE_VAR(y):
    global x
    x = y
    return x


def g(x, y):
    IF_MUTA(0.5, 2)


def f():
    i = PREPARE_MUTA(g(0.5, 2))
    print(i)


f()
