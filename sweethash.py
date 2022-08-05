import itertools
import hashlib
import re
import string
import argparse
from argparse import RawTextHelpFormatter


banner = '''

   ___      __ __ __ __    _____                  _   _               _     
  / _ \    /_ /_ /_ /_ |  / ____|                | | | |             | |    
 | | | | ___| || || || | | (_____      _____  ___| |_| |__   __ _ ___| |__  
 | | | |/ _ \ || || || |  \___ \ \ /\ / / _ \/ _ \ __| '_ \ / _` / __| '_ \ 
 | |_| |  __/ || || || |  ____) \ V  V /  __/  __/ |_| | | | (_| \__ \ | | |
  \___/ \___|_||_||_||_| |_____/ \_/\_/ \___|\___|\__|_| |_|\__,_|___/_| |_|
                                                                            

md5(by firedragon9511 aaaaaaaaaabhpbn)
'''

parser = argparse.ArgumentParser(description=banner, formatter_class=RawTextHelpFormatter)

parser.add_argument('-ab','--append-begin', dest='appendbegin', action='store', type=str, help='append to begin of all payloads.', required=False, default='')
parser.add_argument('-af','--append', dest='append', action='store', type=str, help='append to final of all payloads.', required=False, default='')
parser.add_argument('-A','--Append', dest='Append', action='store', type=str, help='append to final of all payloads using a wordlist.', required=False)
parser.add_argument('-o','--output', dest='output', action='store', type=str, help='save output to a file (append).', required=False)
parser.add_argument('-n','--numbers', dest='numbers', action='store', type=str, help='minimum numbers after 0e (default: 1).', required=False, default=1)
parser.add_argument('-e','--exponent', dest='exponent', action='store', type=str, help='custom exponent prefix (default: 0+[eE]).', required=False, default='0+[eE]')
parser.add_argument('-t','--type', dest='type', action='store', type=str, help='hash algorithm.', required=False, default='md5')


parser.add_argument('-b','--break', dest='breakloop', help='break on first magic hash found.', action='store_true')

args = parser.parse_args()

regex_match_notation = r'^0+[eE]\d+'
#regex_match_notation_template = '^0+[eE]\d{<AMOUNT>}'
regex_match_notation_template = '^<EXPONENT>\d{<AMOUNT>}'

regex_match_notation_template = regex_match_notation_template.replace('<AMOUNT>', str(args.numbers)).replace('<EXPONENT>', args.exponent)

file = None
if args.output is not None:
    file = open(args.output, 'a+')
#print(regex_match_notation_template)

def prnt(payload, code):
    full = args.appendbegin + code + args.append
    print('---------- payload found -----------')
    print('| Payload: ' + full)
    print('| Append Begin: ' + args.appendbegin)
    print('| Append End: ' + args.append)
    print('| Full Hash: ' + payload)
    print('| Notation Payload: ' + re.search(regex_match_notation_template, payload)[0])
    print('| Type Juggling Syntax: hash(%s) == 0' % (full) )
    print('------------------------------------------------------')

    if args.output is not None:
        file.write( full + '\n')

def digest(txt):
    result = ''
    if args.type == 'md5':
        result = hashlib.md5(txt.encode()).hexdigest()
    if args.type == 'sha256':
        result = hashlib.sha256(txt.encode()).hexdigest()

    return result

def find_magic_hash():
    x=0
    # for i in range(0,50):
    char=itertools.product(string.ascii_lowercase,repeat=int(15))
    for pin in char:
        code =''.join(pin)
        hash = digest(args.appendbegin + code + args.append) #hashlib.md5((args.appendbegin + code + args.append).encode()).hexdigest()
        #if args.exponent in hash:
        if re.match(regex_match_notation_template, hash):
            prnt(hash, code)
            if args.breakloop:
                break

find_magic_hash()


if file is not None:
    file.close()