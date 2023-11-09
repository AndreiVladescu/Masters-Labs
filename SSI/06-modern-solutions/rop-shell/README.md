# How it works
```
    40 * b'A': This adds 40 bytes of the character 'A' to the payload. This is typically done to fill the buffer until the return address is reached.

    p64(pop_rdi_ret_address): This assumes pop_rdi_ret_address is the address of a gadget that ends with a pop rdi; ret sequence. This gadget is commonly used to set the value of the rdi register before calling a function. It is often used when calling functions that take arguments.

    p64(bin_sh_offset): This assumes bin_sh_offset is the offset of the "/bin/sh" string in the libc library. This value will be loaded into the rdi register by the pop rdi; ret gadget.

    p64(ret_gadget): This assumes ret_gadget is the address of a gadget that simply executes a ret instruction. This is used to control the flow of execution and return to the address pointed to by the stack.

    system_plt_address: This assumes system_plt_address is the address of the system function in libc. After the ROP chain sets up the rdi register with the address of "/bin/sh", the ret gadget is used to return to system_plt_address, effectively calling the system function with "/bin/sh" as an argument.
	```