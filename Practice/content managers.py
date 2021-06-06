class Filemanager:
    def __init__(self, file_name, mode = 'r'):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        self.file_obj = open(self.file_name, self.mode)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        self.file_obj.close()

with Filemanager('text.txt', mode = 'w') as file_obj:
    #raise TypeError('No world')
    file_obj.write('Good bye, cruel world')
# except TypeError:
#     pass


# try:
#     file_obj.open('text.txt', mode = 'w')
# finally:
#     file_obj.close()

from contextlib import contextmanager

@contextmanager
def file_open(file_name, mode= 'r')
    file_obj = open(file_name, mode = mode)
    try:
        yield file_obj
    finally:
        file_obj.close()

with file_open('text2.txt', mode = 'w') as file_o:
    file_o.write('erwerwerwer')
