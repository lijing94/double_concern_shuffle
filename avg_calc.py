import numpy as np
 
#
def max_of_abs(avg,*list_need_calc):
    abs_element1 = 0
    for key in list_need_calc:
        abs_tmp = abs(key - avg)
        if(abs_element1 < abs_tmp):
            abs_element1 = abs_tmp
    return abs_element1
#求平均数
def avg_calc(per_group_mouse_num,group_num,display=0,*data_result):
    liuzi_group_avg=0
    liuzi_group_avg_list = []
    weight_group_avg=0
    weight_group_avg_list = []
    mouse_num=0
    liuzi_avg  = 0
    weight_avg =0
    abs_element1 = 0
    abs_element2 = 0
    for key in data_result:   
        #print(key)
        liuzi_group_avg = key[4] + liuzi_group_avg
        weight_group_avg= key[1] + weight_group_avg
        weight_avg      = key[1] + weight_avg
        liuzi_avg       = key[4] + liuzi_avg
        mouse_num = mouse_num + 1
        if(mouse_num%per_group_mouse_num == 0):
            #print("===========liuzi:"+str(round(liuzi_group_avg/7,2))+"===================")
            liuzi_group_avg_list.append(round(liuzi_group_avg/per_group_mouse_num,2))
            liuzi_group_avg = 0
            weight_group_avg_list.append(round(weight_group_avg/per_group_mouse_num,2))
            weight_group_avg = 0
    #平均值
    liuzi_avg = liuzi_avg/(per_group_mouse_num*group_num)
    weight_avg= weight_avg/(per_group_mouse_num*group_num)
    # calc 方差
    variance = np.var(liuzi_group_avg_list)
    variance2= np.var(weight_group_avg_list)
    #标准差
    std      = np.std(liuzi_group_avg_list)
    std2     = np.std(weight_group_avg_list)
    #最大绝对值差
    abs_element1 = max_of_abs(liuzi_avg ,liuzi_group_avg_list )
    abs_element2 = max_of_abs(weight_avg,weight_group_avg_list)
    


    if display:
        print("=================result=================")
        print(str(liuzi_group_avg_list) +"因素1平均值"+str(round(liuzi_avg,2)))
        print(str(weight_group_avg_list)+"因素1平均值"+str(round(weight_avg,2)))
        print("因素1方差："+str(round(variance ,2))+"因素1标准差："+str(round(std ,2))+"因素1最大绝对值差："+str(round(abs_element1,2)))
        print("因素2方差："+str(round(variance2,2))+"因素2标准差："+str(round(std2,2))+"因素2最大绝对值差："+str(round(abs_element2,2)))

    if mouse_num != per_group_mouse_num*group_num :
        print("mouse_num not right! 一共有"+str(per_group_mouse_num*group_num)+"只，但是分组了"+str(mouse_num)+"只。")
    return variance,std,abs_element1