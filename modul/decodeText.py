from base64 import b64decode


# WARNA
netral='\033[0;37m'
merah='\033[1;31m'
hijau='\033[1;32m'
kuning='\033[1;33m'
biru='\033[1;34m'
ungu='\033[1;35m'
cyan='\033[1;36m'

# decode text
def detxt():
	inp = raw_input(cyan+"\nKode "+merah+" : "+netral)
	dec = b64decode(inp)
	print ("{1}Hasil {2}: {3}{0}").format(dec,cyan,merah,hijau)
	print ("")