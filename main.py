# def my_max(x,y):
#     '''
#     获取两个数值之间较大的函数
#
#     my_max(x,y)
#
#     '''
#     # 定义一个变量z，该变量等于x,y中较大的值
#     z = x if x > y else y
#     # 返回变量z的值
#     return z
# # 使用 help() 函数查看 my_max()的帮助文档
# help(my_max)
# print(my_max.__doc__)
def sum_and_avg(list):
    sum = 0
    count = 0
    for e in list:
        if isinstance(e,int) or isinstance(e,float):
            count +=1
            sum += e
    return sum,sum/count
