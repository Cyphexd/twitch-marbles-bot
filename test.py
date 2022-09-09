import sys, getopt
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter




def main(argv):
    irc_token = ''
    client_id = ''
    nick = ''
    prefix = ''
    initial_channels = ''

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-t", "--token")
    parser.add_argument("-c", "--clientid")
    parser.add_argument("-n", "--nick")
    parser.add_argument("-p", "--prefix")
    parser.add_argument("-cl", "--channel")
    args = vars(parser.parse_args())

    print(args["token"])
    print(args["clientid"])
    print(args["nick"])
    print(args["prefix"])
    print(args["channel"])

if __name__ == "__main__":
   main(sys.argv[1:])
