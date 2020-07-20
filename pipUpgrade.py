# ******************************************************************************
#  Direitos Autorais (c) 2019-2020 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************

from os import system, chdir

r"""
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

try:
    print('\n[INFO] ATUALIZAÇÃO DOS MÓDULOS EM CURSO\n     ISTO PODE DEMORAR ALGUNS SEGUNDOS, POR FAVOR AGUARDE..')
    print('\n[INFO] UPGRADE OF MODULES RUNNING\n    THIS CAN TAKE A FEW SECONDS PLEASE WAIT..')
    chdir('list')
    system('pip install --upgrade -r pipList.txt')
except Exception as erro:
    print(f'\n[ERRO] {erro}')
    pass
finally:
    print('\nATUALIZAÇÃO CONCLUIDA!')
    exit(0)
