#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework2_2.py
# author:74049
# datetime:2021/5/17 21:41
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import socket

def sender():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    dest_addr = ('192.168.203.1', 8082)

    send_data = input("请输入要发送的数据:")

    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

    udp_socket.close()

    print("等待对方应答")

def receiver():

    # 绑定端口信息
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    local_addr = ('192.168.203.1', 8081)

    udp_socket.bind(local_addr)
    # 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024表示本次接收的最大字节数
    # 打印显示接收到的数据
    print("收到来自用户1信息:", recv_data[0].decode('gbk'))

    udp_socket.close()

if __name__ == '__main__':
    while(True):
        receiver()
        sender()