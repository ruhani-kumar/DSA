class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        capacity = 0 
        boxTypes.sort(key=lambda x: -x[1])

        for box,units in boxTypes:
            if truckSize>=box:
                capacity += box*units
                truckSize -= box
            else:
                capacity += truckSize*units
                break
        return capacity