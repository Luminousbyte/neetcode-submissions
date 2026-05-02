class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p,s in zip(position, speed):
            pair.append((p,s))

        pair.sort(reverse = True)

        prevTime = (target - pair[0][0])/pair[0][1]
        fleet = 1
        for i in range(1, len(pair)):
            currcar = pair[i]
            currTime = (target - currcar[0])/currcar[1]
            if currTime > prevTime:
                fleet += 1
                prevTime = currTime
        return fleet