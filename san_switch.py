from paramiko import SSHClient, AutoAddPolicy


def ssh_run_single_command(hostname, username, password, command):
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect(hostname=hostname, port=22, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(command)
    output = stdout.readlines()
    output = [i.rstrip() for i in output]
    ssh.close()
    return output

