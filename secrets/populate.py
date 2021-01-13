#!/usr/bin/env python3

import json
import os
import sys

from config import *

def main():

  os.chdir(os.path.dirname(os.path.realpath(__file__)))

  with open(PLAIN_FILE) as f:
    values = json.load(f)

  with open(MAP_FILE) as f:
    keys = json.load(f)

  os.chdir(os.path.join(os.path.pardir, CONF_DIR))
  populate(keys, values)

def populate(keys, values):

  for (name, info) in keys.items():
    globals()['_' + info['type']](info['path'], values[name])

def get_dict(d, keys):

  d = d[keys[0]]
  for k in keys[1:-1]:
    d = d[k]

  return d

def _json(path, values):

  with open(os.path.extsep.join([path, TEMPLATE_EXT])) as f:
    template = json.load(f)

  error = False
  for (key, value) in values:
    last = key[-1]
    try:
      new = get_dict(template, key)
    except KeyError:
      print('Missing key {} in template file'.format(key))
      error = True
    new[last] = value

  if error:
    raise RuntimeError

  with open(path, 'w') as f:
    json.dump(template, f, sort_keys=True, indent=4)

if __name__ == '__main__':
  main(*sys.argv[1:])
