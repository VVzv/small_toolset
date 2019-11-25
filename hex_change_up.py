#!/usr/bin/python
# -*- coding:utf-8 -*-
# __Author__: VVzv

import sys
import binascii


try:
    cmd = sys.argv[1]
    if 'x' in cmd:
        if '0x' in cmd:
            cmd = cmd.split('0x')[-1]
            hex_de = binascii.a2b_hex(cmd)
            print('\033[36m"0x%s"hex解码为:"%s"\033[0m' %(cmd, hex_de.decode('utf-8')))
        else:
            if '\\' in cmd:
                c = cmd.split('\\')
                re = [binascii.a2b_hex(c.split('x')[-1]) for c in c[1:]]
                b_text = b''
                for b in re:
                    b_text += b
                print('\033[36m"%s"hex解码为(为b引号包裹的内容):"%s"\033[0m' % (cmd, b_text))
            else:
                c = cmd.split('x')[1:]
                re = [binascii.a2b_hex(c) for c in c]
                b_text = b''
                for b in re:
                    b_text += b
                print('\033[36m"%s"hex解码为(为b引号包裹的内容):"%s"\033[0m' % (cmd, b_text))
    else:
        splist = [('\\r', b'\r'), ('\\n', b'\n'), ('\\t', b'\t'), ('\\f', b'\f'), ('\\a', b'\a'), ('\\b', b'\b'), ('\\v', b'\v')]
        if '\\' in cmd and len(cmd) >1:
            for spstr in splist:
                if spstr[0] in cmd:
                    r_cmd = cmd
                    r_cmd0 = cmd
                    r_cmdx = cmd
                    hex_sp_dict0 = {sp[0]: binascii.b2a_hex(sp[1]).decode('utf-8') for sp in splist}
                    hex_sp_dictx = {sp[0]: '\\x' + (binascii.b2a_hex(sp[1])).decode('utf-8') for sp in splist}
                    ss_en_list0 = [(k, v) for k, v in hex_sp_dict0.items()]
                    ss_en_listx = [(k, v) for k, v in hex_sp_dictx.items()]
                    max_num = len(ss_en_listx)
                    text_en0 = []
                    text_enx = []
                    count = 0
                    cmd_en0 = ''
                    cmd_enx = ''
                    for ss_en in ss_en_listx:
                        cmd  = cmd.replace(ss_en[0], '')
                        count += 1
                        if count == max_num:
                            for i in cmd:
                                i_en = binascii.b2a_hex(bytes(i, 'utf-8'))
                                cmd_en0 += i_en.decode('utf-8')
                                cmd_enx += '\\x' + i_en.decode('utf-8')
                                text_en0.append((i, i_en.decode('utf-8')))
                                text_enx.append((i, '\\x' + i_en.decode('utf-8')))
                    ss_en_list0.extend(text_en0)
                    ss_en_listx.extend(text_enx)
                    for en0 in ss_en_list0:
                        if en0[0] in r_cmd0:
                            r_cmd0 = r_cmd0.replace(en0[0], en0[1])
                    for enx in ss_en_listx:
                        if enx[0] in r_cmdx:
                            r_cmdx = r_cmdx.replace(enx[0], enx[1])
                    hex_en0 = '0x' + r_cmd0
                    print('\033[36m"%s"0x格式hex编码为:"%s"\033[0m' %(r_cmd, hex_en0))
                    print('\033[36m"%s"\\x格式hex编码为:"%s"\033[0m' %(r_cmd, r_cmdx))
                    break
        else:
            hex_en1 = b'0x' + binascii.b2a_hex(bytes(cmd, 'utf-8'))
            hex_en2 = ''
            for i in cmd:
                hex_en2 += (b'\\x' + binascii.b2a_hex(bytes(i, 'utf-8'))).decode('utf-8')
            print('\033[36m"%s"0x格式hex编码为:"%s"\033[0m' % (cmd, hex_en1.decode('utf-8')))
            print('\033[36m"%s"\\x格式hex编码为:"%s"\033[0m' % (cmd, hex_en2))

except Exception as e:
    print('str encode to hex:python3 hex_change.py abc')
    print('hex decode to str:python3 hex_change.py 0x616263')
    print('\033[31mError：%s\033[0m' %str(e))

