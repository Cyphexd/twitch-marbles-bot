
from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser
import os
from subprocess import call



parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
parser.add_argument("-c", "--clientid")
parser.add_argument("-p", "--prefix", default='!')
parser.add_argument("-cl", "--channel")
parser.add_argument("-co", "--counter", default=5)
parser.add_argument("-rnd", "--random", default=5)
args = vars(parser.parse_args())

with open("accounts.txt") as fp:
    for line in fp:
        #print("{}".format(line.strip().split(':')))
        auth = "oauth:{}".format(line.strip().split(':')[1])
        username = line.strip().split(':')[2]
        #os.system('python ./bot.py --token oauth:q700jqd2hydtuggr0ur0crgv6w7uog --clientid un5z8un90tjw79zd9y7cj7ikp7wztg --nick pexwork --prefix ! --channel voxelboxstudiosm --counter 2 --random 5')
        #call(["python", "bot.py", "-t oauth:q700jqd2hydtuggr0ur0crgv6w7uog --clientid un5z8un90tjw79zd9y7cj7ikp7wztg --nick pexwork --prefix ! --channel voxelboxstudiosm --counter 2 --random 5"])
        os.system("start cmd /C python ./bot.py --token {} --clientid {} --nick {} --prefix {} --channel {} --counter {} --random {}".format(auth, args["clientid"], username, args["prefix"], args["channel"],  args["counter"],  args["random"]))
        #print(auth)
        #print(username)

