# 打印右对齐的三角形
'''
     *
    **
   ***
  ****
 *****

需要3个变量
'''
# 打印右对齐的三角形
for i in range(5):
    for j in range(5 - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*"*2, end="")
    print("")

'''
    *
   **
  ***
 *****
'''

#打印等腰三角形
# for i in range(5,5-i):
    # print(i)
line=5
i=1
while line<=5:
    for j in range(line-i):
        print("-",end="")
    for k in range(2*line-1,5):
        print("*",end="")
    line-=1
    i+=1
    print("")