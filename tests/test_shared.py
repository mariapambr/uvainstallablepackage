import pytest
import sys
sys.path.append("sys.path.append("/uvainstallablepackage/shared")
                
import shared as sh
sh.afunction()                

def space_compress(input_string):
    if not isinstance(input_string, str):
        return "Expected string but got {}".format(type(input_string))
    
    compressed_string = " ".join(input_string.split())
    return compressed_string.replace("\n", " ")
                
def test_clean_string():
    test_str = " This! is      a ,test string  "

    assert "This is a test string" == sh.clean_string(test_str), "String <{}> not cleaned as expected".format(test_str)
