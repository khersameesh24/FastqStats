'''
@SEQ_ID                                                      -> (sequence_identifier)
GATTTGGGGTTCAAAGCAGTATCGATCAAATAGTAAATCCATTTGTTCAACTCACAGTTT -> (raw_sequence)
+                                                            -> (description)
!''*((((***+))%%%++)(%%%%).1***-+*''))**55CCF>>>>>>CCCCCCC65 -> (quality_values)
'''


class FastqObj():
    """
    Represent a fastq sequence as an object
    Attr:
    sequence_identifier - sequence id
    raw_sequence - nucleotide sequence
    description - info about the sequence
    quality_values - phred scores for each base in the raw sequence
    """

    def __init__(
        self,
        sequence_identifier: str,
        raw_sequence: str,
        description: str,
        quality_values: str
    ):
        self.sequence_identifier: str = sequence_identifier
        self.raw_sequence: str = raw_sequence
        self.description: str = description
        self.quality_values: str = quality_values

        self.fastq_obj: dict[str:str] = {
            "sequence_identifier": self.sequence_identifier,
            "raw_sequence": self.raw_sequence,
            "description": self.description,
            "quality_values": self.quality_values
        }

    def get_fastq_obj(self):
        """
        Get a fastq object
        A combination of identifier,
        raw sequence, description &
        quality_scores for a single 
        sequence in the fastq file
        """
        return self.fastq_obj

    def __dict__(self):
        return self.fastq_obj

    def __len__(self):
        return len(self.fastq_obj["raw_sequence"])

    def __str__(self):
        return str(self.fastq_obj)

    def __repr__(self):
        return f"FastqObj({self.sequence_identifier} {self.raw_sequence} {self.description} {self.quality_values})"
