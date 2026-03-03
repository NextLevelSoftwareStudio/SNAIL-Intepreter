import subprocess, sys
from pathlib import Path
def creatingFile(file, text: str):
    oi = Path(file)
    if oi.exists() and oi.is_file():
        p = input(f"Do you want do delete {oi}?")
        if p == "y":
            print(f"Deleting file {oi}.")
            oi.unlink()
            print(f"The file {oi} was deleted.")
            print(f"Creating file {oi}.")
            with open(file, "w") as file:
                file.write(text)
            print(f"The file {oi} was created.")
        elif p == "n":
            print("Closing the installer, because the ")
            sys.exit(0)
        else:
            sys.exit(1)
    elif oi.exists() is False:
        with open(file, "w") as file:
            file.write(text)
    else:
        sys.exit(1)
def creatingFolder(folder):
    oi = Path(folder)
    if oi.exists() and oi.is_dir():
        p = input(f"Do you want do delete the folder {oi}?")
        if p == "y":
            oi.unlink()
            oi.mkdir()
        elif p == "n":
            sys.exit(0)
        else:
            sys.exit(1)
    elif oi.exists() is False and oi.is_dir() is False:
        oi.mkdir()
    else:
        sys.exit(1)
print("Welcome to the SNAIL 1.0.0 Interpreter Installer.")
a = input("Do you want to install SNAIL 1.0.0 Interpreter? (y/n)")
if a == "y":
    print("Installing SNAIL 1.0.0 Interpreter.")