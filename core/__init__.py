from os import chdir, makedirs, path
from re import sub
from subprocess import getoutput
from time import sleep


def genlist():
    try:
        makedirs("list", exist_ok=True)
        lista = getoutput("pip list")

        # *****************************************
        with open("list/packages.txt", "w+") as pl:
            pl.write(lista)
            pl.close()

        # *****************************************
        with open("list/packages.txt", "r+") as pl:
            pl_ = pl.readlines()
            for _ in range(2):
                pl_.remove(pl_[0])
            pl.close()

            # *****************************************
            pl2 = open("list/packages.txt", "w+")
            for p in pl_:
                package = sub("[ ]+", ">=", p)
                pl2.write(str(package))
            pl2.close()
    except Exception as error:
        return error
    return "Done, Packages list generated successfully!"


def updpackages():
    if path.exists("list/packages.txt"):
        chdir("list")
        return getoutput("pip install --upgrade -r packages.txt")
    return "Error, list of packages not available!\n- Please, run (Generate List) first.."


def installnew(_package_name: str):
    return getoutput(f"pip install {_package_name}")
