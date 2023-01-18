# write tests for transcribes

from seqparser import (
        transcribe,
        reverse_transcribe)

import pytest


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the
    transcribe function here.
    """
    fasta_file = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    parser_obj = transcribe(fasta_file)
    parser_line = [record for record in parser_obj]

    assert parser_line[0:10] == ['C', 'U', 'C', 'A', 'G', 'C', 'G', 'U', 'C', 'A']
    assert parser_line[0:10] == ['A', 'C', 'A', 'C', 'C', 'A', 'G', 'C', 'A', 'U'], "Error: there's something in transcribe"



def test_reverse_transcribe():
    """
    Write your unit test for the
    reverse transcribe function here.
    """
    fasta_file = 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG'
    parser_obj = reverse_transcribe(fasta_file)
    parser_line = [record for record in parser_obj] 

    parser_line[0:10] == ['C', 'U', 'C', 'A', 'G', 'C', 'G', 'U', 'C', 'A']
    parser_line[0:10] == ['C', 'U', 'C', 'A', 'G', 'C', 'G', 'U', 'C', 'A'], "Error: there's something in reverse_transcribe"

