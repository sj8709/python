#201444032 정성준

class Score :
    ratio = {"mid":30,"fin":30,"hw":20,"att":20}

    def __init__(self):
        self.mid = 0
        self.fin = 0
        self.hw = 0
        self.att = 0

    def total(self):
        return self.mid + self.fin + self.hw + self.att
    
    def grade(self):
        score = self.total()
        if score >= 90 :
            result = "A"
        elif score >= 80 :
            result = "B"
        elif score >= 70 :
            result = "C"
        elif score >= 60 :
            result = "D"
        else :
            result = "F"
        return result
        
    def setScore(self,text,num,total=100):
        if text == "mid":
            self.mid = num / total * self.ratio["mid"]
        elif text == "fin":
            self.fin = num / total * self.ratio["fin"]
        elif text == "hw":
            self.hw = num / total * self.ratio["hw"]
        elif text == "att":
            self.att = num / total * self.ratio["att"]
        else :
            print("항목을 잘못 입력하셨습니다.")


def rank(list):
    temp_list = [] #정렬 전 임시 리스트
    for key in list.keys():
        temp = []
        temp.append(key)
        temp.append(list[key].total())
        temp_list.append(temp)

    sort1 = sorted(temp_list, key=lambda x: x[1], reverse=True) #내림차순 정렬
    for i in range(len(temp_list)):
        print('{0} : {1} / {2}' .format(i+1,sort1[i][0], sort1[i][1]))

if __name__ == "__main__" :
    score_list = {}
    score_list["김아영"] = Score()
    score_list["최미소"] = Score()
    score_list["윤선영"] = Score()

    print("#1")
    score_list["김아영"].setScore("중간",70)
    score_list["김아영"].setScore("mid",70)
    score_list["김아영"].setScore("fin",80)
    score_list["김아영"].setScore("hw",100)
    score_list["김아영"].setScore("att",100)
    score_list["최미소"].setScore("mid",30,30)
    score_list["최미소"].setScore("fin",28,30)
    score_list["최미소"].setScore("hw",20,20)
    score_list["최미소"].setScore("att",20,20)
    score_list["윤선영"].setScore("mid",40,50)
    score_list["윤선영"].setScore("fin",20,50)
    score_list["윤선영"].setScore("hw",100)
    score_list["윤선영"].setScore("att",100)

    print("#2")
    for k,v in score_list.items() :
        print("이름:{0} 총점:{1} 학점:{2}".format(k,v.total(),v.grade()))

    print("#3")
    rank(score_list)
