# -*- coding: utf-8 -*-

# Resource object code
#
# Created by: The Resource Compiler for PyQt5 (Qt v5.15.0)
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore

qt_resource_data = b"\
\x00\x00\x00\xec\
\x00\
\x00\x04\x36\x78\x9c\x9d\x93\xcd\x0d\xc2\x30\x0c\x85\x8d\xc4\x00\
\x8c\xc0\x91\x7b\xa5\x0e\xc0\x9d\x35\xb2\x93\xd7\xe8\x04\x1d\xc0\
\x53\x20\xf5\x8c\x98\x20\xf8\x39\x71\xff\x48\xda\x42\xa5\x27\xbb\
\x4e\x3e\xbb\x6e\x9c\xfb\xa3\x3d\x93\x3d\xad\xea\xa6\xba\x64\x9d\
\xe8\x9a\x16\xf2\xfa\xfc\x89\x31\x16\xf5\x7c\xbd\xab\x6b\x5b\xcc\
\x30\x0c\x24\x22\x66\x8f\xe6\x70\xae\xeb\x3a\x12\x66\xe2\x10\x4c\
\xf6\xbe\x93\xcb\xea\x65\x06\x16\x42\xdc\x72\x20\xae\x42\x1e\xec\
\x2b\xf1\xce\x45\x71\xc9\x18\x6f\x02\x8f\xaa\xd5\xc7\xbe\x89\x5d\
\xf2\x41\x7d\x88\x38\xc5\x7c\xed\x37\x3e\x52\x03\x5e\x7d\x09\xdf\
\xe7\xe5\x7c\xea\x3d\x2c\x78\x56\x9f\x95\x47\xff\x51\xd9\x2d\xde\
\xec\xec\x1b\x9d\xef\xfb\xde\xb8\x92\xd6\xf5\x93\x3f\xf1\xb0\x35\
\x76\xcd\x97\xfa\x37\x1e\x7d\xfd\xc9\x63\x76\x70\x6e\x76\xbe\x3b\
\xfd\x97\x78\x76\x1f\x56\xb8\xca\xd7\xe6\x47\xb2\xdf\x8c\xe7\xcf\
\xc5\x19\xb2\x7f\xcc\x79\x7e\x65\x9a\x5f\xcc\x8d\xeb\xc8\x3d\x42\
\xbd\xf9\xfd\x39\xc2\x7c\x00\xbb\x93\x5d\x9d\
"

qt_resource_name = b"\
\x00\x05\
\x00\x6f\xa6\x53\
\x00\x69\
\x00\x63\x00\x6f\x00\x6e\x00\x73\
\x00\x06\
\x07\x03\x7d\xc3\
\x00\x69\
\x00\x6d\x00\x61\x00\x67\x00\x65\x00\x73\
\x00\x07\
\x04\x65\x49\x20\
\x00\x31\
\x00\x33\x00\x32\x00\x2e\x00\x62\x00\x6d\x00\x70\
"

qt_resource_struct_v1 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x10\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x22\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
"

qt_resource_struct_v2 = b"\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x01\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\x02\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x10\x00\x02\x00\x00\x00\x01\x00\x00\x00\x03\
\x00\x00\x00\x00\x00\x00\x00\x00\
\x00\x00\x00\x22\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\
\x00\x00\x01\x58\xd1\xf5\xbd\x85\
"

qt_version = [int(v) for v in QtCore.qVersion().split('.')]
if qt_version < [5, 8, 0]:
    rcc_version = 1
    qt_resource_struct = qt_resource_struct_v1
else:
    rcc_version = 2
    qt_resource_struct = qt_resource_struct_v2

def qInitResources():
    QtCore.qRegisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

def qCleanupResources():
    QtCore.qUnregisterResourceData(rcc_version, qt_resource_struct, qt_resource_name, qt_resource_data)

qInitResources()
