from src.fastq_reader import read_fastq
from src.utils.track_process import track
from src.fastq_obj import FastqObj


class FastqStats():

    num_seq = 0
    num_bases = 0
    num_quality_values = 0

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
    def get_fastq_stats(cls, filepath: str):
        """
        Generate fastq stats
        """
        sequences = read_fastq(filepath)
        for sequence in sequences:
            cls.get_num_seq(sequence)
            cls.get_num_bases(sequence)
            cls.get_num_quality_values(sequence)

        print("Total Number of Sequences: ", cls.num_seq)
        print("Total Number of bases: ", cls.num_bases)
        print("Total Number of Quality Values", cls.num_quality_values)

        return cls.get_num_seq, cls.num_bases, cls.num_quality_values
