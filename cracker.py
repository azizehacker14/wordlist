#this script by: azrd04
#hello 
#version 8.1.0
import itertools
import os
os.system("clear")









import itertools
import os
os.system("clear")
ban = '''

                         '''
print (" \n\033[1;31m          ▌│█║▌║▌║ [ cracker Facebook ] ║▌║▌║█│▌ ")

print ("  \n\033[1;31m          ▀▄▀▄▀▄ [ BY: AZIZE ABDOU ] ▄▀▄▀▄▀ ")

print (" \n\033[1;31m          ▌│█║▌║▌║ [ SPY NOTE ] ║▌║▌║█│▌")
print ("           ")



scale = input('        \033[31m >> entre any nember "10:10" : ')
start = int(scale.split(':')[0])
final = int(scale.split(':')[1])

use_nouse = str(input("\n\033[1;31m >>> Do you want to enter  information or personel data ? [Y&N]: "))
if use_nouse == 'y':
        first_name = str(input("\n\033[31m[*] ᶠⁱʳˢᵗ ⁿᵃᵐᵉ: "))
        last_name = str(input("\n\033[31m [*] ᴸᵃˢᵗ ᴺᵃᵐᵉ: "))
        birthday = str(input("\n\033[31m[*] ⫷B⫸⫷i⫸⫷r⫸⫷t⫸⫷h⫸⫷d⫸⫷a⫸⫷y⫸: "))
        month = str(input("\n\033[31m[*] ᴹᵒⁿᵗʰ: "))
        year = str(input("\n\033[31m[*] yₑₐᵣ: "))
        chrs = first_name + last_name + birthday + month + year
else:
        chrs = 'abcdefghijklmnopqrstuvwxyz'
        pass

chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

file_name = input('\n\033[31m >> Insert a name for your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[31m >> Do you want to use uppercase characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_up])
if input('\n\033[31m >> Do you want to use special characters? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_specials])
if input('\n\033[31m >> Do you want to use numbers ? (y/n): ') == 'y':
        chrs = ''.join([chrs, chrs_numerics])

for i in range(start, final+1):
        for j in itertools.product(chrs, repeat=i):
                temp = ''.join(j)
                print(temp)
                arq.write(temp + '\n')
arq.close()
