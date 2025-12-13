from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        line_order = {line: i for i, line in enumerate(valid_lines)}
        
        valid_coupons = []
        
        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if not c or not all(ch.isalnum() or ch == '_' for ch in c):
                continue
            if b not in line_order:
                continue
            
            valid_coupons.append((line_order[b], c))
        
        # Sort by businessLine order, then by code
        valid_coupons.sort()
        
        return [c for _, c in valid_coupons]
