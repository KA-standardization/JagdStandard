import subprocess as sb

if __name__ == '__main__':
    a = sb.run(['dir', r'L:\Developer\JagdStandard'], capture_output=True)
    print(a)

"""
 p = Popen('tail -n 1 /root/post_star_kuai.log',stdout=PIPE,stderr=PIPE,shell=True)
>>> p.wait()
0
>>> p.stdout.read()
b'[Log] [Time]: 1655004665,[State]: Success\n'

a=sb.run(['ls','-la'], shell=True)
"""
