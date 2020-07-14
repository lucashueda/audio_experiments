## This code aims to debug the argparse usage

import argparse

# Command line argparse arguments

parser = argparse.ArgumentParser(description='Argparser debug example')

# Testing string argument
parser.add_argument('--name', default = 'Name argument', type = str, metavar = 'N', 
                    help = 'Name is the name argument')
# Testing integer argument (when i tried a float number it giver an "not int error" so its working)
parser.add_argument('--value', default = 1, type = int, metavar = 'V', 
                    help = 'Value is a int variable')
# Testing required parameter
parser.add_argument('--experiment', required = True, type = str, metavar = 'EN', 
                    help = 'The name of experiments (required)')

args = parser.parse_args()

print(args.name, args.value)