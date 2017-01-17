import os
import subprocess
import sys

PATH = os.path.join(sys.exec_prefix, 'Scripts', 'pyuic5.exe')


def main():
    for file in os.listdir('.'):
        if file.endswith('.ui'):
            subprocess.run([PATH, file, '-o', '{}.py.'.format(os.path.splitext(file)[0])])


if __name__ == '__main__':
    main()
