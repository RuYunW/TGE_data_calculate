# This file is for reading DeepCom dataset

with open('./data/DeepCom/describe.txt', 'rb') as f_MTG:
    lines = f_MTG.readlines()
    sum = 0
    max_num = 0
    for line in lines:
        sum += len(str(line).split(' '))
        if len(str(line).split(' ')) > max_num:
            max_num = len(str(line).split(' '))
    print(sum)
    print(len(lines))
    print(sum/len(lines))
    print(max_num)



