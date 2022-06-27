class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outgoing_count = {}
        for path in paths:
            city_a, city_b = path
            outgoing_count[city_a] = outgoing_count.get(city_a, 0) + 1
            outgoing_count[city_b] = outgoing_count.get[city_b, 0]

        for city in outgoing_count:
            if outgoing_count[city] == 0:
                return city
