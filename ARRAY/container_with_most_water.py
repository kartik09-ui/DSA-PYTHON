def maxArea(self, height: list[int]) -> int:
    n = len(height)
    left = 0
    right = n-1
    max = float('-inf')
    while left<=right:
        area = (right-left) * min(height[left],height[right])
        if area > max:
            max = area
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max