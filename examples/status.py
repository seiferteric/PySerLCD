#!/usr/bin/python

from PySerLCD import lcd
import time
import psutil
import serial
import struct
import socket
import datetime
CMD_CMD        = 0xFE
CMD_CLEAR      = 0x01
CMD_INVERT     = 0x12
CMD_ON         = 0x0C
CMD_OFF        = 0x08
CMD_BOX_CUR_ON = 0x0D
CMD_BOX_CUR_OFF= 0x0C
CMD_UND_CUR_ON = 0x0E
CMD_UND_CUR_OFF= 0x0C
CMD_MOV_CUR_R  = 0x14
CMD_MOV_CUR_L  = 0x10
CMD_SCRL_R     = 0x1C
CMD_SCRL_L     = 0x18
CMD_SET_CUR_POS= 0x80


CONFIG_CONFIG  = 0x7C




l = lcd.Lcd("/dev/ttyUSB0", 9600)

l.write("Hello")


# time.sleep(1)
while True:
    l.clear()
    

    l.write(socket.gethostname())
    l.write(datetime.datetime.now().strftime(' %H:%M:%S'))
    l.set_cursor_pos(0,1)
    l.write("C:{}%".format(round(psutil.cpu_percent())))
    
    l.write("M:{}%".format(round(psutil.virtual_memory().percent)))
    
    l.write("D:{}%".format(round(psutil.disk_usage('/').percent)))
    time.sleep(0.5)
