from typing import TypeVar
_T = TypeVar("_T")
# Various ABCs mimicking those in collections.abc.
# _alias = _SpecialGenericAlias
# Iterable = _alias(collections.abc.Iterable, 1)
#加上编号1-10 
@staticmethod
def add_col_num_1to10(group_num,*data):
    num = 1 
    for key in data:
        key["nums_grp"] = num
        num = num + 1
        if num == group_num+1:
            num = 1
    return data


#加上编号
def add_nums(*data):
    num = 0
    for key in data:
        key["num"] = num
        num = num + 1
        #print(key)
