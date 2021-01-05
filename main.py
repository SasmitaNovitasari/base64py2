# Creayed Bye Fransisco Ezra Ivander
# Visit my github fe-ivander
# Python 2

import os
import sys
import platform
from time import sleep as t
from os import system as s
# import file
from modul import encodeText
from modul import decodeText
from modul import encodeFile
from modul import decodeFile



# WARNA
netral='\033[0;37m'
merah='\033[1;31m'
hijau='\033[1;32m'
kuning='\033[1;33m'
biru='\033[1;34m'
ungu='\033[1;35m'
cyan='\033[1;36m'

# FUNGSI

# utk restart program
def restart():
	python = sys.executable
	os.execl (python, python, *sys.argv)

# cek OS
def cek():
	os = platform.system()
	# clear screen linux/windows
	if os == "Linux":
	    s("clear")
	elif os == "win32":
	    s("CLS")


# MULAI MENGGUNAKAN FUNGSI
cek()

print ("""
{2}+-------------------------------------+
|  {4}             Python 2           {2}   |
|  {1}            Fe-Ivander   {2}          |
+-------------------------------------+

{3}Menu{0} :
{1}[{4}1{1}] {2}Encode Text
{1}[{4}2{1}] {2}Decode Text
{1}[{4}3{1}] {2}Encode File
{1}[{4}4{1}] {2}Decode File

{1}[{0}0{1}] {2}Exit
""").format(merah, kuning, hijau, biru, cyan, ungu, netral)

try :
	inp = input(biru+"#Nomor"+merah+" : "+netral)
	if inp == 1:
		encodeText.entxt()
	elif inp == 2:
		decodeText.detxt()
	elif inp == 3:
		encodeFile.encode()
	elif inp == 4:
		decodeFile.decode()
	elif inp == 0:
		s("exit")
		print ("\nGood Bye!\n")
	else:
		print ("\nMenu tidak ada!\n")
		t(1)
		restart()

except KeyboardInterrupt:
	print ("""
[!] Terimakasih sudah menggunakan script ini;)
""")

except SyntaxError:
	print ("""
[!] Input tidak dapat diterima!
""")

except NameError:
	print ("""
[!] Masukan angka yang benar!
""")
	t(2) # sleep 2 dtk
	restart()
	
except IOError:
	print("\nNama file tidak ada!\n")
