class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        child = collections.defaultdict(list)
        branch = [0]*numCourses
        for i,j in prerequisites:
            child[j].append(i)
            branch[i]+=1
        q=collections.deque()
        for i in range(numCourses):
            if branch[i]==0:
                q.append(i)
        
        while q:
            node = q.popleft()
            for i in child[node]:
                branch[i]-=1
                if branch[i]==0:
                    q.append(i)
        
        for i in branch:
            if i!=0:
                return False
        return True