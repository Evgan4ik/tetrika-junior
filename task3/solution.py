def appearance(intervals: dict[str, list[int]]) -> int:
    start = intervals['lesson'][0]
    end = intervals['lesson'][1]

    def cut_intervals(times):
        result = []
        for i in range(0, len(times), 2):
            start_time = max(times[i], start)
            end_time = min(times[i + 1], end)
            if start_time < end_time:
                result.append([start_time, end_time])
        return result
    
    pupil_times = cut_intervals(intervals['pupil'])
    tutor_times = cut_intervals(intervals['tutor'])
    
    def join_intervals(times):
        if not times:
            return []
        times.sort()
        result = [times[0]]
        for current in times[1:]:
            if current[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], current[1])
            else:
                result.append(current)
        return result
    
    pupil_joined = join_intervals(pupil_times)
    tutor_joined = join_intervals(tutor_times)
    
    total = 0
    for p in pupil_joined:
        for t in tutor_joined:
            start = max(p[0], t[0])
            end = min(p[1], t[1])
            if start < end:
                total += end - start
    
    return total

tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       if test_answer == test['answer']:
           print(f'Тест No{i} прошел успешно')
       else:
           print(f'Тест No{i} не прошел')

    
    

    
    
    
