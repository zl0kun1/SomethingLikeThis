# Auto Almost Everything
# Youtube Channel https://www.youtube.com/c/AutoAlmostEverything
# Please read README.md carefully before use

import glob, os, random


def get():
    # os.path.abspath(os.path.dirname(__file__))
    # os.path.join(PROJECT_ROOT, "Wordlist")
    # os.chdir('/Users/hungnguyen/Desktop/Desktop/test/PreSearch/Wordlist')
    os.chdir(os.path.join(os.getcwd(), "Wordlist"))
    dicts = glob.glob('*.txt')
    wordlist = []
    for dict in dicts:
        f = open(dict, 'r', encoding='utf8')
        for line in f:
            wordlist.append(line.strip())
    os.chdir('..')
    return wordlist


def gen(wordlist):
    return ' '.join([wordlist[random.randint(0, len(wordlist))] for j in range(random.randint(1, 3))])
