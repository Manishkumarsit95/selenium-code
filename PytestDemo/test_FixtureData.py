import pytest

from PytestDemo.BasicClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self,dataLoad):
       log = self.getlogger()
       log.info(dataLoad)
       log.info(dataLoad[0])
       log.info(dataLoad[2])
       #print(dataLoad)


