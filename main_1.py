import logging

def log(func):

    def wrapper_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)

        fh = logging.FileHandler("%s.log" % name)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)

        logger.info('Вызываем:%s' % name)
        logger.info(f'Аргументы: {args}, {kwargs}')
        res = func(*args, **kwargs)
        logger.info('Результат:%s' % res)
        return res
    return wrapper_log

@log
def circle(r, pi):
    return pi*(r**2)

circle(15, pi=3.14)
# result = circle(15, pi=3.14)
# print(result)
