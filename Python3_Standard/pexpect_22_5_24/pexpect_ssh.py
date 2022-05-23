from pexpect import pxssh

child = pxssh.pxssh()
child.login(
    '10.0.17.100',
    'root',
    '``',
    auto_prompt_reset=False
)
# child.sendline('systemctl restart zhihu-mixin.service')
child.sendline('ls')
print(child.before)
child.sendline('uname -a')
# child.expect('# root @ 8-200')
print(child.before)
print(child.after)

child.logout()
