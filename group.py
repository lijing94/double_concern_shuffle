#按分组数进行分组
def group_by_group_nums(group_num,per_group_mouse_num,*data_sorted):
    data_result = []
    debug_count = 0
    for i in range(0,group_num):
        seris_num=0
        debug_count=0
        for key in data_sorted:
            if (seris_num+i)%group_num == 0:
               data_result.append(key)
               debug_count = debug_count+1
               #print(debug_count)
            seris_num = seris_num +1
            
    return data_result
