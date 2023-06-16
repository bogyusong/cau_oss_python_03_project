class parking_spot:
    def __init__(self,name,ptype,city,district,latitude,longitude):
    #�ڿ������ ���������� �����͸� �޾� ��ųʸ��� ����
        self.__item={
            'name': name,
            'ptype': ptype,
            'city':city,
            'district':district,
            'latitude':float(latitude),
            'longitude':float(longitude)
        } #������ �浵�� �Ǽ� �̹Ƿ� cast �����ڷ� �ڷ��� ��ȯ
    
    def get(self, keyword='name'):
    #Ű���� ���� value�����ϴ� �Լ�
        return self.__item[keyword]
    
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s
    
def str_list_to_class_list(str_list): 
# parking_spot Ŭ���� ��ü�� ����Ʈ�� ��ȯ �� ��ȯ�ϴ� �Լ�
    result = []
    for string in str_list:
            data = string.split(',') #�޸� �������� �и�
            data = data[1:7] #��ȣ ����
            obj = parking_spot(*data) #��ü ����
            result.append(obj)
    return result

def print_spots(spots):
#����Ʈ�� ���̸� ����� �� ����Ʈ�� ����� ��� ��ü�� ���� ����ϴ� �Լ�
    print(f'"---print elements({len(spots)})---"')

    for spot in spots:
        print_string = spot.__str__() #���ڿ� ���
        print(print_string)



if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    # import file_manager
    # str_list = file_manager.from_file("./input/free_parking_spot_seoul.csv")
    # spots = str_list_to_class_list(str_list)
    # print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '?��?��')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)