from abc import abstractmethod

null = None


class BaseCase:
    @abstractmethod
    def get_test_case(self, *args, **kwargs):
        pass
