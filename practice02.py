'''
## 실습 문제 2: 2차원 신호 지도와 완전 탐색

이번에는 드론이 평면 위를 움직입니다. 봉우리가 네 개인 신호 지도에서, 격자 위의 모든 지점을 재 보는 완전 탐색으로 신호가 가장 센 지점을 찾고 지점마다의 신호를 모은 지도를 그립니다. 그리고 차원이 늘면 완전 탐색의 평가 횟수가 어떻게 되는지 계산합니다.

$$ h(x, y) = \sum_k A_k \exp\left( -\frac{(x - cx_k)^2}{2 sx_k^2} - \frac{(y - cy_k)^2}{2 sy_k^2} \right) $$

| 봉우리 | 높이 A | 중심 (cx, cy) | 폭 (sx, sy) |
|---|---|---|---|
| 1 | 1.00 | (1.0, 1.5) | (1.0, 1.0) |
| 2 | 0.70 | (-2.5, 1.0) | (1.2, 0.8) |
| 3 | 0.55 | (2.0, -2.5) | (0.8, 1.2) |
| 4 | 0.50 | (-1.5, -2.0) | (0.9, 0.9) |

- **요구사항:**
    1. `PEAKS_2D` 의 봉우리를 모두 더해 `signal_2d(x, y)` 를 완성하세요. `x`, `y` 가 numpy 배열이어도 동작해야 합니다. 다른 봉우리의 꼬리가 조금씩 더해지므로 봉우리 중심의 신호는 표의 높이 A와 같거나 약간 큽니다.
    2. `xs`, `ys`(각각 -5부터 5까지 101개)의 모든 조합 `(x, y)` 를 평가해 신호가 가장 센 지점, 그 신호, 평가한 횟수를 반환하는 `brute_force_2d(f, xs, ys)` 를 완성하세요. (힌트: `for` 문 두 겹, 문제 1의 `brute_force_1d`)
    3. 반복문 없이 지도 `Z` 를 한 번에 계산하고 확인하세요.
        - `xs` 를 `(1, 101)`, `ys` 를 `(101, 1)` 모양으로 바꿔 `signal_2d` 에 넣으면 7주차 브로드캐스팅 규칙대로 양쪽이 함께 늘어나, 행이 `y`, 열이 `x` 인 `(101, 101)` 지도가 됩니다. (힌트: `reshape(1, -1)`, `reshape(-1, 1)`)
        - `Z.max()` 가 완전 탐색의 신호와 소수 셋째 자리까지 같은지 확인하세요. 행과 열이 바뀌어도 shape와 최댓값은 같으므로 `Z[65, 60]` 도 꼭 비교하세요.
        - 제공된 `show_map` 으로 지도를 그려, 별(완전 탐색 결과)이 가장 높은 봉우리에, 흰 x 표시가 각 색 덩어리의 중심에 놓이는지 확인하세요.
    4. 축마다 101개 지점을 재는 완전 탐색이 1·2·3·10차원에서 몇 번 평가해야 하는지 `counts` 에, 초당 100만 번 평가할 때 10차원에 걸리는 햇수를 `years` 에 구하세요. (힌트: 파이썬 정수로 `[101 ** d for d in [1, 2, 3, 10]]` — NumPy 정수 배열로 거듭제곱하면 10차원에서 값이 넘쳐 깨집니다. 1년은 `3600 * 24 * 365`초)

## Practice Problem 2: A 2D Signal Map and Brute-Force Search

This time, the drone moves across a plane. On a signal map with four peaks, use brute-force search, which measures every point on the grid, to find the point with the strongest signal, and draw a map that collects the signal at each point. Then calculate what happens to the number of brute-force evaluations as the number of dimensions grows.

$$ h(x, y) = \sum_k A_k \exp\left( -\frac{(x - cx_k)^2}{2 sx_k^2} - \frac{(y - cy_k)^2}{2 sy_k^2} \right) $$

| Peak | Height A | Center (cx, cy) | Width (sx, sy) |
|---|---|---|---|
| 1 | 1.00 | (1.0, 1.5) | (1.0, 1.0) |
| 2 | 0.70 | (-2.5, 1.0) | (1.2, 0.8) |
| 3 | 0.55 | (2.0, -2.5) | (0.8, 1.2) |
| 4 | 0.50 | (-1.5, -2.0) | (0.9, 0.9) |

- **Requirements:**
    1. Complete `signal_2d(x, y)` by summing all the peaks in `PEAKS_2D`. It must work even when `x` and `y` are numpy arrays. Because the tails of the other peaks add a little to each one, the signal at a peak's center is equal to or slightly greater than the height A in the table.
    2. Complete `brute_force_2d(f, xs, ys)`, which evaluates every combination `(x, y)` of `xs` and `ys` (each with 101 points from -5 to 5) and returns the point with the strongest signal, that signal value, and the number of evaluations performed. (Hint: two nested `for` loops, `brute_force_1d` from Problem 1)
    3. Compute the map `Z` all at once without loops, and check it.
        - If you reshape `xs` to shape `(1, 101)` and `ys` to shape `(101, 1)` and pass them into `signal_2d`, both are stretched together according to the broadcasting rules from Week 7, producing a `(101, 101)` map whose rows are `y` and whose columns are `x`. (Hint: `reshape(1, -1)`, `reshape(-1, 1)`)
        - Check that `Z.max()` matches the brute-force signal to three decimal places. Since the shape and the maximum stay the same even if rows and columns are swapped, be sure to compare `Z[65, 60]` as well.
        - Draw the map with the provided `show_map` and check that the star (the brute-force result) sits on the highest peak and that the white x marks sit at the center of each colored blob.
    4. Compute in `counts` how many evaluations a brute-force search measuring 101 points per axis needs in 1, 2, 3, and 10 dimensions, and compute in `years` how many years the 10-dimensional case would take at 1 million evaluations per second. (Hint: use Python integers, `[101 ** d for d in [1, 2, 3, 10]]` — raising a NumPy integer array to a power overflows and breaks at 10 dimensions. One year is `3600 * 24 * 365` seconds)
'''

