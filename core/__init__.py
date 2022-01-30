from os import chdir, makedirs, path
from re import sub
from subprocess import getoutput
from time import sleep


def genlist():
    makedirs("list", exist_ok=True)
    lista = getoutput("pip list")
    sleep(0.2)

    # *****************************************
    with open("list/packages.txt", "w+") as pl:
        pl.write(lista)
        pl.close()
        sleep(0.2)

    # *****************************************
    with open("list/packages.txt", "r+") as pl:
        pl_ = pl.readlines()
        for _ in range(2):
            pl_.remove(pl_[0])
        pl.close()
        sleep(0.2)

        # *****************************************
        pl2 = open("list/packages.txt", "w+")
        for p in pl_:
            package = sub("[ ]+", ">=", p)
            pl2.write(str(package))
        pl2.close()
        sleep(0.2)
    return "Done, list generated successfuly!"


def updpackages():
    if path.exists("list/packages.txt"):
        chdir("list")
        return getoutput("pip install --upgrade -r packages.txt")
    return "Error, list of packages not available!\n- Please, run (Generate List) first.."


def installnew(_package_name: str):
    return getoutput(f"pip install {_package_name}")
