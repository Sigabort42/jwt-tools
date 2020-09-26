#!/usr/bin/env python3

import jwt
import sys
import os
import base64
import json

if len(sys.argv) < 3 or sys.argv[1] == "-h":
    print("USAGE: jwt.py <string_encode> <file_password.lst>")
    sys.exit(1)

password_file = os.path.abspath(sys.argv[2])
header, payload, signature = sys.argv[1].split(".")

print("\033[1mfile:\033[0m", password_file)
print("\033[1mheader:\033[0m", header)
print("\033[1mpayload:\033[0m", payload)
print("\033[1msignature:\033[0m", signature)

decode_header = json.loads(base64.b64decode(header))

typ = decode_header["typ"]
alg = decode_header["alg"]

print("\n\ntyp: \033[93m{}\033[0m\nalg: \033[93m{}\033[0m\n".format(typ, alg))

input("Press enter for continue $>")

with open(password_file, 'r') as fd:
    words = fd.readlines()
    for word in words:
        try:
            print("\033[92mSUCESS:", word, jwt.decode(sys.argv[1], word.strip(), algorithms=alg), "\033[0m")
            sys.exit(0)
        except Exception as err:
            print("TRYING WORD:\033[91m", word, "\033[0m")
