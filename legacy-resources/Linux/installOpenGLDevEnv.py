"""
Script to install OpenGL development environment on Linux Ubuntu
g++
cmake
xorg-dev
libglu1-mesa-dev
mesa-utils
libxinerama-dev
libxcursor-dev
libxi-dev
Glew
GLFW
Glut
glm
SOIL
Bullet
Assimp
"""
# for system commands
import os
import sys


def exit():
    print("Invalid input")
    sys.exit()


def updateSystem():
    print("**********************")
    print("System update ...")
    print("**********************")
    os.system("sudo apt update")
    os.system("sudo apt upgrade")


def installDevTools():
    print("**********************")
    print("Installing Dev Tools ...")
    print("**********************")
    os.system("sudo apt-get install g++ xorg-dev libglu1-mesa-dev libxinerama-dev libxcursor-dev  libxi-dev")


def installCmake():
    installation_instructions = (
        "\n**************************************\n"
        "Install Cmake? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing Cmake ...")
        print("**********************")
        os.system("sudo apt-get install cmake")
    elif install == 'n' or install == 'N':
        print("Skipping Git installation..")
    else:
        print("Invalid input!")
        installCmake()


def installGit():
    installation_instructions = (
        "\n**************************************\n"
        "Install Git? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing Git ...")
        print("**********************")
        os.system("sudo apt-get install git")
    elif install == 'n' or install == 'N':
        print("Skipping Git installation..")
    else:
        print("Invalid input!")
        installGit()


def installGLEW():
    installation_instructions = (
        "\n**************************************\n"
        "Install GLEW? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing GLEW ...")
        print("**********************")
        os.system("sudo apt-get install libglew-dev")
    elif install == 'n' or install == 'N':
        print ("Skipping GLEW installation..")
    else:
        print("Invalid input!")
        installGLEW()


def installGLFW():
    installation_instructions = (
        "\n**************************************\n"
        "Install GLFW [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing GLFW ...")
        print("**********************")
        os.system("sudo apt-get install libglfw3-dev libglfw3")
    elif install == 'n' or install == 'N':
        print ("Skipping GLFW installation..")
    else:
        print("Invalid input!")
        installGLFW()

def installGlm():
    installation_instructions = (
        "\n**************************************\n"
        "Install glm? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing glm ...")
        print("**********************")
        os.system("sudo apt-get install libglm-dev")
    elif install == 'n' or install == 'N':
        print("Skipping Git installation..")
    else:
        print("Invalid input!")
        installGlm()


def installSoil():
    installation_instructions = (
        "\n**************************************\n"
        "Install soil? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing soil ...")
        print("**********************")
        os.system("sudo apt-get install libsoil-dev")
    elif install == 'n' or install == 'N':
        print("Skipping Git installation..")
    else:
        print("Invalid input!")
        installSoil()


def installBULLET():
    installation_instructions = (
        "\n**************************************\n"
        "Install BULLET? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing BULLET ...")
        print("**********************")
        os.system("sudo apt-get install libbullet-dev")
        os.system("sudo apt-get install libbullet-extras-dev")
        os.system("sudo apt-get install libbullet-doc")
    elif install == 'n' or install == 'N':
        print ("Skipping BULLET installation..")
    else:
        print("Invalid input!")
        installBULLET()


def installASSIMP():
    installation_instructions = (
        "\n**************************************\n"
        "Install ASSIMP? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing ASSIMP ...")
        print("**********************")
        os.system("sudo apt-get install assimp-utils")
        os.system("sudo apt-get install libassimp-dev")
    elif install == 'n' or install == 'N':
        print ("Skipping ASSIMP installation..")
    else:
        print("Invalid input!")
        installASSIMP()



def installGLUT():
    installation_instructions = (
        "\n**************************************\n"
        "Install GLUT? [y|n]\n"
        "**************************************\n"
    )
    install = input(installation_instructions)
    if install == 'y' or install == 'Y':
        print("**********************")
        print("Installing GLUT ...")
        print("**********************")
        os.system("sudo apt-get install freeglut3 freeglut3-dev")
        os.system("sudo apt-get install binutils-gold")
    elif install == 'n' or install == 'N':
        print ("Skipping GLUT installation..")
    else:
        print("Invalid input!")
        installGLUT()



def openGLInfo():
    print("**********************")
    print("Installing mesa-utils ...")
    print("**********************")
    os.system("sudo apt install mesa-utils")

    print("**********************")
    print("OpenGL version ...")
    print("**********************")
    os.system("glxinfo | grep \"OpenGL version\"")
    print("**********************")
    print()
    os.system("glxgears")


updateSystem()
installDevTools()
installCmake()
installGit()
installGLFW()
installGLEW()
installGLUT()
installGlm()
installSoil()
installBULLET()
installASSIMP()
openGLInfo()

