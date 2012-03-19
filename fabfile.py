from fabric.api import put, run, sudo, local, env, cd

'''
to set up server from scratch
> fab upload_key
> fab install_packages
> fab deploy_files

'''

'''
todo
put in apache config files
'''


env.hosts = ['108.166.81.194']
env.user = 'root'

PACKAGES = ['git-core',
            'postgresql',
            'python-psycopg2',
            'python-pip',
            'sqlite3',
            'python-sqlalchemy',
            'python-sqlite']

PIP_PACKAGES = ['web.py']

def upload_key():
    # todo: append to file rather than overwrite
    # todo: check if .ssh exists
    sudo('mkdir ~/.ssh')
    put('~/.ssh/id_rsa.pub', '~/.ssh/authorized_keys')

def get_system_info():
    run('uname -s')

def install_packages():
    sudo('apt-get update')
    for p in PACKAGES:
        sudo('apt-get -y install %s' % p)
    for p in PIP_PACKAGES:
        sudo('pip install %s' % p)

def deploy_files():
    local('tar cvf deploy-files.tar *')
    put('deploy-files.tar', '~/')
    run('mkdir ./data_server')
    sudo('tar xvf deploy-files.tar -C ./data_server/')

def create_database():
    with cd('~/data_server'):
        sudo('sqlite3 database.db < create_table.sql')

def run_server():
    pass

def stop_server():
    pass

def restart_server():
    stop_server()
    run_server()