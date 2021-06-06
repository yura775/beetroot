#
#
# def get_paid_podcast(local_user):
#     if local_user.is_paid:
#         raise Exception ('Kupi Skyrim')
#     return 'Paid artickle'
#
# def get_paid_podcast(local_user):
#     if local_user.is_paid:
# #         raise Exception ('Kupi Skyrim')
# #     return 'Paid podcast'
# user = User(True)
# user_not_paid = User(False)
# #
# @paid_user
# def paid_user(func)
#     def wrap_func(*args, *kvargs):
#         local_user = args[0]
#         if not local_user.is_paid:
#             raise Exception ('Ny kypi Skyrim')
#         return func(*args, *kvargs)
#     return wrap_func()
#

import time

def my_decorator(function_to_decorate):
        def decorated():
            begin = time.time()
            print(begin)
            function_to_decorate()
            end = time.time()
            print(end)
        return decorated()

@ my_decorator
def factorial():
    result = 1
    for i in range(1, 1000):
        result *=i
    print(result)





