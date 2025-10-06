from os import listdir
from os.path import splitext
import random

IN = 'sets.txt'

sets = open(IN, 'r').read().split('\n')
drafted = [splitext(p)[0] for p in listdir('./') if splitext(p)[0] in sets]

for s in sets:
    mark = ' '
    if s in drafted:
        mark = 'X'
    print(f'[{mark}] {s}')

not_drafted = [s for s in sets if s not in drafted]
if len(not_drafted) == 0:
    print('\nAll sets drafted! Congrats!')
    exit(0)

print(f'\nSuggestion for next set to draft: {not_drafted[random.randint(0, len(not_drafted)-1)]}')
