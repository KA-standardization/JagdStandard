import time
import paramiko

conn = paramiko.SSHClient()
conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
conn.connect('10.0.17.100', username='root', password='``', look_for_keys=False, allow_agent=False)
# new_conn = conn.invoke_shell()
# output = new_conn.recv(5000)
# print(output)
# time.sleep(1)
# new_conn.send("ls -a")
# output = new_conn.recv(50000)
# print(output)

stdin, stdout, stderr = conn.exec_command('ls')
print(stdout.read().decode())
