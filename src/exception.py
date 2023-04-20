import sys   #contrlling all then errors and having info init
import logging


def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name[{0}] line number [{1} error message]".formate()
    file_name,exc_tb.tb_lineno,str(error)


class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message 




'''
#"to test the file run the below code"


if __name__ == '__main__':

    try:
        a=1/10
    except Exception as e:
        logging.info("Divide by zero")
        raise CustomException(e, sys)

'''