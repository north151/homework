"""
进程: P1,P2,P3,P4,P5
资源: A:10, B:5, C:7
"""
# 最大资源
max_source = [10,5,7] 

# 最大需求
max = [[7,5,3],
       [3,2,2],
       [9,0,2],
       [2,2,2],
       [4,3,3]]

# 已满足需求
allocation = [[0,1,0],
              [2,0,0],
              [3,0,2],
              [2,1,1],
              [0,0,2]]

# 剩余需求
need = []
for i in range(5):
    t = [x-y for x,y in zip(max[i],allocation[i])]
    need.append(t)     

# 剩余资源
available = [0,0,0]
for i in range(5):
    available[0]+=allocation[i][0]
    available[1]+=allocation[i][0]
    available[2]+=allocation[2][0]



# 安全顺序
visted_pid = []
# 访问记录
visted = [False,False,False,False,False]
# 全部安全顺序
safeMatrix = []


def safe_pid(i):

    #  全部进程都访问完成,输出结果
    if len(visted_pid) == 5:
        print(visted_pid)
        return 
    
    # 该进程需求小于剩余资源
    if need[i][0]<=available[0] and need[i][1]<=available[1] and need[i][2]<=available[2]:
        # 暂记下一个为该进程
        visted_pid.append(i)
        # 该进程已访问
        visted[i] = True
        print(visted_pid)

        #  全部进程都访问完成,输出结果
        if len(visted_pid)==5:
            #print(visted_pid)
            print(visted)
            # 记录下访问此种顺序
            safeMatrix.append(str(visted_pid))

        # 更新剩余资源
        available[0] = available[0] + allocation[i][0]
        available[1] = available[1] + allocation[i][1]
        available[2] = available[2] + allocation[i][2]

        for j in range(len(need)):
            # 已访问
            if j in visted_pid:
                continue
            # 递归访问下一个
            else:
                safe_pid(j)
        
        # 回溯找下一种顺序
        t = visted_pid.pop()
        visted[t] = False
        available[0] = available[0] - allocation[t][0]
        available[1] = available[1] - allocation[t][1]
        available[2] = available[2] - allocation[t][2]

    return 




def apply():
    Pid = input("请求的进程(P0~P5): ")
    Pn = int(Pid[1])
    XA = int(input("请求资源A数目: "))
    XB = int(input("请求资源B数目: "))
    XC = int(input("请求资源C数目: "))

    f = open("banker.txt","a",encoding="utf-8")
    f.write("请求进程号: "+Pid+"\n")
    f.write("请求资源数: "+"资源A: "+str(XA)+"    资源B: "+str(XB)+"    资源C: "+str(XC)+"\n")

    # 超出需求
    if (XA + allocation[Pn][0] > max[Pn][0] or XB + allocation[Pn][1] > max[Pn][1] or XC + allocation[Pn][2] > max[Pn][2]) :
        print('超出需求资源,请求失败!')
        f.write('超出需求资源,请求失败!\n\n\n\n')
    # 超出剩余
    elif (XA > (available[0])) or (XB > available[1]) or (XC > available[2]):
        print("超出剩余资源,请求失败!")
        f.write('超出剩余资源,请求失败!\n\n\n\n')
    # 满足要求
    else:
        # 更新剩余需求
        need[Pn][0] = need[Pn][0] - XA
        need[Pn][1] = need[Pn][1] - XB
        need[Pn][2] = need[Pn][2] - XC
        
        # 更新占有资源
        allocation[Pn][0] = allocation[Pn][0]+XA
        allocation[Pn][1] = allocation[Pn][1]+XB
        allocation[Pn][2] = allocation[Pn][2]+XC
        # 更新剩余资源
        available[0] = available[0] - XA
        available[1] = available[1] - XB
        available[2] = available[2] - XC
        
        available2 = available[:]
        # 开始检测
        for i in range(len(need)):
            safe_pid(i)
            print("\n\n\n")
        available[:] = available2[:]

        # 存在安全顺序
        if len(safeMatrix) != 0 :
            print("全部安全顺序: ")
            f.write("全部安全顺序:\n")
            for i in safeMatrix:
                print(i)
                f.write(i+"\n")
            print("请求成功!")
            f.write("请求成功!\n\n\n\n")

        # 不存在安全顺序
        else:
            need[Pn][0] = need[Pn][0] + XA
            need[Pn][1] = need[Pn][1] + XB
            need[Pn][2] = need[Pn][2] + XC
            allocation[Pn][0] = allocation[Pn][0] - XA
            allocation[Pn][1] = allocation[Pn][1] - XB
            allocation[Pn][2] = allocation[Pn][2] - XC
            available[0] = available[0] + XA
            available[1] = available[1] + XB
            available[2] = available[2] + XC
            print("请求失败!")
            f.write("请求失败!\n\n\n\n")
    
    f.close()
    return 

apply()