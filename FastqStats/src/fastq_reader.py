'''
Class to read the fastq file and return a generator obj
Handles different file formats - *.fastq & *.fastq.gz
'''


import os
import sys
import gzip
from FastqStats.src.fastq_obj import FastqObj
from typing import Iterator


def read_fastq(file_path) -> Iterator[str]:
    """
    Read input fastq file path and return a generator
    of FastqObj
    Args: filepath - path to the fastq file
    """

    print("Input Fastq File :", os.path.basename(file_path))
    try:
        file_ext = os.path.splitext(file_path)[1]

        if file_ext == ".gz":
            f = gzip.open(file_path, 'rt')
        elif file_ext == ".fastq" or file_ext == ".fq":
            f = open(file_path, 'rt')
        else:
            print("Check if the correct file was passed. Supported formats `.fastq` & `.fastq.gz`")

        while True:
            # Read one sequence at a time - 4 lines
            fastq_seq = [f.readline().strip() for i in range(4)]

            if not fastq_seq[0]:
                break

            # yield a FastqObj
            yield FastqObj(
                sequence_identifier=fastq_seq[0],
                raw_sequence=fastq_seq[1],
                description=fastq_seq[2],
                quality_values=fastq_seq[3]
            ).get_fastq_obj()

        f.close()

    except FileNotFoundError as err:
        print("Check if the file exists.")
        sys.exit()
