class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start_station = 0
        total_gas = 0
        total_cost = 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            tank += gas[i] - cost[i]

            #if tank is negative, we can't travel to the next
            if tank < 0:
                start_station = i+1 #set to next station
                tank = 0 #reset tank

        return start_station if total_gas >= total_cost else -1
       
            
