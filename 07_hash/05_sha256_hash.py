import hashlib


data_list = ["hello", "Hello", "secure", "hash", "algorithm"]

for data in data_list:
    # 입력 데이터를 utf-8 인코딩을 통해 바이트 형식으로 변환
    data_bytes = data.encode('utf-8')
    print(data_bytes)
    # hashlib의 sha256 함수를 사용하여 해시 객체 생성
    hash_object = hashlib.sha256(data_bytes)
    print(hash_object)
    # 해시 객체를 16진수 문자열로 변환하여 반환
    result = hash_object.hexdigest()
    print("입력 '{}'의 해시 값: {}".format(data, result))
