import os
import glob
import subprocess

AMPY_PORT = 'COM4'

def init():
    os.environ['AMPY_PORT'] = AMPY_PORT
    os.chdir('..')


def find_py():
    py = glob.glob('*.py')
    return py


def cmd(*args, **kwargs):
    process = subprocess.Popen(*args, stdout=subprocess.PIPE, **kwargs)
    #stdout = process.communicate()[0]
    for line in process.stdout:
        print(line.rstrip())


def put_files(files):
    for file in files:
        print('Put: {}'.format(file))
        cmd(['ampy', 'put', file])


def main():
    init()
    
    print('Current files @ {}'.format(AMPY_PORT))
    cmd(['ampy', 'ls'])
    
    
    files = find_py()
    put_files(files)


if __name__ == '__main__':
    main()
    