from fabric.api import run, sudo, local, env

'''
to set up server from scratch
> fab upload_key
> fab install_packages
'''


env.hosts = ['108.166.81.171']
env.user = 'root'

PACKAGES = ['git-core', 'postgresql', 'python-psycopg2', 'python-pip']

PIP_PACKAGES = ['web.py']

def upload_key():
    # todo: append to file rather than overwrite
    # todo: check if .ssh exists
    sudo('mkdir ~/.ssh')
    local('scp ~/.ssh/id_rsa.pub root@108.166.81.171:~/.ssh/authorized_keys')

def get_system_info():
    run('uname -s')

def install_packages():
    sudo('apt-get update')
    for p in PACKAGES:
        sudo('apt-get -y install %s' % p)
    for p in PIP_PACKAGES:
        sudo('pip install %s' % p)