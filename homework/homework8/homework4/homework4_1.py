#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:homework4_1.py
# author:74049
# datetime:2021/5/6 21:39
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import socket
import multiprocessing

def sender():
    while True:
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        dest_addr = ('192.168.203.1', 56286)

        send_data = input("请输入要发送的数据:")

        udp_socket.sendto(send_data.encode('utf-8'), dest_addr)

        udp_socket.close()


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=sender())
    p1.start()
    p1.join()





