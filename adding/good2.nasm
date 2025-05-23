section .text
    global _start

_start:
   add rsp, 16
   mov rax, [rsp]
   sub rsp, 16
   ret