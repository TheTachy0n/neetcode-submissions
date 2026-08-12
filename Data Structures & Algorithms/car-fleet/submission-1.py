class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Stack
        - create a sorted array of tuples of the position and speed and call them cars
        - create an empty stack
        - in a for loop consider 2 variables the pos and spd in the reversed array
        - we know the time taken by each
        - apply the condition-> if not in stack or time> stack[-1] -> append to the stack
        - return the length of the stack
        '''
        cars = sorted(zip(position,speed))
        stack = []
        for pos, spd in reversed(cars):
            time = (target - pos)/spd

            if not stack or time > stack[-1]:
                stack.append(time)
            
        return len(stack)