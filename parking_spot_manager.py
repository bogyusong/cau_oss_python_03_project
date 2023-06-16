class parking_spot:
    def __init__(self,name,ptype,city,district,latitude,longitude):
    #자원명부터 위도까지의 데이터를 받아 딕셔너리에 저장
        self.__item={
            'name': name,
            'ptype': ptype,
            'city':city,
            'district':district,
            'latitude':float(latitude),
            'longitude':float(longitude)
        } #위도와 경도는 실수 이므로 cast 연산자로 자료형 변환
    
    def get(self, keyword='name'):
    #키워드 따라서 value리턴하는 함수
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
def str_list_to_class_list(str_list): 
# parking_spot 클래스 객체의 리스트로 변환 후 반환하는 함수
    result = []
    for string in str_list:
            data = string.split(',') #콤마 기준으로 분리
            data = data[1:7] #번호 제외
            obj = parking_spot(*data) #객체 생성
            result.append(obj)
    return result

def print_spots(spots):
#리스트의 길이를 출력한 뒤 리스트에 저장된 모든 객체의 값을 출력하는 함수
    print(f'"---print elements({len(spots)})---"')

    for spot in spots:
        print_string = spot.__str__() #문자열 얻기
        print(print_string)



if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '?룞?옉')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)