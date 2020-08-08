import os
import sys
from optparse import OptionParser
import socket
from queue import Queue
import threading
from datetime import datetime


# 参数
usage = "扫描主机端口"
p = OptionParser(usage = usage)

p.add_option("-n", help="指定并发数")
p.add_option("-f", help= "进行ping测试或者tcp测试")
p.add_option("--ip", help="ip")
p.add_option("-w", help="保存结果")
p.add_option("-v",help="打印耗时时间")

(opts, args) = p.parse_args()

# ping测试
def ipping(name,q,host):
    try:
        status = os.system("ping -c 1 %s" %host,shell=True,stdout=open('/dev/null','w'));
        if status == 0:
            print(f'{host}能被ping通')
        else:
            print(f'{host}不能被ping连接失败')
    except expression as e:
        print(e)
        
    
# 扫描端口
def scan(name, q, host):
    while True:
        try:
            if q.empty():
                break
            else:
                port = q.get()
                # print(f"扫描线程为{name},扫描端口为{port}，ip地址为{host}")
                s = socket.socket()
                s.settimeout(1)
                res = s.connect_ex((host,port))
                if res == 0:
                    print(f"host is {host} and {port} is open")
                    s.close()
                # else:
                #     print(f"{port} is close")
        except expression as e:
            print(e)

if __name__ == '__main__':
    # 队列
    scan_threads = []

    scanQueue = Queue(1000)
    for p in range(100):
        scanQueue.put(p)

    date1 = datetime.now()
    # 指定线程数
    num = int(opts.n)
    for thread_id in range(num):
        if opts.f=='ping':
            fdef = ipping
        elif opts.f=='tcp':
            fdef = scan
        t = threading.Thread(target=fdef,args=(thread_id,scanQueue,opts.ip))
        t.start()
        scan_threads.append(t)

    # 结束线程
    for t1 in scan_threads:
        t1.join()
 
    date2 = datetime.now() - date1 
    # 打印耗时时间
    if opts.v:
        print(f'线程数为{num}，扫描完耗时时间为{date2}')

