#!/usr/bin/env python3

from getpass import getpass
import json
import os
import sys
from subprocess import run

from config import *

def main(cmd):

  cmds = {k.split('_')[-1] : v for (k, v) in globals().items() if k.startswith('_cmd_')}
  if cmd not in cmds:
    raise ValueError

  os.chdir(os.path.dirname(os.path.realpath(__file__)))
  cmds[cmd]()

def _cmd_encrypt():

  openssl('encrypt')

def _cmd_decrypt():

  openssl('decrypt')

def openssl(mode):

  if mode not in ('encrypt', 'decrypt'):
    raise ValueError

  opts = {
    'encrypt': {
      'run': [PLAIN_FILE],
      'open': [ENC_FILE, 'wb'],
      'write': lambda s:s,
    },
    'decrypt': {
      'run': [ENC_FILE, '-d'],
      'open': [PLAIN_FILE, 'w'],
      'write': lambda s:s.decode('utf8'),
    },
  }[mode]

  cmd = ['openssl', 'enc', '-in']
  cmd.extend(opts['run'])
  cmd.extend(['-aes-256-cbc', '-pass', 'stdin'])

  p = run(cmd, capture_output=True, input=get_pass())

  if p.returncode != 0:
    print('===== ERROR =====')
    print(p.stderr)
    return

  with open(*opts['open']) as f:
    f.write(opts['write'](p.stdout))

def get_pass():

  if os.path.isfile(PASS_FILE):
    with open(PASS_FILE, 'r') as f:
      return f.read().strip().encode('utf8')

  pword = getpass('Password: ')
  with open(PASS_FILE, 'w') as f:
    f.write(pword + '\n')
  return pword.encode('utf8')

if __name__ == '__main__':
  main(*sys.argv[1:])
