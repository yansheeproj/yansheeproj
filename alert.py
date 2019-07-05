import paramiko
from client import client

def ssh_connect( _host, _username, _password ):
    try:
        _ssh_fd = paramiko.SSHClient()
        _ssh_fd.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
        _ssh_fd.connect( _host, username = _username, password = _password )
    except Exception, e:
        print( 'ssh %s@%s: %s' % (_username, _host, e) )
        exit()
    return _ssh_fd

def ssh_exec_cmd( _ssh_fd, _cmd ):
    return _ssh_fd.exec_command( _cmd )

def ssh_close( _ssh_fd ):
    _ssh_fd.close()

def alert(ip): 
    port = 22  
    username = 'pi'  
    password = 'raspberry'  
    cmd = "python /home/pi/server.py"  

    sshd = ssh_connect(ip , username , password)
    stdin, stdout, stderr = ssh_exec_cmd(sshd, cmd)
    client("alert")
    err_list = stderr.readlines()
    
    if len( err_list ) > 0:
        print 'ERROR:'
        for item in err_list:
            print item
        exit()
    
    for item in stdout.readlines():
        print "stdout: ", item, ssh_close( sshd )

if __name__=="__main__":
    ips = '192.168.43.134'
    alert(ips)

