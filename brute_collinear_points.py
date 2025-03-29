from line_segment import LineSegment
from point import Point
from itertools import combinations


class BruteCollinearPoints:
    def __init__(self, points: list[Point]):
        # Corner cases
        if points is None:
            raise ValueError("Input is null")
        if any(p is None for p in points):
            raise ValueError("Input contains null")
        
        #make a sorted copy of points[] to prevent mutating og data
        local_points = sorted(points)

        # checking dupicats pts
        for i in range(1, len(local_points)):
            if local_points[i] == local_points[i - 1]:
                raise ValueError("Input contains duplicate")
            
        self.segment_list = []

        if len(local_points) > 3:
            for c in combinations(local_points, 4):
                if self.is_collinear(c):
                    self.segment_list.append(self.get_segment(c))

    def number_of_segments(self) -> int:
        return len(self.segments)

    def segments(self) -> list[LineSegment]:
        return self.segment_list
    
    def get_segment(self, points: tuple[Point, Point, Point, Point]) -> LineSegment:
        sorted_points = sorted(points)
        return LineSegment(sorted_points[0], sorted_points[3])
    
    def is_collinear(self, points: tuple[Point, Point, Point, Point]) -> bool:
        slope1 = points[0].slope_to(points[1])
        slope2 = points[0].slope_to(points[2])
        slope3 = points[0].slope_to(points[3])
        return slope1 == slope2 == slope3