import random
data_result = []
#shuffle，按正序基础上打乱
def shuffle_by_group(per_group_mouse_num=0,*data_before_shuffle):
    data_shuffle = []
    data_shuffle_tmp = []
    seris_num = 0
    for key in data_before_shuffle:
        data_shuffle_tmp.append(key)
        if (seris_num+1)%per_group_mouse_num == 0:
            random.shuffle(data_shuffle_tmp)
            data_shuffle = data_shuffle_tmp + data_shuffle
            data_shuffle_tmp = []
        seris_num = seris_num +1
    return data_shuffle
    


    
