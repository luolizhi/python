#!/usr/bin/env python3
# encoding=utf-8

import os
from subprocess import call  # 通过call调用shell命令
from subprocess import check_call  # 通过check_call调用检查返回值，成功返回0，否则-1
#import subprocess   #管理子进程

def compile_tcore():

    tcore = os.getenv("Tcore")  # jenkins传递的参数#这里是不同项目的名称
    # print('tcore='+tcore)
    print('!!!----开始编译'+tcore+'-----')
    workspace = os.getenv("WORKSPACE")  # jenkins在该job的工作目录
    # print('workspace='+workspace)
    trunck_src = "/home/jenkins/jenkins/trunk/src/"  # svn checkout 根目录目录
    dest_export_dir = "/home/jenkins/tools/"  # 编译生成的export-user_ta存放的目录
    compile_path = trunck_src + tcore  # 编译tcore的目录，执行make的目录
    print("编译目录compile_path=" + compile_path)
    if os.listdir(workspace):
        print("----工作空间不为空，删除文件----")
        check_call("rm " + " -r " + workspace + "/*", shell=True)
    check_call("chmod -R 777 " + compile_path, shell=True)
    check_call("cd " + compile_path + " && " + "  make clean ", shell=True)
    check_call("cd " + compile_path + " && " + "  make ", shell=True)
    print("----Makefile执行完成----")
    check_call("cp " + compile_path + "/*.bin  " + workspace, shell=True)
    print("----复制.bin文件完成----")
    if os.path.exists(dest_export_dir + "/export-user_ta"):
        print('----删除以前的export-user_ta----')
        check_call("rm " + " -r " + dest_export_dir + "/export-user_ta", shell=True)

    check_call("cp " + " -r " + compile_path + "/out/arm32-plat-mediatek/export-user_ta  " + dest_export_dir,
               shell=True)
    print("----复制export-user_ta文件夹完成----")
    check_call(
        "tar" + " cf " + workspace + "/export-user_ta.war " + compile_path + "/out/arm32-plat-mediatek/export-user_ta",
        shell=True)
    print("----打包export-user_ta.war完成----")
    print('!!!-----' + tcore + '编译完成-----')



def main():
    check_call(["whoami"])
    check_call(["pwd"])
    compile_tcore()


if __name__ == '__main__':
    main()
    print('--------ALL OK----------')
