import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time

os.system("pip install requests")

os.system("clear")

red="\033[0;31m"          # Red

yellow="\033[0;33m"       # Yellow

green="\033[0;32m"        # Green

color_off="\033[0m"       # Text Reset

bblack="\033[1;30m"       # Black

bred="\033[1;31m"         # Red

ured="\033[4;31m"         # Red

on_green="\033[42m"       # Green

blue="\033[0;34m"         # Blue

lightblue = '\033[94m'

red = '\033[91m'

white = '\33[97m'

yellow = '\33[93m'

green = '\033[1;32m'

cyan  = "\033[96m"

end = '\033[0m'

purple="\033[0;35m"

def main():
	os.system("clear")
print("""
                                                                                                                                                                                                                                                                                                                                                                                                                   
   SSSSSSSSSSSSSSS YYYYYYY       YYYYYYYLLLLLLLLLLL             HHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEETTTTTTTTTTTTTTTTTTTTTTT\033[0;32m
 SS:::::::::::::::SY:::::Y       Y:::::YL:::::::::L             H:::::::H     H:::::::HE::::::::::::::::::::ET:::::::::::::::::::::T
S:::::SSSSSS::::::SY:::::Y       Y:::::YL:::::::::L             H:::::::H     H:::::::HE::::::::::::::::::::ET:::::::::::::::::::::T\33[93m
S:::::S     SSSSSSSY::::::Y     Y::::::YLL:::::::LL             HH::::::H     H::::::HHEE::::::EEEEEEEEE::::ET:::::TT:::::::TT:::::T
S:::::S            YYY:::::Y   Y:::::YYY  L:::::L                 H:::::H     H:::::H    E:::::E       EEEEEETTTTTT  T:::::T  TTTTTT
S:::::S               Y:::::Y Y:::::Y     L:::::L                 H:::::H     H:::::H    E:::::E                     T:::::T  \033[0m="\033[1;37m      
 S::::SSSS             Y:::::Y:::::Y      L:::::L                 H::::::HHHHH::::::H    E::::::EEEEEEEEEE           T:::::T        
  SS::::::SSSSS         Y:::::::::Y       L:::::L                 H:::::::::::::::::H    E:::::::::::::::E           T:::::T        
    SSS::::::::SS        Y:::::::Y        L:::::L                 H:::::::::::::::::H    E:::::::::::::::E           T:::::T        
       SSSSSS::::S        Y:::::Y         L:::::L                 H::::::HHHHH::::::H    E::::::EEEEEEEEEE           T:::::T        
            S:::::S       Y:::::Y         L:::::L                 H:::::H     H:::::H    E:::::E                     T:::::T        
            S:::::S       Y:::::Y         L:::::L         LLLLLL  H:::::H     H:::::H    E:::::E       EEEEEE        T:::::T        
SSSSSSS     S:::::S       Y:::::Y       LL:::::::LLLLLLLLL:::::LHH::::::H     H::::::HHEE::::::EEEEEEEE:::::E      TT:::::::TT\033[1;37m     
S::::::SSSSSS:::::S    YYYY:::::YYYY    L::::::::::::::::::::::LH:::::::H     H:::::::HE::::::::::::::::::::E      T:::::::::T      
S:::::::::::::::SS     Y:::::::::::Y    L::::::::::::::::::::::LH:::::::H     H:::::::HE::::::::::::::::::::E      T:::::::::T      
 SSSSSSSSSSSSSSS       YYYYYYYYYYYYY    LLLLLLLLLLLLLLLLLLLLLLLLHHHHHHHHH     HHHHHHHHHEEEEEEEEEEEEEEEEEEEEEE      TTTTTTTTTTT\033[0;34m
                                                                                                                                    
                                                                                                                                    
                                                                                                                                
        GGGGGGGGGGGGG               AAA               NNNNNNNN        NNNNNNNN        GGGGGGGGGGGGG\033[0;35m                                 
     GGG::::::::::::G              A:::A              N:::::::N       N::::::N     GGG::::::::::::G                                 
   GG:::::::::::::::G             A:::::A             N::::::::N      N::::::N   GG:::::::::::::::G                                 
  G:::::GGGGGGGG::::G            A:::::::A            N:::::::::N     N::::::N  G:::::GGGGGGGG::::G                                 
 G:::::G       GGGGGG           A:::::::::A           N::::::::::N    N::::::N G:::::G       GGGGGG                                 
G:::::G                        A:::::A:::::A          N:::::::::::N   N::::::NG:::::G                                               
G:::::G                       A:::::A A:::::A         N:::::::N::::N  N::::::NG:::::G                                               
G:::::G    GGGGGGGGGG        A:::::A   A:::::A        N::::::N N::::N N::::::NG:::::G    GGGGGGGGGG\033[4;31m                               
G:::::G    G::::::::G       A:::::A     A:::::A       N::::::N  N::::N:::::::NG:::::G    G::::::::G                                 
G:::::G    GGGGG::::G      A:::::AAAAAAAAA:::::A      N::::::N   N:::::::::::NG:::::G    GGGGG::::G                                 
G:::::G        G::::G     A:::::::::::::::::::::A     N::::::N    N::::::::::NG:::::G        G::::G                                 
 G:::::G       G::::G    A:::::AAAAAAAAAAAAA:::::A    N::::::N     N:::::::::N G:::::G       G::::G                                 
  G:::::GGGGGGGG::::G   A:::::A             A:::::A   N::::::N      N::::::::N  G:::::GGGGGGGG::::G\033[96m                               
   GG:::::::::::::::G  A:::::A               A:::::A  N::::::N       N:::::::N   GG:::::::::::::::G                                 
     GGG::::::GGG:::G A:::::A                 A:::::A N::::::N        N::::::N     GGG::::::GGG:::G                                 
        GGGGGG   GGGGAAAAAAA                   AAAAAAANNNNNNNN         NNNNNNN        GGGGGG   GGGG\033[0m                                                                                                                                                                                                                                                                                                         
____________________________________________________________
  \33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO
   \033[0;33mGITHUB : \033[1;97mhttps://github.com/Shuvo-BBHH
   WELL COME SYLHET GAMG (IAM NEW MEMBER IN YOUR GRUP)
  LIVE in Sylhet (Read in class 10)
\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU 
____________________________________________________________
""")

