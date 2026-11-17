from models.test_steps import TestSteps
from models.actual_result import ActualResult

import re

class TestCase:
    def __init__(self, id: str, 
        title: str, 
        data: str, 
        steps: list["TestSteps"], 
        actual_result: "ActualResult" = None
        ):

        if not re.match(r"^TC-\d+$", id):
            raise ValueError("ID måste skrivas i formatet 'TC- följt av siffror(t.ex. TC-01)")

        self.id: str = id
        self.title: str = title
        self.data: str = data
        self.steps: list[TestSteps] = steps
        self.actual_result = actual_result
 