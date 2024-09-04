import datetime

def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            log_entry = (
                f"Дата и время: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Имя функции: {old_function.__name__}\n"
                f"Аргументы: args={args}, kwargs={kwargs}\n"
                f"Вывод: {result}\n"
                f"{'-'*40}\n"
            )
            with open(path, 'a') as log_file:
                log_file.write(log_entry)
            return result
        return new_function
    return __logger

class FlatIterator:
    @logger('flat_iterator.log')
    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.flat_list = []
        self.index = 0
        for sublist in self.list_of_list:
            self.flat_list.extend(sublist)

    @logger('flat_iterator.log')
    def __iter__(self):
        self.index = 0
        return self

    @logger('flat_iterator.log')
    def __next__(self):
        if self.index < len(self.flat_list):
            item = self.flat_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

def test_1():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

if __name__ == '__main__':
    test_1()