# -*- coding: utf-8 -*-
import paramiko


class SSHScript(object):

    def __init__(self, host, username=None, password=None, is_idRsa=False, idRsa_file=None):
        self.conn = paramiko.SSHClient()
        self.conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        if is_idRsa:
            key = paramiko.RSAKey.from_private_key_file(idRsa_file)
            self.conn.connect(host, username=username, pkey=key)
        else:
            self.conn.connect(host, username=username, password=password, look_for_keys=False, allow_agent=False)

    def run_cmd(self, cmd):
        stdin, stdout, stderr = self.conn.exec_command(cmd)
        err = stderr.read().decode()
        out = stdout.read().decode()
        if len(err) > 0:
            print('[Stat]: ERROR, [Msgs]: {}'.format(err))
        else:
            print('[Stat]: Success, [Msgs]: \r\n{}'.format(out))

    def close(self):
        self.conn.close()


def main(hosts, cmd):
    for k, v in hosts.items():
        print('<--{}: {}-->'.format(k, v['host']))
        s = SSHScript(v['host'], username=v['user'], is_idRsa=v['is_idRsa'], idRsa_file=v['key'])
        try:
            if cmd in ['start', 'stop', 'restart']:
                s.run_cmd(v['cmd'][f'{cmd}'])
            else:
                s.run_cmd(cmd)
        except Exception as err:
            print('[Stat]: Script-Error, [Msgs]: {}'.format(err))
        finally:
            s.close()


if __name__ == '__main__':
    # ls -lR|grep '^d'|gawk '{print "/logs/ts_scrapy/"$9}'|xargs ls -lR |grep '^[/-]'
    # import sys
    # sys.path.append('Python3_Standard/paramiko_22_5_24')
    # print(sys.path)
    # print(__file__, __name__, __package__, sep='>--<')
    from paramiko_22_5_24.ssh_config import hosts

    main(
        hosts,
        # 'df -h'
        'start'
    )