CorrectUsername = "Mahdi"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;91m📋 \x1b[1;91mTool Username \x1b[1;91m»» \x1b[1;92m")
    if (username == CorrectUsername):
    	
            loop = 'false'
     	
print("""\033[42m[1] GRUP ADMIN:Radi Ahmed(SYLHET GANG)
\033[0;88m[2] ADMIN FB PAGE :Ahia Ahmed
\033[0;88m[3] DAVOLAPER : MAHDI HASAN SUVO
\033[0;33m[4] CONTRACT ME : 01887408
\033[0;32mPLZ Type Admin\033[0m

""")

pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

if pil in ["01","1"]:
		os.system('xdg-open https://www.facebook.com/Radi.Ahmed.official')
		time.sleep(2)
		print (" ")
		n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
		time.sleep(2)
		main()

elif pil in ["02","2"]:
		os.system('xdg-open https://www.facebook.com/Ahia.Dadu.official')
		time.sleep(2)
		print (" ")
		n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
		time.sleep(2)
		main()

elif pil in ["Admin","ADMIN"]:
	os.system("git clone https://github.com/Shuvo-BBHH/mahdi.2")
	os.system("cd mahdi.2")
	os.system("python mahdi.py")	
		
elif pil in ["03","3"]:
		os.system('xdg-open https://www.facebook.com/mahdihasan.80')
		time.sleep(2)
		print (" ")
		n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
		time.sleep(2)
		main()
