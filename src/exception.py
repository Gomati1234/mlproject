#The sys module in Python helps you interact with the system and Python itself. Here's what it does in simple terms:
import sys
from src.logger import logging

# sys.exc_info() returns a tuple (type, value, traceback):
# type: The class/type of the exception (e.g., ZeroDivisionError).
# value: The actual exception object (used for str(error)).
# traceback: A traceback object containing information about where the error occurred.


def error_message_detail(error,error_details:sys):
      _,_,exc_tb=error_details.exc_info()
      file_name=exc_tb.tb_frame.f_code.co_filename
      error_message= "Error occured in script no. [{0}], line number [{1}] ,with error meassage [{2}]]".format(
      file_name, exc_tb.tb_lineno, str(error)
      )
      return error_message

class CustomException(Exception):
      def __init__(self,error_message,error_detail:sys):
            super().__init__(error_message)
            self.error_message=error_message_detail(error_message,error_detail)
      def __str__ (self):
            return self.error_message

if __name__=="__main__":
     try:
           a=10/0
     except Exception as e:
           logging.info(e)
           raise CustomException(e,sys)

    