#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      User
#
# Created:     16/11/2015
# Copyright:   (c) User 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import usb.core
import usb.util
import time

# find our device
dev = usb.core.find(idVendor=0x0e6f)# 0x0e6f Logic3 (made lego dimensions portal hardware)

# was it found?
if dev is None:
    raise ValueError('Device not found')

# set the active configuration. With no arguments, the first
# configuration will be the active one
dev.set_configuration()

# Initialise portal
print dev.write(1, [0x55, 0x0f, 0xb0, 0x01, 0x28, 0x63, 0x29, 0x20, 0x4c, 0x45, 0x47, 0x4f, 0x20, 0x32, 0x30, 0x31, 0x34, 0xf7, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Startup



# Pad color notation used in comments:
# Left, center, right
# l:colour, c: colour:, r: colour




# General command structure for endpoint 01
# 0x55 Magic number
# command byte 1
# command byte 2
# message counter, no noticed effect
# args...
# checksum, (simple addition of previous bytes with overflow at 255)
# padding to 32 bytes


# Noticed argument conventions
# Pad numbering:
# 0x01, 0x02, 0x03
# Colour ordering
# Red, green, blue
# Colour values 1 byte in length


# Checksum characteristics
# 1 Byte in size
# Always the last non-zero byte (Unknown what happens if checksum turns out to be zero)
# Reordering message bytes does not invalidate checksum
# Message counter affects checksum




# 0x06 0xc0 Immediately switch pad(s) to a value
# Byte: use
# 0: Always 0x55
# 1: Command
# 2: command cont
# 3: Message counter
# 4: Pad to change 0=all, 1=center, 2=left, 3=right,
# 5: Red value
# 6: Green value
# 7: Blue Value
# 8: Checksum
# 9-31: padding, 0x00


# Sniffed
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0xff, 0xff, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to light blue (Found via sniffing)
# Mixed colours found by fuzzing
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0x00, 0xff, 0x1b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to Purple (found via fuzzing)
# RGB Monochromatic hex(28) == 0x1c
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0x00, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to red
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0xff, 0x00, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to green (found via fuzzing)
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0xff, 28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch to dark blue (found via fuzzing)
# All pads off
dev.write(1, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0x00, 29, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Switch all pads off (Found by fuzzing)







# 0x14 Fade to value
# Byte 0 is always 0x55
# Byte
##        print dev.write(1, [0x55, 0x14, 0xc6, 0x04, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Fade to dark blue
#[0x55, 0x14, 0xc6, 0x26, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0xfd, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark Blue
#[0x55, 0x14, 0xc6, 0x27, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x18, 0xfb, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All pink
#[0x55, 0x14, 0xc6, 0x28, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x00, 0x00, 0xb4, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All red
#[0x55, 0x14, 0xc6, 0x29, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0xff, 0x6e, 0x00, 0xff, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All yellow
#[0x55, 0x14, 0xc6, 0x2a, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x00, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All green
#[0x55, 0x14, 0xc6, 0x2b, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x6e, 0x18, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All cyan
#[0x55, 0x14, 0xc6, 0x2c, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x01, 0x1e, 0x01, 0x00, 0x00, 0x18, 0x03, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# All dark blue








# 0x0e Immediately switch to set of colours
#[0x55,# Always 0x55
#0x0e,
#0xc8,
#0x20,# Message counter
#0x00,# ?
#0x00,# center:red
#0x00,# center:green
#0x00,# center:blue
#0x01,# ?
#0xff,# left:red
#0x1e,# left:green
#0x00,# left:blue
#0x01,# ?
#0x00,# right:red
#0x00,# right:green
#0x00,# right:blue
#0x6a,# Checksum
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00]# Padding

# left:cyan, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:cyan, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x1b, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x53, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x26, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x26, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x03, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x2e, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x19, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x07, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x3f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0c, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x44, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x01, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x39, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1a, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x6e, 0x18, 0x01, 0xff, 0x00, 0x18, 0x52, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x23, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x0d, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x20, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # Left:orange, center:yellow, right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x59, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x25, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x37, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x37, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x81, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0b, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1e, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x68, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x30, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x07, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x64, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x14, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x32, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x02, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x4c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x17, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x61, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x33, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x7d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x0d, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x57, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x23, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x6d, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])
dev.write(01, [0x55, 0x0e, 0xc8, 0x01, 0x00, 0x00, 0x00, 0x00, 0x01, 0xff, 0x1e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x4b, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])

# Fuzzed:
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x18, 184, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# left:off, center:yellow, right:pink
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x6e, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 160, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off, center:yellow, right:red
# Center
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0xff, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:red right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0xff, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:green right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0xff, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:blue right:off
# Left
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:red center:off right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x00, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:green center:off right:off
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xff, 0x01, 0x00, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:blue center:off right: off
# Right
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0x00, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:red
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0xff, 0x00, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:green
dev.write(01, [0x55, 0x0e, 0xc8, 0x06, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0xff, 51, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]) # left:off center:off right:blue

# Failed fuzzing:
#[0x55, 0x0e, 0xc8, 0x20, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x01, 0xff, 0xff, 0xff, chk, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],# nothing ever tuns on





# 0x06 ?Change one pad?
# Byte 0 is always 0x55
# Byte 3 is a message counter
#dev.write(01,
#    [
#    0x55,# Always 0x55
#    0x06,# 0x06 (command?)
#    0xc0,# 0xc0
#    0x02,# Message counter
#    0x00,# 0x0, 0x1, 0x2, 0x3
#    0xff,# Colour?
#    0xff,# Colour?
#    0xff,# Colour?
#    0x1a,# Checksum
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00,# Padding
#    0x00# Padding
#    ]
#    )
dev.write(01, [0x55, 0x06, 0xc0, 0x2b, 0x03, 0xff, 0x00, 0x18, 0x60, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# l:off, c:off, r:pink
dev.write(01, [0x55, 0x06, 0xc0, 0x02, 0x00, 0xff, 0xff, 0xff, 0x1a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# all light blue
dev.write(01, [0x55, 0x06, 0xc0, 0x02, 0x00, 0x00, 0x00, 0xff, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# All dark blue
dev.write(01, [0x55, 0x06, 0xc0, 0x2b, 0x00, 0x00, 0x00, 0xff, 0x45, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# All dark blue
dev.write(01, [0x55, 0x06, 0xc0, 0x34, 0x01, 0xf0, 0x00, 0x16, 0x56, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00])# Change center to pink


# 0x04 0x02
# Unknown effect, does not turn on pads?
#[0x55,# Always 0x55
#0x04,
#0xd2,
#0x17,# Message counter
#0x02,
#0x23,
#0x67,# Checksum?
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00,# Padding
#0x00]# Padding




# 0x0a 0xb3
# Unknown effect, does not turn on or off pads
[0x55,# Always 0x55
0x0a,#
0xb3,#
0x04,# Message counter?
0xa7,#
0x1f,#
0xd5,#
0x8b,#
0x5f,#
0xa1,#
0x06,#
0x06,#
0x48,# Checksum?
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00]# Padding



# 0x04 0xd2
# Unknown effect, does not turn on or off pads
[0x55,# Always 0x55
0x04,#
0xd2,#
0x2c,# Message counter?
0x00,#
0x26,#
0x7d,# Checksum?
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00],# Padding


# 0x08 0xc2
# Immediately change the colour of one pad, fade and flash available
# r:pink
[0x55,# Always 0x55
0x08,#
0xc2,#
0x13,# Message counter?
0x03,# Pad c=1 r=3
0x03,# ?change speed - confirm?
0x01,# ? flash rate/count - fuzz to investigate?
0xf0,# red
0x00,# green
0x16,# blue
0x3f,# Checksum?
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00,# Padding
0x00],# Padding

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



def main():
    pass

if __name__ == '__main__':
    main()
