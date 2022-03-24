from abc import abstractmethod


class BaseCase:
    @abstractmethod
    def get_test_case(self, *args, **kwargs):
        pass
