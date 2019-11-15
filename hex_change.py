#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import sys
import binascii

try:
    cmd = sys.argv[1]
    if '0x' in cmd:
        cmd = cmd.strip('0x')
        hex_de = binascii.a2b_hex(cmd)
        print("\033[36m'%s'hex解码为:'%s'\033[0m" %(cmd, hex_de.decode('utf-8')))
    else:
        hex_en = b'0x' + binascii.b2a_hex(bytes(cmd,'utf-8'))
        print("\033[36m'%s'hex编码为:'%s'\033[0m" %(cmd, hex_en.decode('utf-8')))
except:
    print('\033[31mstr encode to hex:python3 hex_change.py abc')
    print('hex decode to str:python3 hex_change.py 0x616263\033[0m')


