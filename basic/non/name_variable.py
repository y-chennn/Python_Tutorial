def cal_score(s1, s2, s3):
    n = s1 * 0.2
    m = (70 + s2) * 0.4
    f = (80 + s3) * 0.4

    return n + m + f


def calculate_score(attend: int, midterm: int, final: int) -> float:
    roll_call_weight = 0.2
    midterm_weight = 0.4
    final_weight = 0.4

    score = attend * roll_call_weight + midterm * midterm_weight + final * final_weight

    return score
