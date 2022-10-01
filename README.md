
# About fasta_tools
Some tools to process fasta

# Requirements 
- `Linux` 
- `LiftOver`
- `Python3` (3.9.6) with `pandas` (1.4.3), `argparse`, `os`, `sys`, `time`

# Getting Started
Clone this repository via the commands:
```  
git clone https://github.com/zhanghaoyang0/fasta_tool.git
cd fasta_tool
```

# Some tools
Now I only make one tool, but I may do more.   

`split_fa`
I make minor efforts to `[split-fasta](https://github.com/uditvashisht/split-fasta)` to make it accept gz input and name the output files with seq names.
Examples (hg38tohg19):

```
python ./code/split_fa.py\
--file_in ./example/test.fa \
--path_out ./example/test_splited
```
gzip (file_in end with '.gz') input can be recongized: 
```
python ./code/split_fa.py\
--file_in ./example/test.fa.gz \
--path_out ./example/test_splited
```
The input file is like:
```
>chr1
ACCCTTTTNNNN
>chr11
TCGAAATTTCCGGGGGGAAAA
>chr2
```
The output file (e.g., chr1) is like:
```
ACCCTTTTNNNN
```

# Feedback and comments
Add an issue or send email to zhanghaoyang0@hotmail.com