import subprocess as sp

sp.call('sshpass -p "passwd" ssh username@ip_address "mpg123 c*3;ls"',shell=True)
sp.call('ls',shell=True)
