import os, os.path, urllib.request, hashlib, optparse, subprocess

PLUGIN_URL= "http://advancedcombattracker.com/includes/page-download.php?id=66"
PLUGIN_PATH = "FFXIV_ACT_Plugin.dll"

def check_hash():
	remote = urllib.request.urlopen(PLUGIN_URL)
	remote_hash = hashlib.md5()
	print("Checking for updates...")
	
	while True:
		data = remote.read(4096)
		if not data:
			break
		remote_hash.update(data)
	
	local_hash = hashlib.md5(PLUGIN_PATH.encode('utf-8')).hexdigest()
	
	return remote_hash == local_hash

def main():
	try:
		if not os.path.isfile(PLUGIN_PATH):
			urllib.request.urlretrieve(PLUGIN_URL, PLUGIN_PATH)
			start_act()
			raise SystemExit

		if check_hash() != True:
			print("Downloading...")
			os.remove(PLUGIN_PATH)
			urllib.urlretrieve(PLUGIN_URL, PLUGIN_PATH)
			start_act()
			raise SystemExit
	except:
		start_act()
		raise SystemExit

def start_act():
	os.startfile('"Advanced Combat Tracker.exe"')
	
if __name__ == '__main__':
	main()
