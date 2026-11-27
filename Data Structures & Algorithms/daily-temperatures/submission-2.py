class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # l=len(temperatures)
        # res=[0]*l
        # for i in range(l):
        #     j=i+1
        #     for j in range(i+1,l):
        #         if temperatures[i]<temperatures[j]:
        #             res[i]=j-i
        #             break
        # return(res)

        # above approach takes O(N^2)
        
        # monotoic descreasing stack approach
        l=len(temperatures)
        res=[0]*l
        stack=[]
        for i in range(l):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop()
                res[j]=i-j
            stack.append(i)

        return res