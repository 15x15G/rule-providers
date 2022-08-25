import glob
import yaml
import os
from yaml import load, dump
try:
    from yaml import Cloader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

cdir = os.path.dirname(__file__)
files = set(glob.glob(os.path.join(cdir, '*.txt'))) - set(glob.glob(os.path.join(cdir,
                                                                                 '*-txt.txt')))
for file in files:
    print(file)
    basename = os.path.basename(file)
    filename = os.path.splitext(basename)[0]
    with open(file) as f:
        obj = yaml.load(f, Loader)
        with open(os.path.join(cdir, filename + '-text.txt'), "w") as txt_file:
            for line in obj['payload']:
                txt_file.write("".join(line) + "\n")
exit()
