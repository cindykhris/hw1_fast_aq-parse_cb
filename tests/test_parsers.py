# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser
    class here. You should generate an instance of
    your FastaParser class and assert that it properly
    reads in the example Fasta File.
    """
    fasta_file = "/Users/cindybarrios/Desktop/BMI_203/hw1_fast_aq-parse_cb/data/test.fa"
    parser_obj = FastaParser(fasta_file)
    parser_line = [record for record in parser_obj]

    assert parser_line[0][0] == "seq0"
    assert parser_line[0][0] == "seq1", "Error: there's something wrong with the FastaParser"


def test_FastqParser():
    """
    Write your unit test for your FastqParser
    class here. You should generate an instance of
    your FastqParser class and assert that it properly
    reads in the example Fastq File.
    """
    
    fasta_file = "/Users/cindybarrios/Desktop/BMI_203/hw1_fast_aq-parse_cb/data/test.fq"
    parser_obj = FastqParser(fasta_file)
    parser_line = [record for record in parser_obj]

    assert parser_line[0][0] == "seq0"
    assert parser_line[0][0] == "seq1", "Error: there's something wrong with the FastqParser"
