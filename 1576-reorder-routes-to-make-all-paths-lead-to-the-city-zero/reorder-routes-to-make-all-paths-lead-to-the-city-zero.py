class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbours = defaultdict(list)
        connection = set()

        for start,end in connections:
            neighbours[start].append(end)
            neighbours[end].append(start)
            connection.add((start,end))
        
        cur =[0]
        reverse =0
        visited = set()
        visited.add(0)

        while cur:
            new_cur =[]
            for city in cur:
                for n in neighbours[city]:
                    if n not in visited:
                        visited.add(n)
                        if (n,city) not in connection:
                            reverse+=1
                        new_cur.append(n)
            cur = new_cur
        
        return reverse