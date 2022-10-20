class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        
        queue = deque([start])
        step = 0
        memory = {}
        def create_variations(gene):
            v = []
            for i in range(len(gene)):
                for j in ["A", "C", "G", "T"]:
                    yield gene[:i] + j + gene[i+1:]
        
        while queue:
            lens = len(queue)
            i = 0 
            while i < lens:
                node = queue.pop()
                if node == end:
                    return step
                for variation in create_variations(node):
                    if variation not in memory and variation in bank:
                        memory[variation] = True
                        queue.appendleft(variation)
                i += 1
            step += 1
        return -1