class CountSquares:
    def __init__(self):
        self.points = {}

    def add(self, point: list[int]) -> None:
        p = (point[0], point[1])
        self.points[p] = self.points.get(p, 0) + 1

    def count(self, point: list[int]) -> int:
        qx, qy = point
        result = 0

        for (px, py), cnt in self.points.items():
            if abs(px - qx) != abs(py - qy):
                continue
            if px == qx or py == qy:
                continue

            corner1 = self.points.get((px, qy), 0)
            corner2 = self.points.get((qx, py), 0)

            result += cnt * corner1 * corner2

        return result