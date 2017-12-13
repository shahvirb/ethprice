import os
import glob
import subprocess

AMPY_PORT = 'COM4'
RETRY = 3

def init():
    os.environ['AMPY_PORT'] = AMPY_PORT
    os.chdir('..')


def find_py():
    py = glob.glob('*.py')
    return py


def cmd(*args, **kwargs):
    for i in range(RETRY):
        try:
            process = subprocess.Popen(*args, stdout=subprocess.PIPE, **kwargs)
            for line in process.stdout:
                print(line.rstrip())
            break
        except ampy.pyboard.PyboardError:
            print("FATAL ampy.pyboard.PyboardError")


def put_files(files):
    for file in files:
        print('Put: {}'.format(file))
        cmd(['ampy', 'put', file])


def main():
    init()
    
    print('Current files @ {}'.format(AMPY_PORT))
    cmd(['ampy', 'ls'])
    print()
    
    files = find_py()
    put_files(files)


if __name__ == '__main__':
    main()
    