def delete_ok(answer):
    for x,y,a in answer:
        if a == 0 : #기둥
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                pass
            else:
                return False
        else : # 보
            if [x,y-1,0] in answer or [x+1, y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                pass
            else:
                return False
    return True
def solution(n, build_frame):
    answer = []
    for x,y,a,b in build_frame:
        if b == 1: #설치
            if a == 0 : #기둥 설치
                if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                    answer.append([x,y,a])
            else : # 보 설치
                if [x,y-1,0] in answer or [x+1, y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                    answer.append([x,y,a])
        else : # 삭제
            answer.remove([x,y,a])
            if not delete_ok(answer):
                answer.append([x,y,a])
            
    answer.sort()
    return answer