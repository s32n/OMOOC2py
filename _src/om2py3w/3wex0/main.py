# -*- encoding: utf-8 -*-
#! /usr/bin/env python
'''
文件说明： 这是个Net局域网版本的极简交互式笔记程序
作者信息： penguinjing
版本自述:  0.0.2
程序参考： https://pymotw.com/2/socket/udp.html
'''
# 全局引用
import socket
import sys
from os.path import exists

# 全局变量
# PATH = "/path/2/work dir"
# 函式撰写区

def print_usage():
    print 'no or wrong specify mode, please run it again.'
    print 'python main.py [s|c]'
    print '\t\t| |'
    print '\t\t| - client mode'
    print '\t\t- - server mode'

def print_help():
    print "?/h/H - print help"
    print "q/quit/bye - quit the Notes"
    print "r/sync - synchorme history notes"
    print "shutdown - shuting down the server"

def read_all_records():
    log_name = 'mydiary.log'
    if exists(log_name) == True:
        current_file = open(log_name)
        his_content = current_file.read()
        current_file.close()
    else:
        his_content = 'no historical notes'
    return his_content

def setupserver():
    # Echo Server programe part
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_address = socket.gethostbyname(socket.getfqdn())
    # Bind the socket to the port
    server_address = (local_address, 9009)
    print >>sys.stderr, 'starting up server on %s port %s' % server_address
    sock.bind(server_address)
    print >>sys.stderr, 'Hit Ctrl + C to interrupt'
    print >>sys.stderr, '\nwaiting to receive notes:'


    while True:
        data, address = sock.recvfrom(4096)
        #print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
      
        if data in ['r', 'sync']:
            content = read_all_records()
            sock.sendto(content, address)
            continue
        elif data == 'shutdown':
            print >>sys.stderr, '\nshuting down the server...'
            break
        else: 
            log_name = 'mydiary.log'
            current_file = open(log_name, 'a+')
            print >>sys.stderr, data
            current_file.write(data+'\n')
            current_file.close()

    print >>sys.stderr, 'closing socket'
    sock.close()

def setupclient():
    # Echo client program part
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
    address = raw_input('Please input Notes server address:')

    server_address = (address, 9009)
    while True:
        message = raw_input('>>>' )    
        if message in ['r', 'sync']:
            sock.sendto(message, server_address) 
            data, server = sock.recvfrom(4096)
            print >>sys.stderr, data
            continue
        elif message in ['?', 'h', 'H']:
            print_help()
            continue
        elif message in ['q', 'quit', 'bye']:
            break
        elif message =='':
            continue
        else: 
            sock.sendto(message, server_address) 
    print >>sys.stderr, 'closing socket'
    sock.close()

def main(): 
    if len(sys.argv) == 1:
        print_usage()
    elif sys.argv[1] == 'c':
        setupclient()
    elif sys.argv[1] == 's':
        setupserver()
    else:
        print_usage()
        
# 自检区
if __name__ == "__main__": 
    main()