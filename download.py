import multiprocessing as mp
import subprocess
import glob
import os

with open('ZINC22-downloader-2D-smi.gz.wget', 'r') as f:
    commands = f.readlines()

import multiprocessing as mp
import subprocess

def download_file(command):
    subprocess.run(command, shell=True)
with mp.Pool(mp.cpu_count()-4) as p:
    p.map(download_file, commands)
    