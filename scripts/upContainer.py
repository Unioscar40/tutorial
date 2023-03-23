from subprocess import run as sp_run
from os import getcwd, path

CURRENT_DIR = getcwd()

def run(command):
    sp_run(command, shell=True)

def upContainer():
    directory = path.join(CURRENT_DIR,'..','docker')
    command = f"cd {directory} && docker compose up -d && "
    command += "docker exec -it tutorial-dev-container bash "
    run(command)

def main():
    upContainer()

if __name__ == "__main__":
    main()