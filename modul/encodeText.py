from base64 import b64encode


# WARNA
netral='\033[0;37m'
merah='\033[1;31m'
hijau='\033[1;32m'
kuning='\033[1;33m'
biru='\033[1;34m'
ungu='\033[1;35m'
cyan='\033[1;36m'

# encode text
def entxt():
	inp = raw_input(cyan+"\nText"+merah+"  : "+netral)
	enc = b64encode(inp)
	print ("{1}Hasil {2}: {3}{0}").format(enc,cyan,merah,hijau)
	print ("")
