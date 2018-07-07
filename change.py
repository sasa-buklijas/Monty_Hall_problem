import random

# 1 -> car
# 0 -> goat

choice = [1, 0, 0]
win = 0.0   # as float, to have decimal places

NUMBER_OF_SIMULATION = 10_000

for i in range(NUMBER_OF_SIMULATION):
    random.shuffle(choice)

    #print(choice)

    user_index = 0   # 0 is first
    user_index = random.randint(0, 2)   # or random

    # find where is 1 (car)
    car_index = choice.index(1)

    #print('user_index %d, car_index %d' % (user_index, car_index) )
    
    # available indexes
    available_indexes = [0, 1, 2]
    available_indexes.remove(user_index)
    if car_index != user_index:
        available_indexes.remove(car_index)
        
    index_to_open = random.choice(available_indexes)
    #print('index_to_open %d' %(index_to_open) )

    index_to_switch = [0, 1, 2]
    index_to_switch.remove(user_index)
    index_to_switch.remove(index_to_open)
    index_to_switch = index_to_switch[0]
    #print('index_to_switch %s' % (index_to_switch) )
        
    # check result
    if choice[index_to_switch] == 1:
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
