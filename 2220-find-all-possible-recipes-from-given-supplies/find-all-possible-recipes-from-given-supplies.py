from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # n = len(recipes), k = avg of len of ingredient per recipe, m = initial len of supplies
        # Time and Space complexity: O(nk + m)
        indegree = {}
        graph = defaultdict(list)
        answer = []

        for i in range(len(recipes)):
            indegree[recipes[i]] = len(ingredients[i])

            for ingredient in ingredients[i]:
                graph[ingredient].append(recipes[i])

        queue = deque(supplies)

        while queue:
            item = queue.popleft()

            for recipe in graph[item]:
                indegree[recipe] -= 1

                if indegree[recipe] == 0:
                    queue.append(recipe)
                    answer.append(recipe)

        return answer