from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int


@dataclass
class EllipticCurve:
    pass


class ECPoint:

    @staticmethod
    def BasePointGGet() -> Point:
        pass

    @staticmethod
    def ECPointGen(x: int, y: int) -> Point:
        return Point(x, y)
    
    @staticmethod
    def IsOnCurveCheck(a: Point) -> bool:
        pass
    
    @staticmethod
    def AddECPoints(a: Point, b: Point) -> Point:
        try:
            m = (a.y - b.y) / (a.x - b.x)
        except Exception as e:
            m = 0
        x_r = m*m - a.x - b.x
        y_r = a.y + m * (x_r - a.x)

        return Point(x_r, y_r)

    @staticmethod
    def DoubleECPoints(point: Point, a: int) -> Point:
        x_r = ((3 * point.x * point.x + a) / (2 * point.y))**2 - 2 * point.x
        y_r = -point.y + ((3 * point.x * point.x + a) / (2 * point.y)) * (point.x - x_r)

        return Point(x_r, y_r)
        
    
    @staticmethod
    def ScalarMult(a : Point, k: int) -> Point:
        pass

    @staticmethod
    def ECPointToString(point: Point) -> str:
        pass
    
    @staticmethod
    def PrintECPoin(point: Point) -> str:
        print(ECPoint.ECPointToString(point))


print(ECPoint.AddECPoints(Point(1,2), Point(1,2)))

print(ECPoint.DoubleECPoints(Point(1, 2), -7))








    


