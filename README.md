
# About fasta_tools
Some tools to process fasta.  
Now I only make one tool, but I may do more.   

# Requirements 
- `Linux` 
- `Python3` (3.9.6) with `argparse`, `os`, `sys`, `time`

# Getting Started
Clone this repository via the commands:
```  
git clone https://github.com/zhanghaoyang0/fasta_tool.git
cd fasta_tool
```

# split_fa
a script to split fasta.  
I make some improvements for [split-fasta](https://github.com/uditvashisht/split-fasta) (make it accept `.gz` input and name the output files with seq names).

Examples:
```
python ./code/split_fa.py \
--file_in ./example/test.fa \
--path_out ./example/test_splited
```
gzip (file_in end with '.gz') input can be recongized: 
```
python ./code/split_fa.py \
--file_in ./example/test.fa.gz \
--path_out ./example/test_splited
```
The input file (e.g., test.fa) is like:
```
>fas1
taaccctaaccctaaccctaaccctaaccctaaccctaaccctaacccta
accctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaac
cctaacccaaccctaaccctaaccctaaccctaaccctaaccctaacccc
>fas2
taaccctaaccctaaccctaaccctaacctaaccctaaccctaaccctaa
ccctaaccctaaccctaaccctaaccctaacccctaaccctaaccctaaa
ccctaaaccctaaccctaaccctaaccctaaccctaaccccaaccccaac
>fas3
cccaaccccaaccccaaccccaaccctaacccctaaccctaaccctaacc
ctaccctaaccctaaccctaaccctaaccctaaccctaacccctaacccc
taaccctaaccctaaccctaaccctaaccctaaccctaacccctaaccct
```
The output file (e.g., fas1) is like:
```
taaccctaaccctaaccctaaccctaaccctaaccctaaccctaacccta
accctaaccctaaccctaaccctaaccctaaccctaaccctaaccctaac
cctaacccaaccctaaccctaaccctaaccctaaccctaaccctaacccc
```

# Feedback and comments
Add an issue, or email to zhanghaoyang0@hotmail.com