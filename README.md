```
usage: sweethash.py [-h] [-ab APPENDBEGIN] [-af APPEND] [-o OUTPUT] [-n NUMBERS] [-s COMBINATION] [-e EXPONENT] [-t TYPE] [-b]

   ___      __ __ __ __    _____                  _   _               _     
  / _ \    /_ /_ /_ /_ |  / ____|                | | | |             | |    
 | | | | ___| || || || | | (_____      _____  ___| |_| |__   __ _ ___| |__  
 | | | |/ _ \ || || || |  \___ \ \ /\ / / _ \/ _ \ __| '_ \ / _` / __| '_ \ 
 | |_| |  __/ || || || |  ____) \ V  V /  __/  __/ |_| | | | (_| \__ \ | | |
  \___/ \___|_||_||_||_| |_____/ \_/\_/ \___|\___|\__|_| |_|\__,_|___/_| |_|


md5(by firedragon9511 aaaaaaaaaabhpbn)

options:
  -h, --help            show this help message and exit
  -ab APPENDBEGIN, --append-begin APPENDBEGIN
                        append to begin of all payloads.
  -af APPEND, --append APPEND
                        append to final of all payloads.
  -o OUTPUT, --output OUTPUT
                        save output to a file (append).
  -n NUMBERS, --numbers NUMBERS
                        minimum numbers after 0e (default: 1).
  -s COMBINATION, --append-size COMBINATION
                        size of the append responsible for the attempts (default: 15).
  -e EXPONENT, --exponent EXPONENT
                        custom exponent prefix (default: 0+[eE]).
  -t TYPE, --type TYPE  hash algorithm. Available: md5, sha1, sha224,  sha256, sha384, sha512
  -b, --break           break on first magic hash found.

```