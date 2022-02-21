import random
coin = ['head', 'tails']

print(random.choice(coin))

#programa de un volado 

if random.choice(coin) == 'head':
    print('head')
else:
    print("tails")
