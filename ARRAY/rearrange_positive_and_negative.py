def rearrangeArray(self, nums: list[int]) -> list[int]:
        final_ans = [0] * len(nums)
        pos_idx = 0
        neg_idx = 1
        for val in nums:
            if val >= 0:
                final_ans[pos_idx] = val
                pos_idx +=2

            else:
                final_ans[neg_idx] = val
                neg_idx +=2

        return final_ans