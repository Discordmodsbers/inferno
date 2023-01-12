import os
import time 

delay = 2

def cls():
  os.system('clear')

def deleter():
  try:
    for delete in range(10):
      print(f'Deleting {delete}%', end='\r')
      time.sleep(0.5)
    os.system("rm Inferno.py")
    os.system("rm ServerKey.py")
    os.system("rm requirements.txt")
    os.system("rm banner.py")
    return True
  except:
    print("Failed to update please run as sudo !")
    return False
    sys.exit()


def downloader():
  try:
    for download in range(11, 21):
      print(f"Downloading {download}%", end='\r')
      time.sleep(0.5)
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/inferno/main/Inferno.py')
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/inferno/main/ServerKey.py')
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/inferno/main/requirements.txt')
    os.system('curl -LJO https://raw.githubusercontent.com/Discordmodsbers/inferno/main/banner.py')
    return True
  except:
    print("Failed to download !")
    return False
    sys.exit()


def main():
  cls()
  print("""██   ██ ███    ██  ██████  ██   ██ ███████     ██    ██ ██████  ██████   █████  ████████ ███████ ██████  
██  ██  ████   ██ ██    ██  ██ ██  ██          ██    ██ ██   ██ ██   ██ ██   ██    ██    ██      ██   ██ 
█████   ██ ██  ██ ██    ██   ███   ███████     ██    ██ ██████  ██   ██ ███████    ██    █████   ██████  
██  ██  ██  ██ ██ ██    ██  ██ ██       ██     ██    ██ ██      ██   ██ ██   ██    ██    ██      ██   ██ 
██   ██ ██   ████  ██████  ██   ██ ███████      ██████  ██      ██████  ██   ██    ██    ███████ ██   ██ 
                                                                                                         
                                                                                                         """)
  print("[*] Deleting All Files [*]")
  if deleter():
    print("[*] Deleted All Files [*]")
    
  if downloader():
    print("[*] Downloaded everything ! [*]")


main()
