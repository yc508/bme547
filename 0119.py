print("this is the database module and python calls it {}".format(__name__))#__name__contains the name of the module
#import blood_calculator import how file

#import blood_calculator
from blood_calculator import check_HDL#import function only
#from blood_calculator import * import all function within blood_calculator


HDL_value=55

#classification = blood_calculator.check_HDL(HDL_value)
classification = check_HDL(HDL_value)

print("55 is {}".format (classification))
x=check_HDL(200)

import numpy as np

