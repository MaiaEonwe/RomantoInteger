import re
from unittest.util import _count_diff_all_purpose
class Solution(object):
    def romanToInt(self, s):
        last_form=[]
        index_number=0
        index_number1=0
        calcution=0
        countI =0
        countV =0
        countX =0
        countL =0
        countC =0
        countD =0
        countM =0
        
        self.s=s
        """
        :type s: str
        :rtype: int
        """
        detailed_find=re.findall("IV|IX|XL|XC|CD|CM",self.s)
        general_find=re.findall("I|V|X|L|C|D|M",self.s)
        last_form.extend(detailed_find)
        for i in general_find:
            if i =="I":
                countI+=1
            elif i =="X":
                countX+=1
            elif i =="L":
                countL+=1
            elif i =="C":
                countC+=1
            elif i =="D":
                countD+=1
            elif i =="M":
                countM+=1
        for a in detailed_find:
            if a =="IV":
                countI-=1
                countV-=1
            elif a =="IX":
                countI-=1
                countX-=1
            elif a =="XL":
                countX-=1
                countL-=1
            elif a =="XC":
                countX-=1
                countC-=1
            elif a =="CD":
                countC-=1
                countD-=1
            elif a =="CM":
                countC-=1
                countM-=1
        for i in general_find:
            if i =="I" and countI > 0:
                last_form.append(i)
            elif i =="v" and countV > 0:
                last_form.append(i)
            elif i =="L" and countL > 0:
                last_form.append(i)
            elif i =="C" and countC > 0:
                last_form.append(i)
            elif i =="D" and countD > 0:
                last_form.append(i)
            if i =="M" and countM > 0:
                last_form.append(i)
        for calculator in last_form:
            if calculator=="I":
                calcution+=1
            elif calculator=="V":
                calcution+=5
            elif calculator=="C":
                calcution+=100
            elif calculator=="D":
                calcution+=500
            elif calculator=="L":
                calcution+=50
            elif calculator=="M":
                calcution+=1000
            elif calculator=="IV":
                calcution+=4
            elif calculator=="IX":
                calcution+=9
            elif calculator=="XL":
                calcution+=40
            elif calculator=="XC":
                calcution+=90
            elif calculator=="CD":
                calcution+=400
            elif calculator=="CM":
                calcution+=900


        print(detailed_find)
        print(general_find)
        print(last_form)
        print(calcution)

            

        #general_find=re.findall()
a=Solution()
#a.romanToInt("III")

a.romanToInt("LVIII")
#a.romanToInt("MCMXCIV")  
        
        
        