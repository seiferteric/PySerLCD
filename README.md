PySerLCD
========

Library to drive sparkfun SerLCD https://www.sparkfun.com/products/9067


Example:
--------

    from PySerLCD import Lcd
    
    l = Lcd('/dev/ttyUSB0', 9600)
    l.write("Hello World!")

