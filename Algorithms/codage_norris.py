import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def make_bitseq(s: str) -> str:
    if not s.isascii():
        raise ValueError("ASCII only allowed")
    aux = " ".join(f"{ord(i):07b}" for i in s)
    return  aux.replace(" ","")



message = input()
result =  []
bin_msg = make_bitseq(message)
for element in bin_msg :

    if result == []:
        result.append((element,1))
    elif element == result[-1][0]:
        result[-1] = (result[-1][0],result[-1][1] + 1)
    elif element != result[-1][0]:
        result.append((element,1))
        
        
str_res = ""
for element in result:
    if element[0] == "1" :
        str_res = str_res + "0 "
    elif element[0] == "0" :
        str_res = str_res + "00 " 
    seq_res = ""
    for _ in range (element[1]):
        seq_res = seq_res + "0"
        
    str_res = str_res + seq_res  + " " 
        
        
    


print(str_res[:-1])
