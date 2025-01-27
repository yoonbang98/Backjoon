
def solution(n, k):
    number =''
    while n :
        b = n% k #나머지  
        number = str(b)+number #join으로 하면 나중에 뒤집어줘야함
        n = n // k  #몫

    word = number.split("0")
    answer = 0
    for w in word:
        if len(w) == 0 : continue
        if int(w) == 1 : continue
        sosu=True
        for i in range(2,int(int(w)**0.5)+1): # 소수찾기
            if int(w)%i==0:
                sosu=False
                break
        if sosu:
            answer+=1
    return answer