class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)  # key -> array of (time, values)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        if timestamp < self.map[key][0][0]:
            return ""

        values = self.map[key]
        lo = 0
        hi = len(self.map[key]) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            midTime = values[mid][0]
            if midTime == timestamp:
                return values[mid][1]
            elif midTime > timestamp:
                hi = mid - 1
            else:
                lo = mid + 1
        return values[hi][1]
