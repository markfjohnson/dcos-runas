#!/user/bin/python
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o","--output", help="Output File name", required=True)
args = vars(parser.parse_args())
print (args['output'])
print("Writing file to {}".format(args['output']))
fo = open(args['output'], "w")
fo.write("Hello world")

fo.close()
print("File written")