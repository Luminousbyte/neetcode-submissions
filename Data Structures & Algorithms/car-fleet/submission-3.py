class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p, s in zip(position, speed):
            pair.append((p,s))
        pair.sort(reverse = True)

        fleet = 1
        prevTime = (target - pair[0][0])/pair[0][1]

        for i in range(1, len(pair)):
            currentCar = pair[i]
            currentTime = (target - currentCar[0])/currentCar[1]
            if currentTime > prevTime:
                fleet += 1
                prevTime = currentTime
        return fleet