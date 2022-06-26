import random
import time

base_damage = 100
chance_increase = 1/3
tier = 3 # 1 2 or 3 to denot 120, 200, or 350%
damage_increase = 0
num_attacks_this_round = 10000

for z in range(1, 4):
    tier = z
    print('tier' + str(tier))
    if tier == 1:
        damage_increase = 1.2 # 1.2 for 120%, 2.0 for 200%, 3.5 for 350%
    if tier == 2:
        damage_increase = 2 # 1.2 for 120%, 2.0 for 200%, 3.5 for 350
    if tier == 3:
        damage_increase = 3.5 # 1.2 for 120%, 2.0 for 200%, 3.5 for 350%
    print('damage increase: ' + str(damage_increase))
    cumulative_damage = 0
    number_hits = 0
    for i in range(0, num_attacks_this_round):
        this_hit = base_damage
        rand_num = float(random.randint(0, 100)/100)
        #print("rand num:" + str(rand_num)) # working now
        if rand_num <= chance_increase:
                this_hit *= damage_increase
        cumulative_damage += this_hit
        number_hits += 1
        average_damage = float(cumulative_damage / number_hits)
        #print('this hit:' + str(this_hit) + '\t avg this fight: ' + str(average_damage))
        if i % 1000 == 0:
            print('this hit:' + str(this_hit) + '\t avg this fight: ' + str(average_damage))
