#
# Python fake visitos script
#
# Original Authors: Dhananjay Khairnar <khairnardm@gmail.com>
# Date : 29/12/2021
# Country : <Maharashtra>India
#
# This script create fake hits to target URL. You need list of proxy servers. Add
# Proxy servers url in proxy_list.txt. Url shout be lise separated. Proxy server 
# url should be consist of port number.
# Not sure works with sites like youtube.
# run script with two arguments "python fakevisitor.py --n 1000 --u https://www.youtube.com/watch?v=NnOZml3nKvk"  

import random
import requests
import time
import os
import argparse
import signal
import sys
style= ['\033[31m','\033[32m','\033[33m','\033[34m','\033[35m','\033[36m','\033[37m','\033[4m','\033[0m']
	
userAgentList = []
proxiesList = []
numberOfHits = 0
targetUrl = ""
def signal_handler(sig, frame):
	os.system('cls' if os.name=='nt' else 'clear')
	print(random.choice(style))
	print(' Subscribe to my channel https://www.youtube.com/c/ZenElectro_youtube.')
	print(' Please follow me on github.com https://github.com/8-DK.')	
	print(' Oops.. I drop my palette. Good Bye.')	
	sys.exit(0)
	
def LoadUserAgents():
	uafile="user_agents.txt"
	uas = []
	with open(uafile,'r') as uaf:
		for ua in uaf.readlines():
			if ua:
				uas.append(ua.strip()[1:-1-1])
	random.shuffle(uas)
	return uas

def LoadProxyList():
	plfile="proxy_list.txt"
	pls = []
	with open(plfile,'r') as plf:
		for pa in plf.readlines():
			if pa:
				pls.append(pa.strip()[1:-1-1])
	random.shuffle(pls)
	return pls

userAgentList = LoadUserAgents()
proxiesList = LoadProxyList()

def OpenUrl():	
	global targetUrl
	ua = random.choice(userAgentList)
	
	headers = {
	"Connection" : "close",  # another way to cover tracks
	"User-Agent" : ua}
	proxyRand = random.choice(proxiesList)	
	proxies = {
		'http': proxyRand
	}
	if "https" in proxyRand:
		proxies = {
			'https': proxyRand
		}
	print("User Agent selected : ",ua);	
	print("Proxy selected : ",proxyRand);	
	#params = {"t" : "MTQ2MDIwNw=="}
	#r = requests.get(targetUrl, proxies=proxies,params=params)	
	try:	
		r = requests.get(targetUrl, proxies=proxies, timeout=5) # 10 seconds
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
	#time.sleep(0.3)

def main():
	signal.signal(signal.SIGINT, signal_handler)
	global numberOfHits
	global targetUrl
	parser = argparse.ArgumentParser()
	parser.add_argument("--n", type=int, help="Number of hits, Number of time visit URL.",default=1000)
	parser.add_argument("--u", type=str, help="URL to be visit.",default='https://www.youtube.com/watch?v=NnOZml3nKvk')
	args = parser.parse_args()
	if args.u is None:
		print("Please provide target URL which you want to hit.")
		quit()	
	numberOfHits = args.n
	targetUrl = args.u
	print(" Number of hit : ",numberOfHits)
	print(" URL : ",targetUrl)
	print('')
	time.sleep(2)
	for i in range(numberOfHits) : # Edit 3 with your no. of viwes 
		print("==== Request :",i," ====")
		OpenUrl()
		print("=======================")
		print("")
	
if __name__=="__main__":
	main()	