class Solution:
	def trap(self, height: List[int]) -> int:
		n=len(height)
		#calculate aera square from left to right(spaceL) and right to left(spaceR)
		spaceL,spaceR=0,0
		maxL,maxR=0,0
		for i in range(n):
			if height[i]>maxL:
				maxL=height[i]
			if height[n-i-1]>maxR:
				maxR=height[n-i-1]
			spaceL+=maxL
			spaceR+=maxR
		#water space is spaceR+spaceL-rectangular-bars
		ans=spaceL+spaceR-maxL*len(height)-sum(height)
		return ans