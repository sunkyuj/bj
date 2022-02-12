import sys

sys.setrecursionlimit(10 ** 8)
input = lambda: sys.stdin.readline().rstrip()

move = list(map(int, input().split()))
long = {(1, 3), (2, 4)}

i = 0
ans = 0
l, r = 0, 0

while i < len(move) - 1:
    to = move[i]

    if to == 0:
        break

    # left foot
    if l == 0:
        lcost = 2
    else:
        ldiff = abs(to - l)
        if ldiff == 0:
            lcost = 1
        elif ldiff == 1 or ldiff == 3:
            lcost = 3
        else:
            lcost = 4

    # right foot
    if r == 0:
        rcost = 2
    else:
        rdiff = abs(to - r)
        if rdiff == 0:
            rcost = 1
        elif rdiff == 1 or rdiff == 3:
            rcost = 3
        else:
            rcost = 4

    if lcost < rcost:
        ans += lcost
        l = to
    elif rcost < lcost:
        ans += rcost
        r = to
    else:  # same (두 발 쫙인 상태에서, 다음 움직임이 다리 사이 놈인 경우)
        if l == 0 or r == 0:
            if l == 0:
                l = to
            else:
                r = to
            ans += 2
        else:
            ans += 3
            j = i + 1
            while j < len(move) - 1 and move[j] == move[i]:
                ans += 1
                j += 1
            if j == len(move) - 1:
                break

            if move[j] == l:
                r = move[i]
                ans += 1
            elif move[j] == r:
                l = move[i]
                ans += 1
            else:
                l, r = move[i], move[j]
                ans += 3
            i = j
    i += 1
print(ans)

# 같은 지점 한 번 더 누를 때 1
# 중앙발이 다른 지점으로 움직일 때 2
# 다른 지점에서 인접한 지점으로 움직일 때는 3 (ex. 왼쪽-> 위 / 왼쪽 -> 아래)
# 반대편으로 움직일 때는 4 (ex. 위->아래)


"""while i < len(move) - 1:
    if l > r:
        l, r = r, l  # l 이 항상 작게

    if move[i] in (l, r):  # 현재 발 위치에 이미 있는 경우
        ans += 1
    elif (l, r) in long:  # 현재 발 위치랑 다르고, 쫙 찢어진 경우.  ( < 모양)
        ans += 3
        j = i + 1
        while j < len(move) - 1 and move[j] == move[i]:
            ans += 1
            j += 1
        if j == len(move) - 1:
            break

        if move[j] == l:
            r = move[j]
            ans += 1
        elif move[j] == r:
            l = move[j]
            ans += 1
        else:
            l, r = move[i], move[j]
            ans += 3
        i = j

    else:  # 쫙 찢어진게 아니라 한 쪽 사분면에 있는 경우
        ldiff, rdiff = abs(move[i] - l), abs(move[i] - r)
        if ldiff != 2:
            l = move[i]
        else:
            r = move[i]
        ans += 3
    i += 1

print(ans)"""
