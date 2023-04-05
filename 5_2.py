def a():
    ls = [2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
    duplicate = {str(x) for x in ls if ls.count(x) > 1}
    x = lambda: print('nothing')
    y = lambda: print(' '.join(duplicate))
    x() if len(duplicate) < 1 else y()


a()
