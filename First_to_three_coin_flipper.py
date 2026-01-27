import random

name = 'Name: Nirvana Ayad'
print(f'{name:^40}')

flip_count = 0
consecutive = {"heads": 0, "tails": 0} #hash map for time complexity

while (consecutive["heads"] < 3) and (consecutive["tails"] < 3):
    result = "heads" if random.randint(0, 1) == 0 else "tails"
    consecutive[result] += 1
    consecutive["tails" if result == "heads" else "heads"] = 0
    flip_count += 1
    print(f'Flip: {flip_count} is {result}.')
    print(f'Heads in a row = {consecutive["heads"]:2}, tails in a row = {consecutive["tails"]:2}')

print(f'{result} won!')
