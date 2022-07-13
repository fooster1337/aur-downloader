# aur downloader by @fooster1337/github.com


import os, time, requests
from pathlib import Path
import argparse
from colorama import Fore

# you can change this if you want.
folder_saved = "aur-download"

def banner():
    x = '''
    Aur Arch Downloader | Fooster1337
    fooster1337.net    
'''

    print(x)

def check_files():
    print("[!] Checking Folder [{}]...".format(folder_saved))
    file = Path(folder_saved)
    if file.is_dir():
        print("[+] Folder Found..")
        time.sleep(2)
    else:
        print("[-] Folder Not Found ...\n[+] Creating {} Folder ...".format(folder_saved))
        os.mkdir(folder_saved)
        time.sleep("2")
        print("[+] Created succes! ...")
        print("[+] Run again ...")

def main():
    parser = argparse.ArgumentParser(description="Automatic Aur Downloader, use python3 aur.py <AurPackage>")
    parser.add_argument("aur", metavar="AurPackage", help="For Downloading Package From Aur")
    args = parser.parse_args()
    return aur_downloader(args.aur)

def aur_downloader(package_name):
    check_files()
    os.system("clear")
    banner()
    
    package = 'https://aur.archlinux.org/{}.git'.format(package_name)
    cek = 'https://aur.archlinux.org/packages/{}'.format(package_name)

    print("? > Checking Package {}".format(package_name))
    r = requests.get(cek)
    if r.status_code == 200:
        print(Fore.GREEN + "+ > " + Fore.WHITE + "Package {} Found! ...".format(package_name))
        print(Fore.GREEN + "+ > " + Fore.WHITE + "Downloading {} ...".format(package_name))
        os.system("git clone {} {}/{}".format(package, folder_saved, package_name))
        print(Fore.GREEN + "+ > " + Fore.WHITE + "Installing {}.git".format(package_name))
        os.system("cd {}/{} && makepkg -si".format(folder_saved, package_name))
        print(Fore.GREEN + "+ > " + Fore.WHITE + "Install {} success ...".format(package_name))
    else:
        print(Fore.RED + "! > " + Fore.WHITE + "Packages {} Not Found, please cek again.".format(package_name))
        exit()


if __name__ == "__main__":
    try:
        main()
    except:
        pass