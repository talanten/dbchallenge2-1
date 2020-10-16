from age import Age 

def test_age_inferior_to_02 ():

    current_age = "01"

    expResult = "Error"
    result = None
    cut = Age()

    result = cut.next_age(current_age)

    assert result == expResult

