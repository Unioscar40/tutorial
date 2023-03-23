from subprocess import run as sp_run
from os import getcwd, path, mkdir

CURRENT_DIR = getcwd()
BUILD_DIR = path.join(CURRENT_DIR, "..", "src", "build")


def run(command):
    sp_run(command, shell=True)


def createDir():
    mkdir(BUILD_DIR)

def config():
    if(not path.exists(BUILD_DIR)):
        createDir()
    
    cmd_config_command = f'cd {BUILD_DIR} && cmake ..'
    run(cmd_config_command)


def build():
    cmd_build_command = f'cd {BUILD_DIR} && cmake --build .'
    run(cmd_build_command)


def compile():
    cmd_compile_command = f'cd {BUILD_DIR} && ./Guide'
    run(cmd_compile_command)

def main():
    config()
    build()
    compile()

if __name__ == "__main__":
    main()