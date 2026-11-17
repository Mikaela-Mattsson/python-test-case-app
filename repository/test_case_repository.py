from models.test_case import TestCase

class TestCaseRepository:
    def __init__(self):
        self.test_cases = []

    def try_add(self, test_case: TestCase) -> None:
        self.test_cases.append(test_case)

    def get_all(self) -> list[TestCase]:
        return self.test_cases

    def delete(self, test_case_id: str) -> None:
        for tc in self.test_cases:
            if tc.id == test_case_id:
                self.test_cases.remove(tc)
                break
        
    def update(self, test_case_id: str, update_test_case: TestCase) -> None:
        for i, tc in enumerate(self.test_cases):
            if tc.id == test_case_id:
                self.test_cases[i] = update_test_case
                break