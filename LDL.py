from ast import Return
from ctypes.wintypes import INT


LDL_value = input("Enter your LDL value: ")

LDL = int(LDL_value)

if LDL < 130:
    print("Your LDL value is normal.")
elif 130 <= LDL <= 159:
    print("Your LDL value is borderline high.")
elif 160 <= LDL <= 189:
    print("Your LDL value is high.")
else:
    print("Your LDL value is very high.")
#return
#SyntaxError: 'return' outside function



