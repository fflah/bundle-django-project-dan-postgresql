import errno
import shutil
from subprocess import call
import os
from pathlib import Path                                                                          


def setup():
    program = 'docker'
    home = str(Path.home())  
    dir_app =  home + '\mysite'
    print('||Mengecek Requitments||')
    print('')

    if shutil.which(program) != None:
        print(program + ' installed...ok')
    else:
        print(program + ' not installed')
        print(program + ' install...')
        print('please wait few minutes')
        call('requirements\Docker_Desktop_Installer.exe')
        print(program + ' installed...ok')
    
    print('Tolong set Docker ke Linux Container terlebih dahulu')
    linux_container  = input('Sudah ? (y/n) :')

    if linux_container == 'y':
        try:
            os.mkdir(dir_app)    
        except OSError as e:
            if e.errno == errno.EEXIST:
                # direktory sudah ada
                pass
            else:
                raise

        shutil.copy('requirements\docker-compose.yml', dir_app)
        print('harap tunggu sistem sedang setup image ke docker')
        print('please wait few minutes...')
        os.system('cmd /c "docker load -i requirements\postgres.tar"')
        os.system('cmd /c "docker load -i requirements\mysite.tar"')
        print('load image ke docker... ok')
        print('silakan setting Resources File sharing Docker')
        s_cara = '''
            caranya:
                1. Pergi ke docker settings
                2. Klik Resources kemudian pilih FILE SHARING
                3. Tambahkan path {}:
                4. Klik Apply & Restart
         '''.format(dir_app)
        print(s_cara)
        file_sharing  = input('Sudah ? (y/n) :')
        if file_sharing == 'y':
            cmd_path = 'cmd /c "C: & cd {} & docker-compose up --no-start"'.format(dir_app)  
            os.system(cmd_path)    
            shutil.copy('requirements/run.exe', dir_app)

        input('instalasi selesai, tekan enter untuk keluar')

    else:
        return input('instalasi belum berhasil, anda belum mengeset Docker ke Linux Container silakan coba lagi, tekan enter untuk keluar')

setup()