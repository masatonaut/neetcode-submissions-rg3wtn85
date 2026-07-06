from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)

        if "0000" in dead:
            return -1

        def neighbors(state):
            result = []
            for i in range(4):
                digit = int(state[i])
                for move in (1, -1):
                    new_digit = (digit + move) % 10
                    new_state = state[:i] + str(new_digit) + state[i+1:]
                    result.append(new_state)
            return result

        queue = deque([("0000", 0)])
        visited = {"0000"}

        while queue:
            state, turns = queue.popleft()
            if state == target:
                return turns
            for next_state in neighbors(state):
                if next_state not in visited and next_state not in dead:
                    visited.add(next_state)
                    queue.append((next_state, turns + 1))

        return -1