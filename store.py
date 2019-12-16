import os
import datetime

class Product :
    def __init__(self, number, title, price, stock, isuse=True):
        self.number = number
        self.title = title
        self.price = price
        self.stock = stock
        self.isuse = isuse

def viewProduct():
    if len(product_list) == 0 :
        print("등록한 물품이 없습니다.")        
    else :
        print("번호 판매여부      물품번호     물품명      단가        재고    ")
        print("-------------------------------------------------------------")
        for index, value in enumerate(product_list) :
            print("[{0:3d}][{1:4s}] {2:10s} {3:10s}{4:10d}{5:10d}"
                  .format(index+1, "판매중" if value.isuse else "판매종료",
                          value.number, value.title, value.price,
                          value.stock))
    return len(product_list)

def viewSale_Date() :
    filenames = os.listdir(path)
    list = {}
    
    if len(filenames) > 0:
        for filename in filenames :            
            file_ext = os.path.splitext(filename);
            if  file_ext[-1] == ".sale" :
                with open(os.path.join(path,filename)) as file :                    
                    dt = file_ext[0]
                    for line in file :
                        datas = line.strip().split('|')                                
                        if len(datas) == 3 :                                    
                            number = datas[0]
                            price = int(datas[1])
                            count = int(datas[2])
                            totalprice = price * count

                            if dt in list.keys() :
                                if number in list[dt].keys():
                                    #list[dt][number][1]+=price
                                    list[dt][number][2]+=count
                                    list[dt][number][3]+=totalprice
                                else :                                            
                                    list[dt][number] = [product_title[number],price, count,
                                                        totalprice]                                                                            
                            else :
                                list[dt] = {}
                                list[dt][number] = [product_title[number],price, count, totalprice]


    for fkey, fvalue in list.items() :            
        print('')
        print(fkey, '>>')
        for skey, svalue in fvalue.items() :                    
            print(skey, svalue[0], svalue[1], svalue[2], svalue[3])

def viewSale_Prod() :
    filenames = os.listdir(path)
    list = {}
    
    if len(filenames) > 0:
        for filename in filenames :            
            file_ext = os.path.splitext(filename);
            if  file_ext[-1] == ".sale" :
                with open(os.path.join(path,filename)) as file :                    
                    dt = file_ext[0]
                    for line in file :
                        datas = line.strip().split('|')                                
                        if len(datas) == 3 :                                    
                            number = datas[0]
                            price = int(datas[1])
                            count = int(datas[2])
                            totalprice = price * count

                            if number in list.keys() :
                                if dt in list[number].keys():
                                    #list[number][dt][0]+=price
                                    list[number][dt][1]+=count
                                    list[number][dt][2]+=totalprice
                                else :                                            
                                    list[number][dt] = [price, count, totalprice]                                                                            
                            else :
                                list[number] = {}
                                list[number][dt] = [price, count, totalprice]


    for fkey, fvalue in list.items() :            
        print('')
        print(fkey, product_title[fkey] ,'>>')
        for skey, svalue in fvalue.items() :                    
            print(skey,":", svalue[0], svalue[1], svalue[2])


            
product_title = {}
product_list = []
path = "c:\\prod"
file_prod = "product.dat"

if __name__ == '__main__' :
    if os.path.isdir(path) :
        f = os.path.join(path, file_prod)
        if os.path.isfile(f) :
            with open(f,'r',encoding='UTF8') as file :                
                for line in file :
                    datas = line.strip().split('|')
                    if len(datas) == 5 :
                        number = datas[0]
                        title = datas[1]
                        price = int(datas[2])
                        stock = int(datas[3])
                        isuse = datas[4] == '1'

                        product_list.append(Product(number,title
                                                    ,price,stock,isuse))
                        product_title[number] = title
                    
    else :
        os.makedirs(path)


    print("재고 등록 프로그램입니다.")
   
    while True:
        print("")
        print("1.물품등록")
        print("2.물품판매")
        print("3.판매현황")
        print("4.판매중지")
        print("5.재고변경")  
        print("---------")        
        print("0.종료")
        
        selmenu = int(input("\n작업선택:"))

        if selmenu == 1 :
            #20181206-001|연필|1000|10|1
            print("물품 등록을 하세요")
            title = input("품명:")
            price = int(input("단가:"))
            stock=int(input("재고:"))

            prefix = datetime.datetime.now().strftime("%Y%m%d")

            postfix = 0;
            for product in product_list :
                if prefix in product.number :
                    seq = int(product.number[-3:])
                    if postfix <= seq :
                        postfix = (seq+1)                        
            number = '{0}-{1:03d}'.format(prefix, postfix)

            product_list.append(Product(number,title,price,stock))
            product_title[number] = title
            
            with open(os.path.join(path, file_prod), 'a',encoding='UTF8') as file :
                file.write("{0}|{1}|{2}|{3}|{4}".format(number,title,price,stock,1))
                file.write('\n')
                
            print("[{0}]{1} 물품을 등록하였습니다.".format(number, title))
            
            
        elif selmenu == 2:
            print("물품 판매을 하세요")            
            if 0 == viewProduct() :
                continue
            
            idx = int(input("번호:")) - 1
            if 'y' == input('{0} 제품이 맞습니까?(y/n)'.format(product_list[idx].title)).lower() :
                if product_list[idx].isuse :
                    count = int(input("수량:"))
                    if count > product_list[idx].stock :
                        print("현재 재고 수량이 없습니다.")
                    else :
                        f = os.path.join(path,
                                         datetime.datetime.now().strftime("%Y-%m-%d.sale"))
                        with open(f, 'a',encoding='UTF8') as file :                            
                            file.write("{0}|{1}|{2}\n".format(product_list[idx].number,product_list[idx].price,count))
                            product_list[idx].stock -= count
                        
                else :
                    print(product_list[idx].title, "물품판매가 불가능합니다.")
                
        elif selmenu == 3:
            print("판매 현황을 조회하세요")            

            print("1. 날짜별")
            print("2. 물품별")
            sel = int(input("번호:"))
            if sel == 1:
                viewSale_Date()
            elif sel == 2 :
                viewSale_Prod()
                          
        elif selmenu == 4:
            print("판매 중단을 하세요")           
            viewProduct()
            idx = int(input("번호:")) - 1
            if 'y' == input('{0} 제품이 맞습니까?(y/n)'.format(product_list[idx].title)).lower() :
                product_list[idx].isuse = False
                print(product_list[idx].title, "물품을 판매 중지하였습니다.")
                                
        elif selmenu == 0:
            with open(os.path.join(path, file_prod), 'w',encoding='UTF8') as file :
                for p in product_list :
                    file.write("{0}|{1}|{2}|{3}|{4}\n".format(p.number,p.title,p.price,p.stock,"1" if p.isuse else "0"))
                    
            print("프로그램을 종료합니다.")
            break;
        
