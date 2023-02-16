from fastq_reader import read_fastq
from utils.track_process import track
from fastq_obj import FastqObj


class FastqStats():

    num_seq = 0
    num_bases = 0
    num_quality_values = 0

    @classmethod
    def display_stats(cls, seq_counts = True, nuc_counts = True):
        if seq_counts:
            print("Total Number of Sequences: ", cls.num_seq)
        
        if nuc_counts:
            print("Total Number of bases: ", cls.num_bases)



    @classmethod
    def get_num_seq(cls, sequence: FastqObj):
        """
        Get the total number of sequences
        in the fastq file
        Args: fastq sequence object (FastqObj)
        """
        if sequence["raw_sequence"]:
            cls.num_seq += 1

    @classmethod
    def get_num_bases(cls, sequence: FastqObj):
        """
        Get the total number of bases
        in the fastq file
        Args: fastq sequence object (FastqObj)
        """
        if sequence["raw_sequence"]:
            cls.num_bases += len(sequence["raw_sequence"])

    @classmethod
    def get_num_quality_values(cls, sequence: FastqObj):
        """
        Get quality values (phred scores)
        from the fastq file
        Args: fastq sequence object (FastqObj)
        """
        if sequence["quality_values"]:
            cls.num_quality_values += len(sequence["quality_values"])

    @classmethod
    @track
    def get_fastq_stats(cls, filepath: str, seq_counts = True, nuc_counts = True):
        """
        Generate fastq stats
        """
        sequences = read_fastq(filepath)
        for sequence in sequences:
            if seq_counts:
                cls.get_num_seq(sequence)
            if nuc_counts:
                cls.get_num_bases(sequence)

        cls.display_stats(seq_counts, nuc_counts)
