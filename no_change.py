import random

# 1 -> car
# 0 -> goat

choice = [1,0,0]
win = 0.0

NUMBER_OF_SIMULATION = 10_000

for i in range(NUMBER_OF_SIMULATION):
    random.shuffle(choice)   # put prize on random place

    #print(choice)

    # allways first
    c = 0
    # random select
    c = random.randint(0, 2)

    if choice[c] == 1:
        #print('WIN')
        win += 1
    else:
        #print('LOSE')
        pass

win_percent = win / NUMBER_OF_SIMULATION * 100
lose = NUMBER_OF_SIMULATION - win
lose_percent = 100 - win_percent

print('#################################')
print('State | Number of games | Percent')
print('Win   |         {:7.0f} |  {:.2f}%'.format(win, win_percent) )
print('Lose  |         {:7.0f} |  {:.2f}%'.format(lose, lose_percent) )
print('---------------------------------')
print('SUM   |         {:7.0f} | {:.2f}%'.format(NUMBER_OF_SIMULATION, 100) )
