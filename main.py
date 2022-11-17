from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


@dataclass
class EllipticCurve:
    a: float
    b: float


class ECPoint:

    @staticmethod
    def BasePointGGet() -> Point:
        pass

    @staticmethod
    def ECPointGen(x: float, y: float) -> Point:
        return Point(x, y)

    @staticmethod
    def IsOnCurveCheck(a: Point, curve: EllipticCurve) -> bool:
        return a.y**2 - a.x**3 - curve.a*a.x - curve.b == 0

    @staticmethod
    def AddECPoints(a: Point, b: Point) -> Point:

        m = (a.y - b.y) / (a.x - b.x)

        x_r = m*m - a.x - b.x
        y_r = a.y + m * (x_r - a.x)

        return Point(x_r, -y_r)

    @staticmethod
    def DoubleECPoints(point: Point, a: int) -> Point:
        x_r = ((3 * point.x * point.x + a) / (2 * point.y))**2 - 2 * point.x
        y_r = -point.y + ((3 * point.x * point.x + a) /
                          (2 * point.y)) * (point.x - x_r)

        return Point(x_r, y_r)

    @staticmethod
    def ScalarMult(a: Point, k: int, curve: EllipticCurve) -> Point:

        res_point = a
        i = 1
        while i < k:
            if i * 2 > k:
                res_point = ECPoint.AddECPoints(res_point, a)
                i += 1
            else:
                res_point = ECPoint.DoubleECPoints(res_point, curve.a)
                i *= 2

        return res_point

    @staticmethod
    def ECPointToString(point: Point) -> str:
        return point.__str__()

    @staticmethod
    def PrintECPoint(point: Point) -> None:
        print(ECPoint.ECPointToString(point))


curve = EllipticCurve(-7, 10)
#print(ECPoint.AddECPoints(Point(1,2), Point(1,2)))
#print(ECPoint.IsOnCurveCheck(Point(4, 5), curve=curve))
print(ECPoint.ScalarMult(Point(1, 2), 4, curve))
#print(ECPoint.DoubleECPoints(Point(1, 2), -7))
