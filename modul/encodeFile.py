import platform
from base64 import b64encode
from os import system as s


# WARNA
netral='\033[0;37m'
merah='\033[1;31m'
hijau='\033[1;32m'
kuning='\033[1;33m'
biru='\033[1;34m'
ungu='\033[1;35m'
cyan='\033[1;36m'

# cek OS
def cek():
	os = platform.system()
	# clear screen linux/windows
	if os == "Linux":
	    s("clear")
	elif os == "win32":
	    s("CLS")

# encode file
def encode():
	cek()
	# menampilkan semua file
	print ("""
{0}  File python yang ditemukan
{1}==============================
{2}""").format(hijau, kuning, netral)
	s("ls | grep .py")


	# mengambil nama file
	inp = raw_input(cyan+"\nNama File"+merah+" : "+netral)
	# membaca file
	f = open(inp, "rb").read()
	# encode isi file
	enc = b64encode(f)
	# isi file untuk hasil
	txt = """
# Encode Bye Fe-Ivander
# Kunjungi github fe-ivander
import base64
exec (base64.b64decode('{}'))
""".format(enc)
	# menulis file
	hasil = open("fe-"+inp, "wb").write(txt)
	# petunjuk
	print ("\n{1}[{3}!{1}]{2} Hasil disimpan di fe-{0}\n").format(inp, hijau, kuning, merah)
