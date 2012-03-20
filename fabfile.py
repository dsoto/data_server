from fabric.api import put, run, sudo, local, env, cd
from config import host_ip

'''
to set up server from scratch
> fab bootstrap
'''

'''
todo
put in apache config files
'''


env.hosts = [host_ip]
env.user = 'root'

PACKAGES = ['git-core',
            'python-pip',
            'sqlite3',
            'python-sqlalchemy',
            'python-sqlite']

PIP_PACKAGES = ['web.py',
                'twiggy']

def bootstrap():
    upload_key()
    create_directories()
    install_packages()
    deploy_files()
    create_database()

def create_directories():
    run('mkdir ./data_server')

def upload_key():
    # todo: append to file rather than overwrite
    run('mkdir ~/.ssh')
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
    sudo('tar xvf deploy-files.tar -C ./data_server/')

def create_database():
    with cd('~/data_server'):
        sudo('sqlite3 database.db < create_table.sql')

def run_server():
    # todo: figure this shit out
    #run('bash ~/data_server/init.sh')
    #run('nohup python server.py >& /dev/null < /dev/null &')
    #run('screen -d -m "python server.py"')
    run('dtach /tmp/dtachsocket -z python server.py')

def stop_server():
    pass

def restart_server():
    stop_server()
    run_server()