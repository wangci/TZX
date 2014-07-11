#!/usr/bin/python
#coding=utf-8
import os
import sys
import getopt
import string
def Querylog():
    sType=raw_input("选择需要查找全部日志还是最新日志:[a]表示全部,[n]表示最新  ")
    sGateway=raw_input("选择需要查找的网关:[a]表示农行,[i]表示工行,[o]表示其他  ")
    sDate=raw_input("选择需要查询的日志日期,格式如:20140608  ")
    sId=raw_input("请输入退款id号： ")
    print os.path.abspath(os.curdir)
    if sType=="a":
            os.chdir("/home/logs/resin-payments-admin/log-all")
    else:
            os.chdir("/home/logs/resin-payments-admin/log-new")
    print os.path.abspath(os.curdir)
    if sGateway=="a":
            os.chdir("10.120.83.196")
    elif sGateway=="i":
            os.chdir("10.110.10.146")
    else:
            os.chdir("10.120.82.56")
    sTmpdir=os.getcwd()
    print os.path.abspath(os.curdir)
    print sTmpdir
    
    sYear=sDate[0:4]
    sMonth=sDate[4:6]
    sDay=sDate[6:8]
    
    
    if sType=="n":
        sTmp1=raw_input("选择查询历史备份数据还是当天新生成数据:[b]历史数据,[n]新生成数据")
        if sTmp1=="b":
            os.chdir(sTmpdir+"/payment_log/admin-log/backup")
        else:
            os.chdir(sTmpdir+"/admin-log")
    elif sMonth=="01":
        os.chdir(sTmpdir+"/2014-01")
    elif sMonth=="02":
        os.chdir(sTmpdir+"/2014-02")
    elif sMonth=="03":
        os.chdir(sTmpdir+"/2014-03")
    elif sMonth=="04":
        os.chdir(sTmpdir+"/2014-04")
    elif sMonth=="05":
        os.chdir(sTmpdir+"/2014-05")
    elif sMonth=="06":
        os.chdir(sTmpdir+"/2014-06")
    elif sMonth=="07":
        os.chdir(sTmpdir+"/2014-07")
    elif sMonth=="08":
        os.chdir(sTmpdir+"/2014-08")
    elif sMonth=="09":
        os.chdir(sTmpdir+"/2014-09")
    elif sMonth=="10":
        os.chdir(sTmpdir+"/2014-10")
    elif sMonth=="11":
        os.chdir(sTmpdir+"/2014-11")
    elif sMonth=="12":
        os.chdir(sTmpdir+"/2014-12")
    else:
        print "not corrent input!"
    print os.path.abspath(os.curdir)
    #拼接查找命令
    sCmdorder='zgrep -a '+'"'+sId+'"'+' payments_admin.log.'+sYear+'-'+sMonth+'-'+sDay+'.gz'
    print sCmdorder
    #执行查找命令
    os.system(sCmdorder)
if __name__ == "__main__":
    try:
        Querylog()
        print("please exit, log again!!!\n")
        os.system("sleep 1")
except OSError:
    print '输入的日期日志不存在，请检查'  
