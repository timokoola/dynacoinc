
from pymarkovchain import MarkovChain
from twython import Twython
from PIL import Image
import codecs
import StringIO
import random
import os
import argparse

class TwythonHelper:

    def __init__(self, keyfile):
        f = open(keyfile)
        lines = f.readlines()
        f.close()
        consumerkey = lines[0].split("#")[0]
        consumersecret = lines[1].split("#")[0]
        accesstoken = lines[2].split("#")[0]
        accesssec = lines[3].split("#")[0]

        self.api = Twython(consumerkey, consumersecret, accesstoken, accesssec)

if __name__ == '__main__':
	api = (TwythonHelper("dynacoinc.keys")).api
	mc = MarkovChain("./markov")
	f = codecs.open("corpus.txt")
	text = " ".join(f.readlines())
	f.close()
	mc.generateDatabase(text)
	status = mc.generateString()

	if len(status) > 110:
		status = status[:110]
		lr = status.rfind(" ")
		status = status[:lr] + "."
	else:
		status = status + "."

	r = random.Random()
	lf = os.listdir(".")
	ll = [l for l in lf if l.find("jpg") != -1]

	photo = open(r.choice(ll), "rb")

	api.update_status_with_media(media=photo, status=status)