'''
Class to read the fastq file and return a generator obj
Handles different file formats - *.fastq & *.fastq.gz
'''


import os
import sys
import gzip
from FastqStats.src.fastq_obj import FastqObj
from FastqStats.src.utils.track_process import track
from typing import Iterator


# @track
def read_fastq(file_path: str) -> Iterator[str]:
    """
    Read input fastq file path and return a generator
    of FastqObj
    Args: filepath - path to the fastq file
    """
    try:
        file_ext = os.path.splitext(file_path)[1]

        if file_ext == ".gz":
            filehandle = gzip.open(file_path, 'r')
        
        elif file_ext == ".fastq" or file_ext == ".fq":
            filehandle = open(file_path, 'rt')
        else:
            print(
                "Check if the correct file was passed. Supported formats `.fastq`, `.fq` & `.fastq.gz`")
            sys.exit(1)

        print(f"Input Fastq File : {os.path.basename(file_path)}")
        print(f"Fastq File Size  : {os.path.getsize(file_path)/(1024*1024*1024):.2f}G")

        for seq_iden, raw_seq, desc, qual_val in zip(*[filehandle] * 4):

            # yield a FastqObj
            yield FastqObj(
                sequence_identifier = seq_iden,
                raw_sequence = raw_seq,
                description = desc,
                quality_values = qual_val
            ).get_fastq_obj()

        filehandle.close()

    except FileNotFoundError as err:
        print("Check if the file exists.")
        sys.exit()
