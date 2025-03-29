from line_segment import LineSegment
from point import Point


class FastCollinearPoints:
    def __init__(self, points: list[Point]):
        # YOUR CODE HERE
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
            
        self.segments = []
        if len(local_points) > 3:
            for p in local_points:
                sorted_points = sorted(local_points, key=p.slope_to)
                self.find_segments(sorted_points, p)

    def number_of_segments(self) -> int:
        return len(self.segments)

    def segments(self) -> list[LineSegment]:
        return self.segments
    
