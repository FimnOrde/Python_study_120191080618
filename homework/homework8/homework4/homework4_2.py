#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4_2.py
# author:74049
# datetime:2021/5/8 11:49
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import socket
import multiprocessing

def receiver():
    while True:
        # 绑定端口信息
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        local_addr = ('192.168.203.1', 56286)

        udp_socket.bind(local_addr)
        # 接收数据
        recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
        # 打印显示接收到的数据
        print("收到信息:", recv_data[0].decode('gbk'))
        # print(recv_data[1])

        udp_socket.close()

if __name__ == '__main__':

    p2 = multiprocessing.Process(target=receiver())
    p2.start()
    p2.join()

