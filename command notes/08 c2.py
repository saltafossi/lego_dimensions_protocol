# 0x08 0xc2 - Immediately change the colour of one or all pad(s), fade and flash available
# Byte: use
# 0: Always 0x55
# 1: 0x08
# 2: 0xc2
# 3: Message counter
# 4: Pad all=0 c=1 l=2 r=3
# 5: ?change speed - needs more investigation
# 6: ?flash rate/count - fuzz to investigate?
# 8: green
# 9: blue
# 10: Checksum
# 11-31: Padding
[0x55, 0x08, 0xc2, 0x0b, 0x01, 0x03, 0x01, 0xf0, 0x00, 0x16, 0x35, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# c:pink
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0x03, 0x01, 0xf0, 0x00, 0x16, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# r:pink
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0x03, 0x01, 0xff, 0x00, 0x00, 52, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# r:red
# rgb
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x03, 0x01, 0xff, 0x00, 0x00, 50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x03, 0x01, 0x00, 0xff, 0x00, 50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:green
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x03, 0x01, 0x00, 0x00, 0xff, 50, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:blue
# fades and flashes:
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0xff, 0x01, 0xff, 0x00, 0x00, 46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# r:red slow fade in
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0xf0, 0x01, 0x03, 0x00, 0x16, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# r:blue slow fade in
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x01, 0xff, 0xff, 0x00, 0x00, 46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red rapid flash between red and prev color
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x00, 0xff, 0xff, 0x01, 0x00, 46, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red rapid flash between red and prev color, almost imperceptible
[0x55, 0x08, 0xc2, 0x0f, 0x03, 0x16, 0x01, 0x03, 0x00, 0xf0, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# r:blue qucik fade in
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x55, 0x01, 0xff, 0x00, 0x00, 132, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red fade from previous colour
[0x55, 0x08, 0xc2, 0x0f, 0x01, 0x01, 0x55, 0xff, 0x00, 0x00, 132, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# c:red rapid flash then solid red
[0x55, 0x08, 0xc2, 0x05, 0x01, 0x01, 0x06, 0x4c, 0x20, 0x00, 0x98, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]# Flash yellow quickly several times then return to previous colour