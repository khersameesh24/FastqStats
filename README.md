# FastqStats

## Introduction
---
FastqStats is a command line utility to generate various stats from a fastq file.
Currently the tool supports counting the number of sequences and the total nucleotide bases present in a fastq file. The current implementation supports both `.fastq` (uncompressed) and `.fastq.gz` (compressed) file formats.

Upcoming versions would support more functionalities and file formats to work with.

## Installation
---
To install the tool as a command line utility download/clone the repository.
1. Clone this repository
    ```
    $ git clone https://github.com/khersameesh24/FastqStats.git
    ```
2. Install pip if not already installed.
    ```
    $ sudo apt install python3-pip
    ```
3. Install the package as command line tool
    ```
    $ cd FastqStats/ && pip install .
    ```

## Usage
---
```
$ fastqstats -h

usage: fastqstats [-h] -i FASTQ_FILE [-n] [-b]

Generate Stats from a fastq file.

optional arguments:
  -h, --help            show this help message and exit

Required arguments:
  -i FASTQ_FILE, --input FASTQ_FILE
                        Input fastq file path

Optional arguments:
  -n, --seq-count       Get the the total number of sequences in
                        the fastq file
  -b, --nuc-count       Get the total number of bases in the
                        fastq file

```
### Example usage
```
$ fastqstats -i tests/example_files/fastq/test_file_1.fastq -n -b
```
**Outputs**
```
Input Fastq File : test_file_1.fastq
Total Number of Sequences:  118571
Total Number of bases:  11857100
```
