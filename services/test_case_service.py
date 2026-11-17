from models.test_case import TestCase
from models.test_steps import TestSteps
from models.actual_result import ActualResult
from repository.test_case_repository import TestCaseRepository

class TestCaseService:
    def __init__(self, test_case_repository: TestCaseRepository):
        self._repository: TestCaseRepository = test_case_repository

    def try_add_test_case(self, test_case: TestCase) -> None:
        self._repository.try_add(test_case)

    def get_by_id(self, test_case_id: str) -> TestCase | None:
        all_cases = self._repository.get_all()
        for tc in all_cases:
            if tc.id == test_case_id:
                return tc
        return None

    def delete_test_case(self, test_case_id: str) -> None:
        self._repository.delete(test_case_id)
    
    def update_test_case(self, test_case_id: str, updated_test_case: TestCase) -> None:
        self._repository.update(test_case_id, updated_test_case)
    
    def get_all_test_cases(self) -> list[TestCase]:
        return self._repository.get_all()