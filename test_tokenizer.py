from tokenizer import Tokenizer

def test_split_empty_string_result_empty_array():

    stringToSplit = ""
    expResult = []
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult

def test_split_comma_empty_string_result_empty_array():
    stringToSplit = ","

    expResult = []
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult

def test_split_one_string_result_array_of_one():
    stringToSplit = "java"

    expResult = ["java"]
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult    

def test_split_two_string_result_array_of_two():
    stringToSplit = "java, python"

    expResult = ["java", "python"]
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult       

def test_split_comma_string_result_array_of_one():
    stringToSplit = ",java"

    expResult = ["java"]
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult       

def test_split_space_string_result_array_of_one():
    stringToSplit = " java"

    expResult = ["java"]
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult        

def test_split_end_comma_string_result_array_of_one():
    stringToSplit = "java,"

    expResult = ["java"]
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult         

def test_split_end_space_string_result_array_of_one():
    stringToSplit = "java "

    expResult = ["java"]
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult      

def test_split_complicated_string_result_array_of_multiple():
    stringToSplit = "java byte code, python"

    expResult = ["java byte code", "python"]
    result = None
    cut = Tokenizer()

    result = cut.parse_string(stringToSplit)

    assert result == expResult     