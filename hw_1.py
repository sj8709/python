#201444032 정성준

def totalprint(score_list):

        sort1 = sorted(score_list.items(), key=lambda x: x[1][1], reverse=True) #정렬
        for i in range (len(sort1)):
            print('이름:{0} 과목:{1} 평균:{2}'.format(sort1[i][0],sort1[i][1][0], sort1[i][1][1]))
        
        
            
                

 
dic_temp = {} #받은 값 넣을 딕셔너리
ck_score = 1 #평균 내기위한 카운트
ck_count = False
while(1): # 'n' 들어올때 까지 무한 루프
    ck = input('성적을 입력하시겠습니까?(Y,N)')
    if(ck == 'y' or ck =='Y'):  #'Y'일 경우
        ck_count = True
        list_temp = []
        key = input('이름:')
        subject = input('과목:')
        try :
                score = int(input('성적:'))
        except:
                print('성적에는 숫자만 입력하세요')
        ck_key = key in dic_temp
        if (ck_key == True): #이미 key 값이 존재할 경우
            ck_score += 1
            temp = dic_temp[key] #기존 key 값의 value를 가져옴
            temp[0] += subject #기존 과목값에 과목 더함
            temp_avg = (int(temp[1]) + int(score)) / ck_score #평균 계산
            temp[1] = temp_avg
            dic_temp[key] = temp
        else:
            list_temp.append(subject)            
            list_temp.append(score)
            dic_temp[key] = list_temp
        
    elif(ck == 'n' or ck =='N'): #'N'일 경우
        if(ck_count == False):
                print('입력한 성적이 없습니다.')
                break
        else:
                totalprint(dic_temp)
                break
    else: #그외 값일 경우
        print('y/n 둘 중 하나를 선택하세요')
