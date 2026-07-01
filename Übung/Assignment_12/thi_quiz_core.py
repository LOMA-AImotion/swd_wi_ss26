from thi_quiz_interfaces import AbstractQuizCore, AbstractSequenceGenerator

class QuizCore(AbstractQuizCore):
    def __init__(self, sequence_generator: AbstractSequenceGenerator, name='SWD QUIZ'):
        """
        Args: 
            sequence_generator: AbstractSequenceGenerator, must provide get_next_question
            name: name of the quiz
        """
        # Calling init of the base class -> inheritance!
        super().__init__()

        # This is a type hint, it tells you which datatype this obejct should have
        self.sequence_generator: AbstractSequenceGenerator = sequence_generator
        self.name = name

        self.active_question = None

    def get_next_question(self):
        """
        Returns the next question as Question object
        """
        next_question = self.sequence_generator.get_next_question()
        self.active_question = next_question
        return next_question

    def reset(self):
        """
        Resets the internal state
        """
        self.active_question = None

    def check_answer(self, index):
        """
        Checks if the given index corresponds to a true answer or not. 
        """
        answer = self.active_question.answers[index]
        if answer.correct:
            return True
        else:
            return False
