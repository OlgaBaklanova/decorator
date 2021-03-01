import logging
import json
import hashlib

class My_iterator:

    def __init__(self, file_name: str):
        self.start = -1
        with open(file_name, 'r', encoding='utf8') as file:
            self.countries = json.load(file)

    def __iter__(self):
        return self

    def __next__(self):
        self.start += 1
        if self.start == len(self.countries):
            raise StopIteration
        return self.countries[self.start]['name']['common']



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
            res = func(*args, **kwargs)
            logger.info('Результат:%s' % res)
            return res
        return wrapper_log
    return log

# def circle(r, pi):
#     return pi*(r**2)
#
# circle(5.5, pi=3.14)

if __name__ == '__main__':
    list_countries = My_iterator('countries.json')
    with open('result.txt', 'w', encoding='utf8') as file:
        count = 0
        for country in list_countries:
            count += 1
            file.write(f'{country} - https://ru.wikipedia.org/wiki/{country.replace(" ", "_")}\n')


@param_dec('result.txt')
def LineReader(filename: str):

    with open(filename, 'r', encoding='utf8') as my_file:
        while True:
            line = my_file.readline()
            if line:
                yield hashlib.md5(line.encode('utf8')).hexdigest()
            else:
                break


# for item in LineReader('result.txt'):
#     print(item)