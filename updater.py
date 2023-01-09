import os
import time 

delay = 2


def deleter():
  try:
    for delete in range(10):
      print(f'Deleting {delete}%', end='\r')
      time.sleep(0.5)
    os.system("rm main.py")
    os.system("rm ServerKey.py")
    os.system("rm requirements.txt")
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
    os.system('git clone https://github.com/Discordmodsbers/inferno')
    os.system('pip install -r requirements.txt')
    return True
  except:
    print("Failed to download !")
    return False
    sys.exit()


def main():
  if deleter():
    print("[*] Deleted All Files [*]")
    
  if downloader():
    print("[*] Downloaded everything ! [*]")


main()
