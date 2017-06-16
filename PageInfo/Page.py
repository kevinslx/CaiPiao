import os
import sys

print(sys.argv, len(sys.argv))
os.system(sys.argv[1])
print('using Git')

