from bs4 import BeautifulSoup
import requests
import json
import time
from nordvpnzwitch import initialize_VPN,rotate_VPN,terminate_VPN

#retrieve standard server list and pass to dict
serverlist =  BeautifulSoup(requests.get("https://nordvpn.com/api/server").content,"html.parser")
site_json=json.loads(serverlist.text)
filtered_servers = {key: [] for key in ['windows_names','linux_names']}
for specific_dict in site_json:
	try:
		if specific_dict['categories'][0]['name'] == 'Standard VPN servers':
			filtered_servers['windows_names'].append(specific_dict['name'])
			filtered_servers['linux_names'].append(specific_dict['domain'].split('.')[0])
	except IndexError:
		pass

#Filter servers by country name. Replace windows_names with linux_names if you're working on Linux
servers_id = [x for x in filtered_servers['windows_names'] if 'Indonesia' in x] 

#test
initialize_VPN(save=1,area_input=servers_id)
time.sleep(8)
for i in range(3):
    rotate_VPN()
    time.sleep(5)