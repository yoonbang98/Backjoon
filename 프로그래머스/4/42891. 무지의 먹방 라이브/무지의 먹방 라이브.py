from collections import defaultdict
def solution(food_times, k):
    N = len(food_times)
    if sum(food_times) <= k:
        return -1
    food_loc = defaultdict(list)
    for idx, t in enumerate(food_times):
        food_loc[t].append(idx)

    food_times.sort()
    height = 0
    for idx, t in enumerate(food_times):

        if t > height :
            tmp_time = (t-height)*(N-idx)
            height = t
            if k >= tmp_time:
                k -= tmp_time
                food_loc[food_times[idx]] = []
            else:
                k %= N-idx
                idx_list = []
                for key, value in food_loc.items():
                    idx_list += value
                idx_list.sort()
                return idx_list[k] + 1
        else:
            continue

