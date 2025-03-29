from line_segment import LineSegment
from point import Point
from typing import List

class FastCollinearPoints:
    def __init__(self, points: List[Point]):
        #corner cases
        if points is None:
            raise ValueError("Input is null.")
        
        for p in points:
            if p is None:
                raise ValueError("Input contains null.")
        
        #make a sorted copy of points[] to prevent mutating og data
        local_points = sorted(points)
        
        for i in range(1, len(local_points)):
            if local_points[i] == local_points[i - 1]:
                raise ValueError("Input contains duplicate.")
        
        self.segments_list = []

        if len(local_points) > 3:
            for p in local_points:
                sorted_points = sorted(local_points, key=p.slope_to)
                self._find_segments(sorted_points, p)
    
    def number_of_segments(self) -> int:
        return len(self.segments_list)
    
    def segments(self) -> List[LineSegment]:
        return self.segments_list.copy()
    
    def _find_segments(self, points: List[Point], p: Point):
        start = 1
        slope = p.slope_to(points[1])
        
        for i in range(2, len(points)):
            temp_slope = p.slope_to(points[i])
            if temp_slope != slope:
                if i - start >= 3:
                    segment_points = self._gen_segment(points, p, start, i)
                    if segment_points[0] == p:
                        self.segments_list.append(LineSegment(segment_points[0], segment_points[1]))
                start = i
                slope = temp_slope
        
        if len(points) - start >= 3:
            last_points = self._gen_segment(points, p, start, len(points))
            if last_points[0] == p:
                self.segments_list.append(LineSegment(last_points[0], last_points[1]))
    
    def _collinear_slope(self, s1: float, s2: float) -> bool:
        return s1 == s2
    
    def _gen_segment(self, points: List[Point], p: Point, start: int, end: int) -> List[Point]:
        segment_points = [p] + points[start:end]
        segment_points.sort()
        return [segment_points[0], segment_points[-1]]
