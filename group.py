from global_val import *
import numpy as np
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
    print("num i j data_sorted[num]")
    for i in range(0,per_group_mouse_num): #colums
        data_result_tmp = []
        for j in range(0,group_num):     #rows
            num = j+i*group_num
            print(num,i,j,str(data_sorted[num]))
            data_result_tmp.append(data_sorted[num][4])
        if(i%2):
            data_result_tmp = sorted(data_result_tmp,reverse=True)
        data_result.append(data_result_tmp)
    print_format_excel(*data_result) 
    #data_result = np.rot90(data_result,-1)
    #print_format_excel(*data_result)
    avg_row_calc_for_2dim_list(group_num,*data_result)
    return data_result

def avg_row_calc_for_2dim_list(group_num,*data_result):
    data_result_tmp = []
    row_avg_2_float = []
    row_abs_to_avg_all = []
    avg_all = 0
    data_result_flatten = []

    for i in data_result:
        data_result_tmp.append(i)
        m_round = np.mean(data_result,axis=0)
    for i in m_round:
        n = round(i,2)
        row_avg_2_float.append(n)
    data_result_tmp.append(row_avg_2_float)
    data_result_flatten = list(np.array(data_result_tmp).flatten())
    avg_all = np.mean(data_result_flatten)
    for r in row_avg_2_float:
        row_abs_to_avg_all.append(round(abs(r-avg_all),2))
    data_result_tmp.append(row_abs_to_avg_all)
    
    print_format_excel(*data_result_tmp)
    print("方差:"+str(round(np.var(row_avg_2_float),2))+"最大绝对值:"+str(max(row_abs_to_avg_all)))

