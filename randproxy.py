import random
import requests
import time
import os

proxies_list = ["200.164.128.236:8080","92.118.27.193:80","170.79.88.113:999","200.24.203.131:999","190.109.161.124:999","206.253.164.146:80","103.241.182.97:80","103.214.109.66:80","120.220.220.95:8085","47.57.188.208:80","167.249.31.104:999","165.154.92.146:8888","156.200.116.73:1976","179.49.161.74:999","121.1.41.162:111","117.54.114.98:80","62.182.114.164:60731","122.232.146.32:8085","85.214.23.160:8000","31.204.172.176:8080","112.246.105.237:8888","185.38.32.157:39121","103.197.251.202:80","222.64.95.60:9000","164.70.72.55:3128","103.153.230.2:80","183.89.163.227:8080","114.250.173.66:7890","118.140.160.85:80","223.27.194.66:63141","36.37.139.2:43997","218.89.224.8:3128","170.155.5.235:8080","95.217.102.133:3128","51.91.157.66:80","62.182.66.150:9090","177.38.76.153:8080","138.186.3.46:8080","168.90.29.214:3128","34.124.138.205:8080","176.48.29.152:8080","194.233.69.90:443","20.122.24.174:80","45.236.170.62:999","45.225.184.177:999","45.185.126.133:8080","61.7.141.30:8080","103.148.192.75:8080","120.34.160.219:4216","187.216.90.46:53281"]

def LoadUserAgents():
	uafile="user_agents.txt"
	uas = []
	with open(uafile,'rb') as uaf:
		for ua in uaf.readlines():
			if ua:
				uas.append(ua.strip()[1:-1-1])
	random.shuffle(uas)
	return uas

uas = LoadUserAgents()

def OpenUrl():
	ua = random.choice(uas)
	
	headers = {
    "Connection" : "close",  # another way to cover tracks
    "User-Agent" : ua}
	proxyRand = random.choice(proxies_list)
	proxies = {
		'http': proxyRand
	}
	if "https" in proxyRand:
		proxies = {
			'https': proxyRand
		}
	print("Proxy selected : ");
	print(proxyRand);
	#params = {"t" : "MTQ2MDIwNw=="}
	#r = requests.get('https://iplogger.org/2eWgZ6', proxies=proxies,params=params)	
	try:	
		r = requests.get('https://www.youtube.com/watch?v=NnOZml3nKvk', proxies=proxies, timeout=5) # 10 seconds
		print(proxies);
		print(ua)
		print(r)
	except requests.exceptions.ProxyError:
		pass
	except requests.exceptions.ConnectTimeout:
		pass
	else:
		# success, break loop
		pass
	time.sleep(0.3)

for i in range(10000) : # Edit 3 with your no. of viwes 
    OpenUrl()