from fabric.api import put, run, sudo, local, env, cd

'''
loads file to columbia server
'''


env.hosts = ['cunix.cc.columbia.edu']
env.user = 'ds2998'

def upload_key():
    # todo: append to file rather than overwrite
    #run('mkdir ~/.ssh')
    put('~/.ssh/id_rsa.pub', '~/.ssh/authorized_keys')

def deploy_files():
    put('kitchen_custom.js', '~/public_html/monitor/kitchen_custom.js')
    put('kitchen_custom.html', '~/public_html/monitor/kitchen_custom.html')

