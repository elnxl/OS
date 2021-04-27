BITS 64
global _start

_start: 
	mov al, 1
	cpuid
	test ecx, 0x80000000
	jnz vm 
	mov esi, desktop
	mov edx, 8
	jmp output
	
vm: 
	mov rsi, virtual
	mov rdx, 16
	
output:
	xor eax, eax
	add al, 1
	xor edi, edi
	add di, 1
    syscall
	xor eax, eax
	add al, 60
	xor edi, edi
	syscall

desktop: db "desktop", 0x0a
virtual: db "Virtual Machine", 0x0a
