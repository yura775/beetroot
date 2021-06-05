
rlist=['some', 'list', 'of', 'words']
i=5
def oops (wrong_index):
    try: rlist[wrong_index]
    except IndexError:
        print('ooops, something went wrong')
oops(i)


