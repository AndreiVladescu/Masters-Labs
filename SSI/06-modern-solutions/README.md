# Prologue of a function in assembly:
```
push ebp         ; Save the current value of the base pointer
mov ebp, esp     ; Set the base pointer to the current value of the stack pointer
sub esp, X       ; Allocate space for local variables by subtracting X bytes from the stack pointer

```

# Epilogue of a function in assembly:

```
mov %ebp, %esp   ; Restore the stack pointer to the saved base pointer value
pop %ebp         ; Restore the original value of the base pointer
ret              ; Return from the function
```

# Calling convention

# x86 (32-bit):

## cdecl (C declaration):
In cdecl, the caller is responsible for cleaning up the stack after a function call. Function arguments are typically passed on the stack in reverse order (right to left), and the return value is often placed in the `EAX` register.

# x86-64 (64-bit):

## System V AMD64 ABI (used by Unix-like systems):
The System V AMD64 ABI is a widely used calling convention for x86-64 on Unix-like systems.

- Integer and pointer arguments (up to the first six) are passed in registers (`RDI`, `RSI`, `RDX`, `RCX`, `R8`, `R9`).
- Additional arguments are passed on the stack.
- The return value is stored in the `RAX` register.
- The callee is responsible for cleaning up the stack.
- Callee-saved registers (`RBX`, `RBP`, `R12-R15`) must be preserved by the callee.

## Microsoft x64 calling convention (used by Windows):
On Windows, the x64 calling convention is different from the System V AMD64 ABI.

- Integer and pointer arguments are passed in registers (`RCX`, `RDX`, `R8`, `R9`).
- Floating-point arguments are passed in `XMM0` to `XMM3`.
- The return value is stored in the `RAX` register.
- The caller is responsible for cleaning up the stack.
- Callee-saved registers (`RBX`, `RBP`, `RDI`, `RSI`, `R12-R15`) must be preserved by the callee.

Keep in mind that these conventions are used by compilers to generate assembly code for function calls. The choice of calling convention may also depend on the operating system and compiler settings. Additionally, other conventions exist, and some programming languages or libraries may define their own conventions. Always refer to the specific documentation for the platform, compiler, or language you are working with for the most accurate and up-to-date information.
