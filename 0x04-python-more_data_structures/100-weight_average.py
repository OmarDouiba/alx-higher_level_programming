def weight_average(my_list=[]):
    som, div = 0, 0
    for i in my_list[:]:
        som += i[0] * i[1]
        div += i[1]
    return som / div
