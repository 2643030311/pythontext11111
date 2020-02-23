def divide(num):
    integer = int(num)#整数部分
    fraction = round((num-integer)*100)#两位小数部分
    return str(integer), str(fraction)

han_list = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"] #0——9 对应的中午读法
unit_list = ['十','百','千']
unitfa_list = ["角","分"]
def four_to_hanstr(num_str):
    result = ""
    num_len = len(num_str) #输入字符串的长度
    for i in range(num_len):
        num = int(num_str[i])
        if i != num_len - 1 and num != 0:
            result += han_list[num] + unit_list[num_len-2-i]
        else:
            result += han_list[num]
    return result
def integer_to_str(num_str):
    str_len = len(num_str)
    if str_len > 12:
        print("太大了哦暂时翻译不了")
    elif str_len > 8:
        return four_to_hanstr(num_str[:-8])+ "亿" + four_to_hanstr(num_str[-8:-4]) + "万" + four_to_hanstr(num_str[-4:] )
    elif str_len > 4:
        return four_to_hanstr(num_str[:-4]) + "万" + four_to_hanstr(num_str[-4:])
    else:
        return four_to_hanstr(num_str)
def fraction_to_hanstr(fa):
    result = ""
    for i in range(0,2):
        num = int(fa[i])
        result += han_list[num] + unitfa_list[i]
    return result
def fraction_to_str(fa):
   return fraction_to_hanstr(fa)
num = float(input("请输入钱数\n"))
integer1, fraction1 = divide(num)
if int(fraction1) == 0:
    print(integer_to_str(integer1))
else:
    print(integer_to_str(integer1)+fraction_to_str(fraction1))
print(integer1,fraction1)
