import sys, warnings
if sys.version_info[0] < 3:
    warnings.warn('Дл выполнения этой программы необхадима как минимум версия Python 3.0', RuntimeWarning)
else:
    print('Нормальное продолжение.')
