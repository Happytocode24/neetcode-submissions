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
        
        l=len(temperatures)
        res = [0]*l
        # to push index in the stack 
        stack=[]
        for i in range(l):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                j=stack.pop() 
                res[j]=i-j
            stack.append(i)
        return res

        