#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys

from shutil import copyfile

def usage(commands):
    print('usage: ./exec.py <command> [args]')
    print()
    print('available commands:')
    for command in commands:
        print('    {}'.format(command))

def execute(*args):
    print(' '.join(args))
    subprocess.call(list(args))

def compose(*args):
    execute('docker-compose', *args)

def backend(*args):
    compose('run', '--rm', 'web', './wait-for-postgres.sh', *args)

# TODO allow docker or pipenv calls based on environment
def pipenv(*args):
    backend('pipenv', *args)

def run(*args):
    pipenv('run', *args)

def manage(*args):
    pipenv('run', 'python', 'manage.py', *args)

def backup_db(*args):
    manage('dumpdata', '-o', 'data/db.json', '--indent', '4', *args)

def docs(*args):
    pipenv('run', 'make', '-C', 'docs', *args)

def lint(*args):
    # TODO set up flake8, isort, and pylint
    print('lint is not supported yet')

def reset():
    print('Reset will remove all data associated with the containers.')
    if input('Are you sure you would like to remove all data? (y/N): ') != 'y':
        return

    if not os.path.isfile('.env'):
        copyfile('default.env', '.env')

    compose('down', '-v') 
    compose('build')
    pipenv('sync', '--dev')

def reset_db():
    manage('reset_db')
    manage('migrate')

def restore_db(*args):
    manage('loaddata', 'data/db.json')

def runserver(*args):
    manage('runserver', '0:8000')

def shell():
    pipenv('shell')

if __name__ == '__main__':
    commands = {
        'backup_db': backup_db,
        'compose': compose,
        'docs': docs,
        'lint': lint,
        'manage': manage,
        'pipenv': pipenv,
        'reset': reset,
        'reset_db': reset_db,
        'restore_db': restore_db,
        'run': run,
        'runserver': runserver,
        'shell': shell,
    }

    parser = argparse.ArgumentParser(
        description='Execute project-defined command.'
    )
    parser.add_argument('command', type=str)

    args, params = parser.parse_known_args()
    if args.command not in commands:
        usage(commands)
        exit(1)

    commands[args.command](*params)
