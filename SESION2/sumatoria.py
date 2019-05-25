def sumatoria(num):

    """
    (int) -> int
    Calcula la sumatoria hasta el numero
    >>> sumatoria(10)
    55
    >>> sumatoria(5)
    15

    :param num: el alcance d ela sumatoria
    :return: el resultado de la sumatoria
    """
#     acumulador=0
#     for i in range(num+1):
#         acumulador+=1
#     return acumulador
    return (num * (num + 1)) // 2
# def sumatoria_v2(num):
#     return (num*(num+1))//2
