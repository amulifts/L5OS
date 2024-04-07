import subprocess

def manage_opencanary(command):
    if command not in ['start', 'stop', 'restart']:
        raise ValueError('Invalid command')
    subprocess.run(['service', 'opencanary', command], check=True)
