import math
from collections import defaultdict
from typing import List

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        n = len(points)
        if n < 4:
            return 0
        
        # Data structure for Trapezoid detection
        # Key: Slope (dy, dx)
        # Value: Dict {Intercept -> Count of segments}
        # We group by slope, then subgroups by line equation (intercept) to handle collinearity
        lines_by_slope = defaultdict(lambda: defaultdict(int))
        
        # Data structure for Parallelogram detection
        # Key: Midpoint (2*mx, 2*my) 
        # Value: Dict {Slope -> Count of segments}
        midpoints = defaultdict(lambda: defaultdict(int))
        
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                
                # 1. Calculate Slope (dy/dx) in canonical form
                dy = y1 - y2
                dx = x1 - x2
                g = math.gcd(dy, dx)
                dy //= g
                dx //= g
                
                # Ensure canonical representation of slope (handle signs)
                if dx < 0 or (dx == 0 and dy < 0):
                    dx = -dx
                    dy = -dy
                slope = (dy, dx)
                
                # 2. Calculate Intercept to distinguish parallel vs collinear lines
                # Line eq: dy*x - dx*y + C = 0  => C = dx*y - dy*x
                intercept = dx * y1 - dy * x1
                
                lines_by_slope[slope][intercept] += 1
                
                # 3. Calculate Midpoint for parallelogram detection
                # We use sum (2 * midpoint) to avoid float division issues
                mx = x1 + x2
                my = y1 + y2
                midpoints[(mx, my)][slope] += 1
        
        total_trapezoids_count = 0
        
        # Phase 1: Count pairs of segments that are parallel but on DIFFERENT lines
        for slope, intercept_map in lines_by_slope.items():
            counts = list(intercept_map.values())
            total_segments_with_slope = sum(counts)
            
            # Calculate pairs from different lines:
            # Total Pairs - Pairs from same line (which are collinear, not trapezoids)
            # Mathematical shortcut: (Sum^2 - Sum(squares)) / 2
            pairs = (total_segments_with_slope**2 - sum(c*c for c in counts)) // 2
            total_trapezoids_count += pairs
            
        # Phase 2: Count Parallelograms
        # A parallelogram is formed by two segments that share a midpoint but have DIFFERENT slopes
        parallelogram_count = 0
        for midpoint, slope_map in midpoints.items():
            counts = list(slope_map.values())
            total_segments_at_midpoint = sum(counts)
            
            # Calculate pairs with different slopes:
            pairs = (total_segments_at_midpoint**2 - sum(c*c for c in counts)) // 2
            parallelogram_count += pairs
            
        # Phase 3: Deduplicate
        # total_trapezoids_count currently contains:
        #   1x count for every Non-Parallelogram Trapezoid
        #   2x count for every Parallelogram (once for each pair of parallel sides)
        # We want Parallelograms counted only once.
        # Result = (Non-P + 2*P) - P = Non-P + P
        
        return total_trapezoids_count - parallelogram_count
