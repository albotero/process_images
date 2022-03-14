#!/usr/bin/env python3

'''
Usage example:
    ls images | ./process_images.py images tmp
'''

from PIL import Image
import os
import sys

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

# If 1 argument it is destination folder
# If 2 arguments they are source and destination folder
src_img_dir = os.getcwd()
dest_img_dir = ''
if len(sys.argv) == 2:
    dest_img_dir = sys.argv[1]
elif len(sys.argv) == 3:
    src_img_dir = sys.argv[1]
    dest_img_dir = sys.argv[2]
else:
    print(color.BOLD + color.RED + 'ERROR:' + color.END + ' Invalid arguments')
    sys.exit(1)

# Create destination dir
os.makedirs(dest_img_dir, exist_ok = True)

# Pass src images as stdin from ls
for src_file in sys.stdin:
    src_file = src_file.strip()
    img = Image.open(os.path.join(src_img_dir, src_file)).resize((128,128)).rotate(90).convert('RGB')
    img.save(os.path.join(dest_img_dir, src_file), format='JPEG')

print(color.BOLD + color.GREEN + 'OK:' + color.END + ' Files converted in ' + dest_img_dir)
