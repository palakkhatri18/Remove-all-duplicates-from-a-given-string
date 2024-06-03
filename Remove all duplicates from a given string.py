#Given a string str which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string. The order of remaining characters in the output should be same as in the original string.
class Solution:	
        def removeDuplicates(self,str):
            # code here
            str1=""
            for x in str:
                if x not in str1:
                    str1 = str1 + x
                
            return (str1)