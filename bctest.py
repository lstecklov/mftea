#!/bin/env python3

import sys
import bcrypt
import pprint

print(bcrypt.hashpw('password'.encode('utf-8'), bcrypt.gensalt()))


pp = pprint.PrettyPrinter(indent=4)
pp.pprint(sys.modules)
