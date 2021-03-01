import logging


def param_dec(file_name):

    def log(func):

        def wrapper_log(*args, **kwargs):
            name = func.__name__
            logger = logging.getLogger(name)
            logger.setLevel(logging.INFO)

            fh = logging.FileHandler(file_name)
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)

            logger.info('Вызываем функцию:%s' % name)
            logger.info(f'Аргументы: {args}, {kwargs}')
            res = func(*args, **kwargs)
            logger.info('Результат:%s' % res)
            return res
        return wrapper_log
    return log

@param_dec('param.txt')
def circle(r, pi):
    return pi*(r**2)

circle(5.5, pi=3.14)

