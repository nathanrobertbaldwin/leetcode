# def trap(height):
#     area = 0

#     left = 0
#     right = 1


#     test_max = -1
#     test_max_idx = -1

#     while left < len(height) - 1:
#         if right - left > 1 and height[left] <= height[right]:
#             small_peak = min(height[left], height[right])
#             for i in range(left + 1, right):
#                 area += small_peak - height[i]

#             left = right
#             right += 1

#         elif right == len(height) - 1 and test_max > -1:
#             right = test_max_idx

#             while height[left + 1] > height[right]: left += 1

#             small_peak = min(height[left], height[right])
#             for i in range(left + 1, right):
#                 area += small_peak - height[i]

#             left = right
#             right += 1

#         elif height[left] <= height[right]:
#             left += 1
#             right += 1

#         elif height[left] > height[right]:
#             if height[right] >= test_max:
#                 test_max = height[right]
#                 test_max_idx = right

#             right += 1

#     return area


def trap(height):
    area = 0

    left = 0
    right = 1

    max_height = height[0]
    max_idx = 0

    while right < len(height):
        if height[right] >= max_height:
            max_height = height[right]
            max_idx = right

        if right - left > 1 and height[left] <= height[right]:
            small_peak = min(height[left], height[right])
            for i in range(left + 1, right):
                area += small_peak - height[i]

            left = right
            right += 1

        elif height[left] <= height[right]:
            left += 1
            right += 1

        elif height[left] > height[right]:
            right += 1

    right -= 1
    left = right - 1

    while left >= max_idx:
        if right - left > 1 and height[left] >= height[right]:
            small_peak = min(height[left], height[right])
            for i in range(left + 1, right):
                area += small_peak - height[i]

            right = left
            left -= 1

        elif height[right] >= height[left]:
            left -= 1

        elif height[right] < height[left]:
            left -= 1
            right -= 1

    return area


print(trap([4, 2, 3]))
