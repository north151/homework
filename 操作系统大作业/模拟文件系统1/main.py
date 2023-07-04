import os

from folder import *
from file   import *


class FileSystem():
    def __init__(self,username="root",maxdisk=1024,maxflag=20):
        self.username = username                        # 系统用户名
        self.home = Folder(father=None, name=username)  # 系统主目录
        self.path = username                            # 当前绝对路径
        self.curfolder = self.home                      # 当前目录


    def clear(self):
        os.system("cls")

    def man(self):
        print("     系统操作     ")
        print("查询: man")
        print("清屏: clear")
        print("退出: exit\n")

        print("     目录操作     ")
        print("创建目录: mkdir [目录名]")
        print("删除目录: rmdir [目录名]:")
        print("显示目录: ls    [目录名](默认.)")
        print("切换目录: cd    [目录名](默认当前用户主目录)\n")

        print("     文件操作     ")
        print("创建文件: touch [文件名] [大小]")
        print("删除文件: rm    [文件名]")
        print("打开文件: stat  [文件名]")
        print("读取文件: cat   [文件名]")
        print("写入文件: echo  [写入内容] > [文件名]\n")



if __name__ == '__main__':
    print("进入模拟文件系统: ")
    username = input("请输入用户名: ")
    fs = FileSystem(username=username)

    while True:
        print(username + "@localhost:/" + fs.path, end="# ")
        order = input().strip().split(" ")

        # 创建目录
        if order[0] == "mkdir":
            try:
                mkdir(fs,order[1])
            except:
                print("格式错误: mkdir [目录名]")
        # 删除目录
        elif order[0] == "rmdir":
            try:
                rmdir(fs,order[1])
            except:
                print("格式错误: rmdir [目录名]:")
        # 显示目录
        elif order[0] == 'ls':
            try:
                ls(fs)
            except:
                print("格式错误: ls    [目录名](默认.)")
        # 切换目录
        elif order[0] == 'cd':
            try:
                order.append("~")
                cd(fs,order[1])
            except:
                print("格式错误: cd    [目录名](默认当前用户主目录)")

        # 创建文件
        elif order[0] == "touch":
            try:
                touch(fs,order[1])
            except:
                print("格式错误: touch [文件名]")
        # 删除文件
        elif order[0] == "rm":
            try:
                rm(fs,order[1])
            except:
                print("格式错误: rm    [文件名]:")
        # 读取文件
        elif order[0] == "cat":
            try:
                cat(fs,order[1])
            except:
                print("格式错误: cat   [文件名]")
        # 写入文件
        elif order[0] == "echo":
            try:
                echo(fs,order[1],order[3])
            except:
                print("格式错误: echo  [写入内容] > [文件名]\n")


        # 查看命令
        elif order[0] == "man":
            try:
                fs.man()
            except:
                print("格式错误: man")
        # 清屏
        elif order[0] == "clear":
            try:
                fs.clear()
            except:
                print("格式错误: clear")
        # 退出文件系统
        elif order[0][:4] == "exit":
            break

        else:
            print(order[0]+"不是正确的命令")

    print("退出模拟文件系统!")

