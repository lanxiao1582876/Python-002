def amap(func, data):
    res = []
    for i in data:
        res.append(func(i))
    return res


def f_cheng(x):
    return x * x


def f_str(x):
    return str(x)


if __name__ == '__main__':
    # 1
    alist = [1, 3, 5, 7]
    print(amap(f_cheng, alist))

    # 2
    print(amap(f_str, alist))
