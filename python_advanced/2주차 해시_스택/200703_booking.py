# for in 구문에 map 함수 활용해보기


def solution(seat):
    # set 활용하여 중복 좌석 제거
    set_seat = set(map(tuple, seat))
    '''
    위와 같이 아래 문장을 간소화할 수 있음
    더불어 set_seat에 대한 선언문도 생략 가능
    for each_seat in seat:
        set_seat.add(tuple(each_seat))
    '''
    return len(set_seat)