import multiprocessing as mp
import subprocess
import glob
import pandas as pd
from rdkit import Chem
import os
    
def canonicalize(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        return Chem.MolToSmiles(mol, isomericSmiles=True)
    else:
        return None
    
# dirs = glob.glob('/data1/ZINC22/H*')
# paths = []
# for directory in dirs:
#     paths += glob.glob(directory+'/*.smi')
    
# # def ZINC_clean(path):
# #     df = pd.read_csv(path, sep='\t', names=['SMILES', 'name'])['SMILES']
# #     df.to_csv(path.replace('.smi', '.csv'), index=False)
# #     command = f'rm {path}'
# #     subprocess.run(command, shell=True)
# def ZINC_clean(path):
#     df = pd.read_csv(path, sep='\t', names=['SMILES', 'name'])[['SMILES']]
#     df.to_parquet(path.replace('.smi', '.parquet'), index=False)
#     command = f'rm {path}'
#     subprocess.run(command, shell=True)

# with mp.Pool(1) as p:
#     p.map(ZINC_clean, paths)





# dirs = glob.glob('/data1/ZINC22/H*')
# # paths = []
# # for directory in dirs:
# #     paths += glob.glob(directory+'/*.parquet')

# # paths_with_sizes = [(f, os.path.getsize(f)) for f in paths]
# # # Sort the list by filesize
# # paths_with_sizes.sort(key=lambda x: x[1])
# def canonicalize_func(row):
#     smiles = row['SMILES']
#     row['SMILES'] = canonicalize(smiles)
#     return row
# # def ZINC_clean(path):
# #     df = pd.read_parquet(path[0])
# #     df = df.apply(canonicalize_func, axis=1)
# #     df.to_parquet(path, index=False)
# # # print(paths)
# # for path in paths_with_sizes:
# #     ZINC_clean(path)
    
# paths = []
# for directory in dirs:
#     paths += glob.glob(directory+'/*.csv')
# paths_with_sizes = [(f, os.path.getsize(f)) for f in paths]
# # Sort the list by filesize
# paths_with_sizes.sort(key=lambda x: x[1])
# def ZINC_clean(path):
#     path = path[0]
#     df = pd.read_csv(path)
#     df = df.apply(canonicalize_func, axis=1)
#     df.to_parquet(path.replace('.csv', '.parquet'), index=False)
#     command = f'rm {path}'
#     subprocess.run(command, shell=True)
# with mp.Pool(4) as p:
#     p.map(ZINC_clean, paths_with_sizes)




dirs = glob.glob('/data1/ZINC22/H*')
paths = []
for directory in dirs:
    paths += glob.glob(directory+'/*.smi')
paths_with_sizes = [(f, os.path.getsize(f)) for f in paths]
# Sort the list by filesize
paths_with_sizes.sort(key=lambda x: x[1])
def ZINC_clean(path):
    path = path[0]
    df = pd.read_csv(path, sep='\t', names=['SMILES', 'name'])[['SMILES']]
    df.to_parquet(path.replace('.smi', '.parquet'), index=False)
    command = f'rm {path}'
    subprocess.run(command, shell=True)

# with mp.Pool(3) as p:
#     p.map(ZINC_clean, paths_with_sizes)
for path in paths_with_sizes:
    ZINC_clean(path)