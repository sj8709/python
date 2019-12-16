#201444032 정성준

class Product :
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.amout = 0
        self.total = 0

    def buy(self,cnt=1) :
        if(self.stock < cnt): # 재고보다 많은 판매량일 경우
            print('{0}의 판매할 재고 수량이 없음' .format(self.name))
        else:
            ck = input(('{0}의 총 판매가격은 {1}원 구매하시겠습니까(Y/N)?' .format(self.name, self.price*cnt)))
            if (ck == 'y' or ck =='Y'): #'y'일 경우
                print('{0}제품 {1}개 총 {2}원에 판매하였습니다.' .format(self.name, cnt, self.price*cnt))
                self.stock -= cnt
                self.amout += cnt
                self.total += self.price*cnt
            elif(ck =='n' or ck =='N'): #'n'일 경우
                pass
            else: # 다른 값 입력시
                print('Y/N 둘중 하나를 선택 잘못된 값 입력')
                
    def currentState(self):
        print('제품명:{0} 단가:{1} 재고:{2}' .format(self.name, self.price, self.stock))

    def totalState(self):
        print('제품명:{0} 총 판매 수량:{1} 총 판매 금액:{2}' .format(self.name, self.amout, self.total))

def rankTotalPrice(list) :
    temp_list = [] #정렬 전 임시 리스트
    for i in range(len(list)):
        temp = []
        temp.append(list[i].name)
        temp.append(int(list[i].total))
        temp_list.append(temp) #임시 리스트에 각 항목 값을 삽입

    sort1 = sorted(temp_list, key=lambda x: x[1], reverse=True) #내림차순 정렬
    for j in range(len(sort1)): #출력
        print('{0} : {1} / {2}' .format(j+1,sort1[j][0], sort1[j][1]))

if __name__ == "__main__" :
    product_list = [ Product(name="연필", price=1000, stock=10)
                   , Product("샤프", 3000, 5)
                   , Product("공책", 2000, 5)
                   , Product("볼펜", 1000, 5)]

    
    print("#1"); product_list[0].buy()
    print("#2"); product_list[0].buy()
    print("#3"); product_list[1].buy(10)
    print("#4"); product_list[2].buy(2)
    print("#5"); product_list[2].buy(1)
    print("#6"); product_list[3].buy(2)

    print("#7")
    for p in product_list :
        p.currentState()
        p.totalState()
        print()

    print("#8")
    rankTotalPrice(product_list)
