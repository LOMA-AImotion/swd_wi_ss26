# These interfaces serve as base classes to inherit from. 
# They are used by higher level modules to define how they interact with lower level modules
# Interfaces define which function a class must provide AT LEAST
# By throwing a NotImplementedError in the functions, we enforce that the actual implementation takes place in the subclasses

from abc import ABC, abstractmethod

class AbstractQuizCore(ABC):

    @abstractmethod
    def get_next_question(self):
        """
        Returns a Question object
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Resets the internal state
        """
        pass

    @abstractmethod
    def check_answer(self, index):
        """
        Takes an integer index and checks if it corresponds to a true answer or not. 

        Returns a Boolean value
        """
        pass

class AbstractSequenceGenerator(ABC):

    @abstractmethod
    def get_next_question(self):
        """
        Returns a Question object
        """
        pass

