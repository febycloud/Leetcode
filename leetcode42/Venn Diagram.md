Venn Diagram 

![image.png](https://pic.leetcode-cn.com/60f50754e0b15a27def14e54887a357c7f16dd0c7f767e963fc306144c3d16e1-image.png)

Space from left to right:

no mater water or the bar, we can just got all the space included,

everytime we just add the space which value is depend on the heighest bar, so the spaceL is

SpaceL +=maxL

![image.png](https://pic.leetcode-cn.com/2749a1e1805a9f22bba66e259f75c95cdab5d36413ee47b7f923107ff49583d0-image.png)

Space from right to left:

same 

SpaceR +=maxR



![image.png](https://pic.leetcode-cn.com/a20ea5560f99de54f6dcd508e72d8527da74a39bb51e1e98f4f6621fc8aa1451-image.png)

now we have a Space which spaceL+spaceR was included all the rectangle

and the duplicate space is spaceBar and spaceWater

so

water=spaceR+spaceL-retangle-spaceBar