# ******************************************************************************
#  Direitos Autorais (c) 2019-2020 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************
import os
from re import sub
from subprocess import getoutput


def pt():
    print('\n[I] GERANDO A LISTA DOS MÓDULOS\n    ISTO PODE DEMORAR ALGUNS SEGUNDOS POR FAVOR AGUARDE..')
    lista = getoutput('pip list')

    if not os.path.exists('list'):
        os.makedirs('list')

    with open('list/pipList.txt', 'w+') as pl:
        pl.write(lista)
        pl.close()
    
    with open('list/pipList.txt', 'r+') as pl:
        pl_ = pl.readlines()
        for i in [1, 2]:
            pl_.remove(pl_[0])
        pl.close()
        
        pl2 = open('list/pipList.txt', 'w+')
        for l in pl_:
            pip = sub('[ ]+', '>=', l)
            pl2.write(str(pip))
    
    pl2.close()
    print('\nFEITO..')
    
    perg = input('\n[P] DESEJA FAZER A ATUALIZAÇÃO AUTOMÁTICA AGORA?\n[S|N]> ')
    
    if perg.upper() == 'S':
        os.system('py pipUpgrade.py')
    elif perg.upper() == 'N':
        print('\n[I] OBRIGADO\n    AGORA VERIFIQUE O FICHEIRO pipList.txt E DEPOIS EXECUTE O SCRIPT pipUpgrade.py PARA ATUALIZAR A SUA LISTA DE MÓDULOS 3rd-PART..')
        exit(0)
    else:
        print('\n[X] OPÇÃO INVÁLIDA..\n    TERMINANDO OPERAÇÃO!')
        exit(0)


def en():
    print('\n[I] BUILDING THE LIST OF MODULES\n    THIS CAN TAKE A FEW SECONDS, PLEASE WAIT..')
    lista = getoutput('pip list')

    if not os.path.exists('list'):
        os.makedirs('list')

    with open('list/pipList.txt', 'w+') as pl:
        pl.write(lista)
        pl.close()
    
    with open('list/pipList.txt', 'r+') as pl:
        pl_ = pl.readlines()
        for i in [1, 2]:
            pl_.remove(pl_[0])
        pl.close()
        
        pl2 = open('list/pipList.txt', 'w+')
        for l in pl_:
            pip = sub('[ ]+', '>=', l)
            pl2.write(str(pip))
    
    pl2.close()
    print('\nDONE..')
    
    perg = input('\n[Q] DO YOU WANT TO MAKE AUTO-UPDATE RIGHT NOW?\n[Y|N]> ')
    
    if perg.upper() == 'Y':
        os.system('py pipUpgrade.py')
    elif perg.upper() == 'N':
        print('\n[I] THANKS\n   NOW CHECK FILE pipList.txt AND AFTER RUN pipUpgrade.py TO UPDATE YOUR 3rd-PART MODULE LIST..')
        exit(0)
    else:
        print('\n[X] INVALID CHOICE..\n    CLOSING OPERATION!')
        exit(0)


if __name__ == '__main__':
    print(r"""
     ________                                      _____________
    / ______ \                                    |     _____   \
   |_/      \ \                                   |    |     \   |
             | |                __                |    |      |  |
             | |               |  |  ___________  |    |_____/   |    ____________
     _       | |__             |  | |           | |    _________/    |____________|
    | |------| |  | ______     |  | |  PYTHON   | |   |      __ _______   |  |
    |_|------| |  |/ _____|____|  | |  PIP      | |   |     /  |   _   |  |  |
             | |  | /    /   __   | |  INSTALL  | |   |    /   |  |_|  |  |  |
             | |  |/    |   /  |  | |  UPGRADE  | |   |   / /| |  _____|  |  |
    _        | |  |     |  |   |  | |___________| |   |  /  _  | |\ \     |  |
   | \______/ /|  |     |   \__|  |               |   | /  / | | | \ \    |  |
    \________/ |__|      \________|               |___|/__/  |_|_|  \_\   |__|
                      ________     __       ____________      _______
          __       __|    __  \   |  |___  |____________|__  |   __  \
         |  |     |  |   |__|  |  |  |   \      |__|  _____| |  |__|  |
         |  |     |  |    ____/___|  | |\ \     |__| |       |   ____/
         |  |     |  |   |    /   |  |  _  \    |__| |---|   |  | \  \
          \  \___/  /|   |   |    |  | | \  \   |__| |_____  |  |  \  \
           \_______/ |___|    \___|__|_|  \__\  |__|_______| |__|   \__\
""")
    idiom = input('\n[PT - EN]\n> ')
    
    if idiom.upper() == 'PT':
        pt()
    elif idiom.upper() == 'EN':
        en()
    else:
        pass
