class StockSpanner(object):

    def __init__(self):
        self.stack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        ans = 1
        while self.stack and self.stack[-1][0] <= price:
            ans += self.stack.pop()[1]
        self.stack.append((price, ans))
        return ans

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

#作者：smoon1989
#链接：https://leetcode-cn.com/problems/online-stock-span/solution/dong-tai-gui-hua-dan-diao-zhan-python3-by-smoon198/
#来源：力扣（LeetCode）
#著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#此处做法为动态规划和单调stack实现，这道题的本质是寻找每个数左边第一个比它严格大的数字，故可以采用单调栈的思想