from typing import List


def create_array(x):
    #创建长度为10的数组，传入参数 i， 返回长度为 5 的数组，其中每个值为 i * index 
    raise NotImplementedError('方法未实现')


def lookup_num(nums: List[int], target: int)->List[int]:
    #给定一个整数数组 `nums` 和一个整数值 `target`, 请你找出在数组中找出为该值 `target` 的整数们，并返回它们的所有数组下标。
    raise NotImplementedError('方法未实现')

def plot_from_excel(filename: str):
    import matplotlib.pyplot as plt
    import pandas as pd
    df = pd.read_excel(filename)
    ## @TODO 从 dataframe 里读取两列信息， 一列为 ID， 一列为 Grade
    ## @Hint 可以用 print(df.head()) 查看 df 中存储的元素
    raise NotImplementedError("方法未实现")
    ## TODO
    # 显示图表
    plt.show()

def two_sum(nums: List[int], target: int)->List[int]:
    #给定一个整数数组 `nums` 和一个整数值 `target`, 请你找出在数组中找出为该值 `target` 的整数们，并返回它们的所有数组下标。
    raise NotImplementedError('方法未实现')
    
def check_even(num: int):
    return num % 2 == 0
    # raise NotImplementedError("方法未实现")