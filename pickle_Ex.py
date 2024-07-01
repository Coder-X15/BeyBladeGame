import pickle
import os

os.chdir(".\sources\profiles")

filelist = [i for i in os.walk("./")]

for file in filelist[0][2]:
    print(file)
    smth = open(file)
    try:
        while True:
            print(pickle.load(smth))
    except:
        pass
    