import numpy as np



# 아래 상수와 도우미 함수는 수정하지 말고 그대로 사용하세요.
PEAKS_2D = [
    (1.00, 1.0, 1.5, 1.0, 1.0),
    (0.70, -2.5, 1.0, 1.2, 0.8),
    (0.55, 2.0, -2.5, 0.8, 1.2),
    (0.50, -1.5, -2.0, 0.9, 0.9),
]


def report_2d(result):
    """2차원 완전 탐색 결과 ((x, y), 신호, 평가 횟수)를 읽기 좋은 문자열로 바꿔 줍니다."""
    p, val, n = result
    if p is None:
        return "아직 없음"
    return "(x, y) = ({0:.2f}, {1:.2f}), 신호 = {2:.3f}, 평가 {3}번".format(
        float(p[0]), float(p[1]), float(val), n)


def signal_2d(x, y):
    # TODO: PEAKS_2D 의 (A, cx, cy, sx, sy) 로 만든 봉우리를 모두 더해 반환하세요.
    #   A * np.exp(-((x - cx) ** 2 / (2 * sx ** 2) + (y - cy) ** 2 / (2 * sy ** 2)))
    return (x - x) + (y - y)    # 자리표시(항상 0): 지우고 작성하세요


def brute_force_2d(f, xs, ys):
    best_p, best_val, n_eval = None, -np.inf, 0
    # TODO: xs 와 ys 의 모든 조합 (x, y) 에서 f(x, y) 를 재고, 지금까지보다 크면
    #       best_p 를 (x, y) 로, best_val 을 그 신호로 갱신하세요. 잰 횟수는 n_eval 에 세세요.
    return best_p, best_val, n_eval


xs = np.linspace(-5, 5, 101)
ys = np.linspace(-5, 5, 101)

print('봉우리 중심 signal_2d 기대값: 1.009 0.703 0.550 0.501  <- 다른 봉우리의 꼬리가 더해져 높이 A와 같거나 약간 큼')
print('봉우리 중심 signal_2d 실제값:',
      ' '.join('{0:.3f}'.format(float(signal_2d(cx, cy))) for _, cx, cy, _, _ in PEAKS_2D))

best = brute_force_2d(signal_2d, xs, ys)
print('완전 탐색 기대값: (x, y) = (1.00, 1.50), 신호 = 1.009, 평가 10201번')
print('완전 탐색 실제값:', report_2d(best))
# xs 와 ys 에 서로 다른 후보를 넣어도 맞게 동작하는지 확인 (x < 0 구역의 지역 최댓값)
print('x < 0 구역 기대값: (x, y) = (-2.50, 1.00), 신호 = 0.703, 평가 5050번')
print('x < 0 구역 실제값:', report_2d(brute_force_2d(signal_2d, xs[xs < 0], ys)))

# TODO: xs 를 (1, 101), ys 를 (101, 1) 모양으로 바꿔 signal_2d 에 넣어 지도 Z 를 한 번에 만드세요.
Z = None

print('Z.shape 기대값: (101, 101) / 실제값:', None if Z is None else np.shape(Z))
print('Z.max() 기대값: 1.009 (완전 탐색으로 찾은 신호와 같음) / 실제값:',
      None if Z is None else round(float(np.max(Z)), 3))
print('Z[65, 60] 기대값: 1.009  <- 행 65는 y = 1.5, 열 60은 x = 1.0 / 실제값:',
      None if Z is None or np.ndim(Z) != 2 else round(float(Z[65, 60]), 3))


# TODO: 축마다 101개 지점일 때 1, 2, 3, 10차원의 평가 횟수 목록과, 초당 100만 번 평가할 때 10차원에 걸리는 햇수를 구하세요.
counts = None
years = None

print('평가 횟수 기대값: [101, 10201, 1030301, 110462212541120451001]  <- 1, 2, 3, 10차원 (10차원은 약 1.10e+20)')
print('평가 횟수 실제값:', counts)
print('10차원 소요 기대값: 3.50e+06년 (약 350만 년)')
print('10차원 소요 실제값:', None if years is None else '{0:.2e}년'.format(years))
