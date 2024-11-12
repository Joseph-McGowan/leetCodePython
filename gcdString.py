class Solution(object):
    @staticmethod
    def gcdOfStrings(str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
        #return largest string x that divides both str1 and str2

        gcd_string = ""
        flag = 1

        #establish which string is larger

        #biggerString = (str1 if len(str1) > len(str2) else str2)

        c = [a for a,b in zip(str1,str2) if a == b]
        greatest_common_string = "".join(c)

        if greatest_common_string == "":
            return greatest_common_string

        i = 1
        while i <= len(greatest_common_string) + 1 :
            #try dividing strings to see if we have a common diviser
            diviserString = "".join(c[0:i])
            split_str1 = str1.split(diviserString)
            split_str2 = str2.split(diviserString)

            for a in split_str1:
                for b in split_str2:
                    if a != '' or b != '':
                        flag = 0

            if flag == 1:    
                gcd_string = diviserString
            
            flag = 1
            i += 1

        return gcd_string
    



def main():

    #Solution.gcdOfStrings( "LEET", "CODE")

    Solution.gcdOfStrings( "CXTXNCXTXNCXTXNCXTXNCXTXN", "CXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXNCXTXN")


main()
        
        
