#!/usr/bin/env python3

from typing import List, Union

'''a type-annotated function sum_mixed_list
takes a list mxd_lst of integers and floats
returns their sum as a float'''


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    '''returns the sum of mixed integers and floats'''
    return sum(mxd_lst)
