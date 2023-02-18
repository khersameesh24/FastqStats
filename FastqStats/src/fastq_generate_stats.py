from FastqStats.src.fastq_reader import read_fastq
from FastqStats.src.utils.track_process import track
from typing import Iterator


class FastqGenerateStats():

    num_seq = 0
    num_bases = 0

    @classmethod
    def display_stats(cls, seq_counts: bool = True, nuc_counts: bool = True) -> None:
        """
        Display requested stats on the console
        """
        if seq_counts:
            print("Total Number of Sequences: ", cls.num_seq)
        
        if nuc_counts:
            print("Total Number of bases: ", cls.num_bases)

    @classmethod
    def get_num_seq(cls) -> int:
        """
        Get the total number of sequences
        in the fastq file
        Args: fastq sequence object (FastqObj)
        """
        return cls.num_seq

    @classmethod
    def get_num_bases(cls) -> int:
        """
        Get the total number of bases
        in the fastq file
        Args: fastq sequence object (FastqObj)
        """
        return cls.num_bases

    # @track
    @classmethod
    def get_fastq_stats(cls, filepath: str, seq_counts = True, nuc_counts = True):
        """
        Generate fastq stats
        """
        sequences: Iterator[str] = read_fastq(filepath)
        if seq_counts and nuc_counts:
            for sequence in sequences:
                cls.num_seq += 1
                cls.num_bases += len(sequence['raw_sequence'])

        elif seq_counts:
            for sequence in sequences:
                cls.num_seq += 1

        elif nuc_counts:
            for sequence in sequences:
                cls.num_bases += len(sequence['raw_sequence'])

        cls.display_stats(seq_counts, nuc_counts)
