#input is non-negative int array,use all numbers in the array 
#to complete a number,print the smallest number
#input [10,2]
#output "102"
#input [3,30,34,5,9]
#output"3033459"

class compareSmall(str):
	def _lt_(x,y):
		return x+y<y+x #compare str and sort from small to big

class Solution:
	def minNumber(self,nums:List[int])->str:
		res=sorted(map(str,nums),key=compareSmall)
		smallest=''.join(res)
		return smallest