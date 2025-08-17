; calc.asm — NASM x86-64 Linux
; nasm -felf64 calc.asm && ld -o calc calc.o
; ./calc

BITS 64

%define SYS_READ   0
%define SYS_WRITE  1
%define SYS_EXIT   60
%define STDIN      0
%define STDOUT     1

section .data
    msg1:      db "Digite o primeiro numero: ",0
    msg1_len   equ $-msg1
    msgop:     db "Digite o operador (+, -, *, /): ",0
    msgop_len  equ $-msgop
    msg2:      db "Digite o segundo numero: ",0
    msg2_len   equ $-msg2
    msgres:    db "Resultado: ",0
    msgres_len equ $-msgres
    msgerr0:   db "Erro: divisao por zero!",10,0
    msgerr0_len equ $-msgerr0
    msgerrop:  db "Operador invalido!",10,0
    msgerrop_len equ $-msgerrop
    nl:        db 10

section .bss
    buf1   resb 64
    buf2   resb 64
    bufop  resb 8
    outbuf resb 64

section .text
    global _start

_start:
    ; num1
    mov rdi, msg1       ; print prompt 1
    mov rsi, msg1_len
    call print

    mov rdi, buf1       ; read line
    mov rsi, 64
    call read_line
    mov rdi, buf1       ; parse int -> RAX
    call parse_int
    mov r12, rax        ; num1 em r12

    ; operador
    mov rdi, msgop
    mov rsi, msgop_len
    call print

    mov rdi, bufop
    mov rsi, 8
    call read_line
    mov al, [bufop]     ; primeiro char
    mov bl, al          ; op em bl

    ; num2
    mov rdi, msg2
    mov rsi, msg2_len
    call print

    mov rdi, buf2
    mov rsi, 64
    call read_line
    mov rdi, buf2
    call parse_int
    mov r13, rax        ; num2 em r13

    ; calcula
    mov rax, r12
    cmp bl, '+'
    je .add
    cmp bl, '-'
    je .sub
    cmp bl, '*'
    je .mul
    cmp bl, '/'
    je .div

    ; operador invalido
    mov rdi, msgerrop
    mov rsi, msgerrop_len
    call print
    jmp exit0

.add:
    add rax, r13
    jmp .show

.sub:
    sub rax, r13
    jmp .show

.mul:
    imul rax, r13
    jmp .show

.div:
    cmp r13, 0
    je .divzero
    cqo                 ; sign-extend rax -> rdx:rax
    idiv r13            ; rax = rax / r13
    jmp .show

.divzero:
    mov rdi, msgerr0
    mov rsi, msgerr0_len
    call print
    jmp exit0

.show:
    ; "Resultado: "
    mov rdi, msgres
    mov rsi, msgres_len
    call print

    ; itoa(r ax) -> outbuf, retorna RSI=len
    mov rdi, rax
    mov rsi, outbuf
    call itoa

    ; print número
    mov rdi, outbuf
    ; len está em RAX (retorno do itoa)
    mov rsi, rax
    call print

    ; newline
    mov rdi, nl
    mov rsi, 1
    call print

exit0:
    mov rax, SYS_EXIT
    xor rdi, rdi
    syscall

; --- funções utilitárias ---

; print(ptr, len)
; RDI=ptr, RSI=len
print:
    mov rax, SYS_WRITE
    mov rdi, STDOUT
    ; RSI já é ptr, RDX=len
    mov rdx, rsi
    mov rsi, rdi        ; cuidado: precisamos restaurar rdi/si
    ; arruma registros: RDI=fd, RSI=ptr (salvo antes), RDX=len
    xchg rsi, rdx       ; rsi<-len, rdx<-ptr
    ; agora precisamos RDX=len e RSI=ptr:
    xchg rsi, rdx       ; volta (efeito net: RDI=1, RSI=ptr, RDX=len)
    syscall
    ret

; read_line(buf, max) -> lê até '\n' ou EOF, coloca 0 final
; RDI=buf, RSI=max
read_line:
    push rdi
    mov rax, SYS_READ
    mov rdx, rsi        ; count
    mov rsi, rdi        ; buf
    mov rdi, STDIN
    syscall             ; rax = bytes lidos
    pop rdi
    cmp rax, 0
    jle .done
    mov rcx, rax
    mov rbx, rdi
.find_nl:
    cmp byte [rbx], 10
    je .zap
    cmp rcx, 0
    je .done
    inc rbx
    dec rcx
    jmp .find_nl
.zap:
    mov byte [rbx], 0
.done:
    ret

; parse_int(ptr) -> RAX=int64
; aceita espaço inicial, sinal, dígitos
parse_int:
    mov rsi, rdi
    xor rax, rax        ; acumulador
    xor rbx, rbx        ; flag negativo
.skip_ws:
    mov dl, [rsi]
    cmp dl, ' '
    je .adv
    cmp dl, 9
    je .adv
    cmp dl, 13
    je .adv
    cmp dl, 0
    je .end
    jmp .chk_sign
.adv:
    inc rsi
    jmp .skip_ws
.chk_sign:
    cmp dl, '-'
    jne .chk_plus
    mov bl, 1
    inc rsi
    jmp .loop
.chk_plus:
    cmp dl, '+'
    jne .loop
    inc rsi
.loop:
    mov dl, [rsi]
    cmp dl, '0'
    jb .end
    cmp dl, '9'
    ja .end
    imul rax, rax, 10
    mov rdx, 0
    mov r8, rax
    movzx rdx, dl
    sub rdx, '0'
    add rax, rdx
    inc rsi
    jmp .loop
.end:
    cmp bl, 0
    je .ret
    neg rax
.ret:
    ret

; itoa(valor:RDI, buf:RSI) -> RAX=len
itoa:
    mov rax, rdi        ; valor
    mov rbx, rsi        ; buf
    mov rcx, 0
    mov r8, 0           ; flag negativo

    cmp rax, 0
    jge .conv
    neg rax
    mov r8, 1

.conv:
    cmp rax, 0
    jne .loop2
    mov byte [rbx], '0'
    mov eax, 1
    ret
.loop2:
    xor rdx, rdx
    mov r10, 10
    div r10             ; rax/=10, rdx=resto
    add rdx, '0'
    push rdx
    inc rcx
    cmp rax, 0
    jne .loop2

    cmp r8, 0
    je .outdig
    mov byte [rbx], '-'
    inc rbx

.outdig:
    ; desempilha dígitos
    .popd:
        pop rdx
        mov [rbx], dl
        inc rbx
        dec rcx
        jnz .popd

    mov [rbx], byte 0
    ; len = (rbx - buf)
    mov rax, rbx
    sub rax, rsi
    ret
