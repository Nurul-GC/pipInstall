# ******************************************************************************
#  Direitos Autorais (c) 2019-2020 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from os import system, chdir, path
from sys import exit

banner = r"""
     ________                          _______________
    / ______ \                         |     ______   \
   |_/      \ \                        |     |     \   |
             | |       __              |     |      |  |
             | |      |  |             |     |_____/   |   ____________
     _       | |      |  |             |   ___________/   |____________|
    | |------| |      |  |  _________  |   |      __ _______   |  |
    |_|------| | _____|  | |_________| |   |     /  |   _   |  |  |
             | |/   __   | |_________| |   |    /   |  |_|  |  |  |
             | |   /  |  | |_________| |   |   / /| |  _____|  |  |
   __        | |  |   |  |             |   |  /  _  | |\ \     |  |
   \ \______/ /|   \__|  |             |   | /  / | | | \ \    |  |
    \________/  \________|             |___|/__/  |_|_|  \_\   |__|
                  ________     __       ____________      _______
      __       __|    __  \   |  |___  |____________|__  |   __  \
     |  |     |  |   |__|  |  |  |   \      |__|  _____| |  |__|  |
     |  |     |  |   _____/___|  | |\ \     |__| |       |   ____/
     |  |     |  |   |    /   |  |  _  \    |__| |---|   |  | \  \
      \  \___/  /|   |   |    |  | | \  \   |__| |_____  |  |  \  \
       \_______/ |___|    \___|__|_|  \__\  |__|_______| |__|   \__\

"""


def pipupgrade(_pip_list: str):
    if path.exists(_pip_list):
        try:
            print(f"{banner}\n\n[info] upgrading your modules\n\tthis can take a few seconds please wait..")
            chdir("list")
            system(f"pip install --upgrade -r {_pip_list}")
        except Exception as erro:
            print(f"\n\t[!] {erro}..\n")
            pass
        finally:
            print("\nPackages Updated Successfully!")
            exit(0)
    else:
        print("\n\n\t[!] Am Sorry the package list provided doesn't exist.")
        exit(0)
