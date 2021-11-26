import sys
import hashlib
from colorama import init, Fore

init()

def calculatechecksum(file):
    f = open(file, 'rb')
    hash = hashlib.sha256()
    hash.update(f.read())
    checksum = hash.hexdigest()
    print(Fore.GREEN + f'SHA256 checksum for {sys.argv[1]}: {checksum}')

def menu():
    try:
        if sys.argv[1]:
            args = sys.argv[1]
            calculatechecksum(args)
    except:
        print(Fore.RED + f'Usage: python3 {sys.argv[0]} [filename]')

menu()
