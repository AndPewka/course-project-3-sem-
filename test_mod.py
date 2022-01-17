import pytest
from functions import *
from base import *



def test_correctNumber():
    assert checkNumber("89831982874") == True
    assert checkNumber("+79134426504") == True
    assert checkNumber("+234231") == False
    assert checkNumber("89831982873") == True
    assert checkNumber("123") == False

def test_addVacancies():
    vac = Vacancies
    assert vac.add_vacancie("test","test","test","test","test","test") == True


def test_delVacancies():
    vac = Vacancies
    assert vac.del_vac("test") == True
    assert vac.del_vac("test2") == False


def test_addSummaries():
    summ = Summaries
    assert summ.add_summary("test","test","test","test","test","test","test","test") == True

def test_delSummaries():
    summ = Summaries
    assert summ.del_summ("test") == True
    assert summ.del_summ("test2") == False



def test_addUser():
    user = Users
    assert user.add_profile("89831982872","8","8","8","8") == True
    assert user.add_profile("89831982872","7","7","7","7") == False


def test_delUser():
    user = Users
    assert user.del_profile("89831982872") == True
    assert user.del_profile("88888888888") == False




if __name__ == "__main__":
    pytest.main()