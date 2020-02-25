#回环矩阵
SIZE = 7
array = [[0]*SIZE]
#创建一个二维表大小为
for i in range(SIZE-1):
    array += [[0]*SIZE]
#0123分别表示下右上左 这个也是回环矩阵的一个规律
orient = 0
j = 0
k = 0
for i in range(1,SIZE*SIZE+1):
    array[j][k] = i
    #向下走
    if (j == k-1) and (k <= SIZE/2):
        orient = 0
    #左右
    elif j+k == SIZE - 1:
        if j > k:
            orient = 1
        else:
            orient = 3
    #上
    elif (k == j) and (k >= SIZE/2):
        orient = 2
    #赋值
    #下右上左
    if orient == 0:
        j += 1
    if orient == 1:
        k += 1
    if orient == 2:
        j -= 1
    if orient == 3:
        k -= 1
for i in range(SIZE):
    for j in range(SIZE):
        print("%02d " % array[i][j], end="")
    print("")


#乘法表
for i in range(1,10):
    j=1
    for j in range(1,i+1):
        print(j,"X",i,"=",i*j,"\t",end ="")
    print("")

