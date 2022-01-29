# ******************************************************************************
#  Direitos Autorais (c) 2019-2020 Nurul GC                                    *
#                                                                              *
#  Jovem Programador                                                           *
#  Estudante de Engenharia de Telecomunicações                                 *
#  Tecnologia de Informação e de Medicina.                                     *
#  Foco Fé Força Paciência                                                     *
#  Allah no Comando.                                                           *
# ******************************************************************************
from re import sub
from subprocess import getoutput
from time import sleep

from pu import pipupgrade


def piplist():
    print('\n[i] Building the list of modules..')
    sleep(0.3)
    print("\nThis can take a few seconds, please wait..")

    lista = getoutput('pip list')
    with open('list/packages.txt', 'w+') as pl:
        pl.write(lista)
        pl.close()
    
    with open('list/packages.txt', 'r+') as pl:
        pl_ = pl.readlines()
        for _ in range(2):
            pl_.remove(pl_[0])
        pl.close()
        
        pl2 = open('list/packages.txt', 'w+')
        for p in pl_:
            package = sub('[ ]+', '>=', p)
            pl2.write(str(package))
        pl2.close()
    print('\n[v] done..')
    
    perg = input('\n[?] Do you want to run the updater right now?\n[y|n]> ')
    
    if perg.upper() == 'Y':
        pipupgrade(_pip_list='list/packages.txt')
    elif perg.upper() == 'N':
        print('\n[i] Thanks then, now check the file list/packages.txt to view all your packages..')
        exit(0)
    else:
        print('\n[x] Invalid choice..\n\tClosing the program!')
        exit(0)
