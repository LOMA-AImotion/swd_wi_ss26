import random
from thi_quiz_interfaces import AbstractSequenceGenerator


class Answer:
    def __init__(self, text, correct):
        """
        Object representing an answer to a Quiz question.

        :param text: Answer text as string
        :parma correct: Boolean flag if answer is true or not
        """
        self.text = text
        self.correct = correct


class Question:
    def __init__(self, question, answers: list):
        """
        Question for the quiz
        
        :param question: question text as string
        :param answers: list of Answer objects
        """
        self.question = question
        self.answers = answers


class QuestionSequenceGenerator(AbstractSequenceGenerator):
    def __init__(self, all_questions: list):
        """
        Generates a random sequence of a list of questions
        Args:
            all_questions: list of Question objects 
        """
        # Calling init of the base class -> inheritance!
        super().__init__()

        self.sequence = random.sample(all_questions, len(all_questions)) # permuting the list 

    def get_next_question(self):
        """
        Returns the next question in the sequence or None if no question is left.
        """
        if self.sequence:
            return self.sequence.pop() # list.pop() returns the last element in the list and removes it from the list 
        else:
            return None

    def new_questions(self, all_questions):
        self.__init__(all_questions)



def load_questions_from_file(path_to_file):
    """
    Loads a txt file that contains questions in the format from the lecture.

    Args:
        path to file: String that contains the path to the txt file

    Returns:
        A list that contains all questions from the txt file in the following format:
        [Question_1, ..., Question_n]
    """   
       
   
    file = open(path_to_file, 'r', encoding='utf-8-sig') # specifying the encoding may be necessary on some operating systems.
    lines = file.readlines()
    file.close()

    # Number of questions is defined in the first line.
    num_overall_questions = int(lines[0])

    all_questions = list()
    
    
    # each question consists of 5 lines 
    for i in range(1, (num_overall_questions)*5, 5):
        all_answers = list()
        question_text = lines[i]
        tmp_answers = [lines[i+j] for j in range(1, 5)]
        
        
        # search answers for CORRECT: tag and extract the question
        for  text in tmp_answers:
            if text.startswith("CORRECT:"): # this must be a correct answer --> We can have multiple true answers now!
                text = text.replace("CORRECT:", "")    
                answer = Answer(text=text, correct=True)
            else:
                answer = Answer(text=text, correct=False)

            all_answers.append(answer)
                
        
        question = Question(question=question_text, answers=all_answers)
        all_questions.append(question)

    return all_questions
