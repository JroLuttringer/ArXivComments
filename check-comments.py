import requests 
import sys 
import os
import glob

doi = sys.argv[1]

URL = "https://arxiv.org/e-print/{}".format(doi)
response = requests.get(URL)

open("paper-{}".format(doi), "wb").write(response.content)
os.system("mkdir untar-paper-{}".format(doi))
os.system("tar -xvf paper-{} -C untar-paper-{}".format(doi,doi))

os.chdir("untar-paper-{}".format(doi))
for file in glob.glob("**/*.tex", recursive=True):
	print("-----"+file+"-----")
	with open(file) as f:
		for l in f.readlines():
			if l.strip().startswith("%"):
				print(l)




