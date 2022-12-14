# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

from datetime import datetime


def screen(log, haveDateTime=False):
    if haveDateTime:
        now = datetime.now()
        log = ' [' + f'{now:%d/%m/%Y %H:%M:%S}' + '] ' + log
    else:
        log = ' ' + log
    print(log)


def file(log, haveDateTime=True):
    try:
        fn = 'run.log'
        f = open(fn, 'a')
        if haveDateTime:
            now = datetime.now()
            log = ' [' + f'{now:%d/%m/%Y %H:%M:%S}' + '] ' + log
        else:
            log = ' ' + log
        f.write(log + '\n')
        f.close()
        return True
    except:
        return False


def screen_n_file(log, haveDateTime=True):
    screen(log, haveDateTime)
    file(log, haveDateTime)
