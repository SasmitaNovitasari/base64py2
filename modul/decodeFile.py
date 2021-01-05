import platform
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

# decode file
def decode():
	cek()
	# menampilkan semua file
	print ("""
{0}  File python yang ditemukan
{1}==============================
{2}""").format(hijau,kuning,netral)
	s("ls | grep .py")

	# mengambil input
	inp = raw_input(cyan+"\nNama File"+merah+" : "+netral)
	# membaca isi file
	f = open(inp, "rb").read()
	# mengubah exec menjadi print
	n = f.replace("exec", "print")
	# menulis hasil n di file in.py
	open("in.py", "wb").write(n)
	# menulis file di fe-hasil.py
	# fungsi > menulis di file dan menghapus tulisan lama
	s("echo '# ========== Decode By Fe-Ivander! ==========' > fe-hasil.py")
	# fungsi >> menambah text di akhir file
	s("echo '# Kunjungi github fe-ivander' >> fe-hasil.py")
	# menambah di akhir file
	s("python2 in.py >> fe-hasil.py")
	# menghapus file in.py
	s("rm in.py")
	# petunjuk
	print ("\n{0}[{2}!{0}] Hasil disimpan di file fe-hasil.py\n").format(hijau, merah, kuning)
