# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# Inpoot: 5 -> 1 0 1 1 0
# Outpoot: 2

from random import randint

coins = 5
side_of_coin = [randint(0, 1) for i in range(coins)]
print(f'{coins}  ->', *side_of_coin, sep=' ')
heads, tails = 0, 0
for i in range(coins):
    if side_of_coin[i] == 1:
        heads += 1
    else:
        tails += 1
if heads > tails:
    print(tails)
else:
    print(heads)
