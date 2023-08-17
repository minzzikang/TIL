T = 10
for tc in range(1, T+1):
    N = int(input())  # 건물 개수
    buildings = list(map(int, input().split()))  # 건물들의 높이
    cnt = 0  # 조망권 확보한 세대 수  (초기화 할 필요 없음)

    # 건물의 꼭대기에서부터 확인하다가 양옆에 두 자리에 건물 만나면 멈추고 다음 건물로
    for i in range(2, N-2):  # 2번째에 위치한 건물부터 N-2번째 위치한 건물까지 확인

        for j in range(buildings[i], -1, -1):  # i번째 빌딩의 맨 위 높이부터 0층까지 위에서 아래로 확인

        # i번째 빌딩의 높이인 j가 양옆 2칸까지의 건물의 높이보다 높으면 조망권 있는 세대
            if j > buildings[i-1] and j > buildings[i-2] and j > buildings[i+1] and j > buildings[i+2]:
                cnt += 1

            else:
                break  # 조건 만족 안하면 굳이 0층까지 다 확인할 필요 x

    
    print(f'#{tc} {cnt}')