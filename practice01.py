## 실습 문제 1: 신호 세기 지형 만들기와 완전 탐색
'''
드론이 직선 위를 오가며 지상 송신기의 신호 세기를 측정합니다. 신호 세기는 위치 `x` 하나로 결정되며, 세기가 강한 지점이 여러 곳에 흩어져 있습니다. 
먼저 목적 함수와 그 지형을 만들고, 후보 지점을 하나도 빼지 않고 모두 재 보는 완전 탐색으로 신호가 가장 센 지점을 찾습니다. 완전 탐색은 모든 후보를 평가하므로 후보 중 최선을 반드시 찾지만, 후보의 수만큼 평가해야 합니다.


| 봉우리 | 높이 A | 중심 c | 폭 sigma |
|---|---|---|---|
| 1 | 1.00 | 3.0 | 1.0 |
| 2 | 0.60 | -2.0 | 0.8 |
| 3 | 0.45 | 7.5 | 1.2 |

- 요구사항:
    1. 표의 세 봉우리를 더해 `signal_1d(x)` 를 완성하세요. `x` 가 실수일 때와 numpy 배열일 때 모두 동작해야 합니다. (힌트: `np.exp`)
    2. 후보 `candidates` 를 하나씩 모두 평가해 신호가 가장 센 위치, 그 신호, 평가한 횟수를 반환하는 `brute_force_1d(f, candidates)` 를 완성하세요. (힌트: 이론 1장의 `brute_force_tsp` 처럼 지금까지의 최선을 갱신)
        - `f` 자리에는 `signal_1d` 같은 함수가 통째로 들어오므로 함수 안에서 `f(x)` 로 부르면 됩니다 (4주차 "함수도 하나의 객체"). 예: `brute_force_1d(signal_1d, xs)`
        - numpy 배열도 리스트처럼 `for x in candidates` 로 하나씩 꺼낼 수 있습니다
    3. -6부터 11까지를 500개로 나눈 `xs` 전체에서 전역 최댓값을, `x < 0` 인 후보와 `x > 6` 인 후보만 골라 넣어 지역 최댓값 두 개를 찾고, 곡선 위에 세 지점을 표시하세요. (힌트: `xs[xs < 0]`, `plt.plot`, `plt.scatter`, `plt.annotate`)
    4. -6과 11을 포함해 후보를 10개, 100개, 1000개로 바꿔 가며 완전 탐색하고, 찾은 위치와 신호가 평가 횟수에 따라 어떻게 달라지는지 비교하세요. 참 최댓값은 x ≈ 3.00, 신호 ≈ 1.000입니다. (힌트: `np.linspace(-6, 11, n)`)
'''

import numpy as np
import matplotlib.pyplot as plt

def signal_1d(x):
    # TODO: A * np.exp(-((x - c) ** 2) / (2 * sigma ** 2)) 꼴의 봉우리 세 개를 더해 반환하세요.
    return x - x    # 자리표시(항상 0): 지우고 작성하세요


def brute_force_1d(f, candidates):
    best_x, best_val, n_eval = None, -np.inf, 0
    # TODO: candidates 의 모든 x 에서 f(x) 를 재고, 지금까지의 best_val 보다 크면 best_x, best_val 을 갱신하세요.
    #       잰 횟수는 n_eval 에 세세요.
    return best_x, best_val, n_eval


def report_1d(result):
    """완전 탐색 결과 (위치, 신호, 평가 횟수)를 읽기 좋은 문자열로 바꿔 줍니다. 수정하지 마세요."""
    x, val, n = result
    if x is None:
        return "아직 없음"
    return "x = {0:.2f}, 신호 = {1:.3f}, 평가 {2}번".format(float(x), float(val), n)


print('signal_1d(3.0), (-2.0), (7.5) 기대값: 1.000 0.600 0.450')
print('signal_1d(3.0), (-2.0), (7.5) 실제값: {0:.3f} {1:.3f} {2:.3f}'.format(
    float(signal_1d(3.0)), float(signal_1d(-2.0)), float(signal_1d(7.5))))
# 봉우리 중심은 폭 sigma 가 틀려도 맞게 나올 수 있으므로 중심이 아닌 곳도 비교합니다.
print('signal_1d(-1.0), (1.0), (5.0), (9.0) 기대값: 0.275 0.136 0.187 0.206')
print('signal_1d(-1.0), (1.0), (5.0), (9.0) 실제값: {0:.3f} {1:.3f} {2:.3f} {3:.3f}'.format(
    float(signal_1d(-1.0)), float(signal_1d(1.0)), float(signal_1d(5.0)), float(signal_1d(9.0))))


xs = np.linspace(-6, 11, 500)

# TODO: xs 전체에서 완전 탐색으로 전역 최댓값을 찾으세요.
global_best = (None, None, 0)
# TODO: xs 중 x < 0 인 후보와 x > 6 인 후보만 골라 각각 완전 탐색해 지역 최댓값을 찾으세요.
local_left = (None, None, 0)
local_right = (None, None, 0)

print('전역 최댓값 기대값: x = 2.99, 신호 = 1.000, 평가 500번')
print('전역 최댓값 실제값:', report_1d(global_best))
print('x < 0 지역 최댓값 기대값: x = -2.01, 신호 = 0.600, 평가 177번')
print('x < 0 지역 최댓값 실제값:', report_1d(local_left))
print('x > 6 지역 최댓값 기대값: x = 7.49, 신호 = 0.450, 평가 147번')
print('x > 6 지역 최댓값 실제값:', report_1d(local_right))


expected = {10: 'x = 3.44, 신호 = 0.907, 평가 10번',
            100: 'x = 2.93, 신호 = 0.998, 평가 100번',
            1000: 'x = 3.00, 신호 = 1.000, 평가 1000번'}
for n in [10, 100, 1000]:
    # TODO: -6 과 11 을 포함해 n 개로 나눈 후보로 완전 탐색해 result 에 담으세요.
    result = (None, None, 0)
    print('후보 {0}개 기대값: {1}'.format(n, expected[n]))
    print('후보 {0}개 실제값: {1}'.format(n, report_1d(result)))
