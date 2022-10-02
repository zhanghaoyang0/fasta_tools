import os
import sys
import gzip
import time
import argparse

start = time.time()

def openfile(filename):
    if filename.endswith('.gz'): return gzip.open(filename) 
    else: return open(filename)

### flags parser
parser = argparse.ArgumentParser(description='split fasta')
parser.add_argument('--file_in', type=str, default='./example/test.fa')
parser.add_argument('--path_out', type=str, default='./example/test_splited')
args = parser.parse_args()

file_in = args.file_in
path_out = args.path_out

# default setting
file_in = './example/test.fa.gz'
path_out = './example/test_splited/'

print('setting:')
print('file_in: '+ file_in)
print('path_out: '+ path_out)

# path_out
try:
    os.mkdir(path_out)
except FileExistsError:
    pass

print('splitting ...')
# split
if file_in.endswith('.gz'): 
    f = gzip.open(file_in, 'rb')
    data = f.read().decode().split('>')
else: 
    f = open(file_in, 'r')
    data = f.read().split('>')

f.close()

# write output
for i in data[1:]:
    items = i.split('\n')
    seq_name = items[0]
    seq = '\n'.join(items[1:])
    with open(path_out+'/'+seq_name, 'w') as f:
        _ = f.write(seq) # use a var to aviod printing


# print log
print(f'{len(data[1:])} seqs are splited successfully')
print(f'done!')
end = time.time()
print (f'spend {round(end-start, 2)} sec')