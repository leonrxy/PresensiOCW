from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import os
from datetime import date
import telebot
from colorama import init
from colorama import Fore, Style
init(autoreset=True)

loginocw="https://ocw.uns.ac.id/saml/login"
agama="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM05qaz0%3D&dosen=UlV4Sk1EQXk%3D&kelas=UkE9PQ%3D%3D"
pancasila="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM09EQT0%3D&dosen=U1ZKWE1EQXg%3D&kelas=UWc9PQ%3D%3D"
bindo="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM09ERT0%3D&dosen=UVZKSk1ETTU%3D&kelas=UWc9PQ%3D%3D"
evp="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM09UTT0%3D&dosen=VUVGU01ERTE%3D&kelas=UWc9PQ%3D%3D"
ldti="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM09UUT0%3D&dosen=UmtWT01EQXg%3D&kelas=UWc9PQ%3D%3D"
ppi="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM09UYz0%3D&dosen=VGtGT01EQTU%3D&kelas=UWc9PQ%3D%3D"
pkom="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjNE1UVT0%3D&dosen=U0VGU01ESTI%3D&kelas=UWc9PQ%3D%3D"
jarkom="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjNE1UWT0%3D&dosen=UVVKRU1EQTA%3D&kelas=UWc9PQ%3D%3D"
pjarkom="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjNE1UYz0%3D&dosen=UVVKRU1EQTA%3D&kelas=UWc9PQ%3D%3D"
algo="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM09UVT0%3D&dosen=VTBGSU1EQXk%3D&kelas=UWc9PQ%3D%3D"
palgo="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjM09UWT0%3D&dosen=UVVkVk1ESXk%3D&kelas=UWc9PQ%3D%3D"
minfor="https://ocw.uns.ac.id/presensi-online-mahasiswa/view-mbkm?mk=T1RjNE1UUT0%3D&dosen=U0VGU01ESTI%3D&kelas=UWc9PQ%3D%3D"
email = "leonardusreka"
password = "kawatan19"

#Header
def header():
	print(Fore.LIGHTBLUE_EX+"======================================================================================")
	print(Fore.LIGHTBLUE_EX+"| d8888b.  .d88b.  d888888b       .d88b.   .o88b. db   d8b   db                      |")
	print(Fore.LIGHTBLUE_EX+"| 88  `8D .8P  Y8. `~~88~~'      .8P  Y8. d8P  Y8 88   I8I   88            _   ___   |")
	print(Fore.LIGHTBLUE_EX+"| 88oooY' 88    88    88         88    88 8P      88   I8I   88   /\   /\ / | / _ \  |")
	print(Fore.LIGHTBLUE_EX+"| 88~~~b. 88    88    88         88    88 8b      Y8   I8I   88   \ \ / / | || | | | |")
	print(Fore.LIGHTBLUE_EX+"| 88   8D `8b  d8'    88         `8b  d8' Y8b  d8 `8b d8'8b d8'    \ V /  | || |_| | |")
	print(Fore.LIGHTBLUE_EX+"| Y8888P'  `Y88P'     YP          `Y88P'   `Y88P'  `8b8' `8d8'      \_/   |_(_)___/  |")
	print(Fore.LIGHTBLUE_EX+"===================================== By leonrxy =====================================")    

	print(Fore.LIGHTYELLOW_EX + "BOT Auto Send Reminder Absensi")                                               

#BOT TELE
TOKEN = "5665087358:AAH6u4e2vTWjpMxFF6js5KesCwi2KPBLa-M"
chat_id="818406813"
tb = telebot.TeleBot(TOKEN)
def kirimPesan(text):
    tb.send_message(chat_id, text)

def time_in_range(start, end, current):
    """Returns whether current is in the range [start, end]"""
    return start <= current <= end

def Login():
	driver.get((loginocw))
	wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="btn btn-primary btn-block btn-flat"]')))
	# Mengisi Email dan Password
	driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(email)
	driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(password)
	driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary btn-block btn-flat"]').click()
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '[class="nav navbar-nav navbar-right"]')))

def CekAbsen(matkul,nama,i):
	#Cek Absen Matkul
	wait = WebDriverWait(driver, timeout=10)
	driver.get((matkul))
	try:
		wait.until(EC.presence_of_element_located((By.XPATH, "(//div[@class='panel panel-default'])[1]")))
		warna = driver.find_element(By.XPATH, "(//div[@class='panel panel-default'])[1]").get_attribute("style")
		tanggal = driver.find_element(By.TAG_NAME, "small").text
		pertemuan = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/p[1]").text
		jam = driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/small[2]").text
		today = date.today()
		waktu = jam.split(" - ")
		start = waktu[0]
		end = waktu[1]
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		current = current_time
		if time_in_range(start, end, current) == True and tanggal == today and loop%5==0:
			pesan = "======= PERINGATAN PRESENSI =======\nMatkul = " + nama +" \n" + tanggal + "\n" + pertemuan+"\nJam " + jam+"\n"
			kirimPesan(pesan)
			print(Fore.LIGHTYELLOW_EX + "Pesan Telegram Telah Terkirim!")
		if warna == "background: rgb(248, 187, 208);":
			print(Fore.LIGHTRED_EX+ Style.BRIGHT + "Terdapat absensi baru!")
			if loop%20==0:
				statusLoop[i]=0
			if statusLoop[i]==0:
				if tanggal == today:
					pesan = "======= ABSENSI HARI INI =======\nMatkul = " + nama +" \n" + tanggal + "\n" + pertemuan+"\nJam " + jam+"\n"
					kirimPesan(pesan)
					print(Fore.LIGHTYELLOW_EX + "Pesan Telegram Telah Terkirim!")
					statusLoop[i]=1
		elif warna == "background: rgb(200, 230, 201);":
			print(Fore.LIGHTGREEN_EX + "Tidak ada absensi baru")
	except TimeoutException:
		print("Absensi Tidak ditemukan")
	
def Close():
	driver.close()

listMatkul = ['Agama','Pancasila','Bahasa Indonesia','EVP','Literasi Data & Teknologi Informasi','Penulisan Ilmiah','Praktik Komputasi','Teori Jaringan Komputer','Praktik Jaringan Komputer','Algoritma','Praktik Algoritma','Matematika Informatika']
linkMatkul = [agama,pancasila,bindo,evp,ldti,ppi,pkom,jarkom,pjarkom,algo,palgo,minfor]
daftarMatkul = ["agama","pancasila","bindo","evp","ldti","ppi","pkom","jarkom","pjarkom","algo","palgo","minfor"]
statusLoop = [0,0,0,0,0,0,0,0,0,0,0,0]
loop=0

while True:
	loop+=1
	osname = os.name
	if osname == 'nt':
		os.system('cls')
	else:
		os.system('clear')
	header()
	options = webdriver.ChromeOptions()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
	wait = WebDriverWait(driver, timeout=10)
	Login()
	for i in range(len(listMatkul)):
		t = time.localtime()
		current_time = time.strftime("%H:%M:%S", t)
		print(Fore.LIGHTMAGENTA_EX+"["+current_time+"] "+Fore.LIGHTBLUE_EX + "Mengecek Absensi Matkul {}".format(listMatkul[i])+"...")
		CekAbsen(linkMatkul[i],listMatkul[i],i)
		print("========================================")
		time.sleep(3)
	Close()
	print(Fore.LIGHTYELLOW_EX + "Pause 5 Menit...")
	time.sleep(300)
	if loop==1000:
		loop=0
