from global_val import *
from numpy import *
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

#保存到二维数组里面
def group_by_group_nums_to_2dims_list(group_num,per_group_mouse_num,*data_sorted):
    data_result = []
    data_result_tmp = []
    for i in range(0,group_num):
        data_result_tmp = []
        for j in range(0,per_group_mouse_num):
            num = i+j*group_num
            print(data_sorted[num])
            data_result_tmp.append(data_sorted[num][4])
        data_result.append(data_result_tmp)
    print_format_excel(*data_result)
    avg_row_calc_for_2dim_list(*data_result)
    return data_result

def avg_row_calc_for_2dim_list(*data_result):
    data_result_tmp = []
    m_avg = []
    for i in data_result:
        m_row = i
        sum = 0
        count = 0
        i.append(round(mean(i),2))
        data_result_tmp.append(i)
        for m in m_row:
            sum = sum + m
            count = count + 1
        print(data_result_tmp)
    print_format_excel(*data_result_tmp)

