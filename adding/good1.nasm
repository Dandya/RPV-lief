section .text
    global _start

_start:
    xor rax, rax

    mov rax, 0x0A2183D1B1D0B0D0
    push rax
    mov rax, 0xBBD020BBD0B0D0BB
    push rax
    mov rax, 0xD0B5D0B4D081D120
    push rax
    mov rax, 0x8FD1202CB0D094D0
    push rax

    mov rdx, 32

    ; output
    mov rax, 1
    mov rdi, 1
    mov rsi, rsp
    syscall

    add rsp, 32

    ; exit
    mov rax, 60
    xor rdi, rdi
    syscall