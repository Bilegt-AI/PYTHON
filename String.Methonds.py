phone_number=input("Enter Your Phone #: ")

name=input("Enter Your Full Name: ")
result=len(name) #len гэдэг нь lenght гэдэг үгний товчлол бөгөөд үгний хэдэн үсэгтэйг тогтооно.
result=name.find("i") #find гэдэг нь үгнээс үсэг олох ба тэр үсэг нь яг хэд дэх дараалалд байгааг олно. Python учраас 0-ээс эхэлж тооцоолно.
result=name.rfind("i") #r.find гэдэг нь дээрх үйлдлийг яг эсрэг нь ба "r" гэдэг нь reverse гэдэг үгний товчлол.
name=name.capitalize() #эхний үсгийг томсгоно. 
name=name.upper() #бүх үсгийг томсгоно. 
name=name.lower() # бүх үсгийг жижиг болгоно.
result=name.isdigit() #энэ нь гараас өгсөн өгөгдөл зөвхөн тоо байвал True гэдэг утга хэвлэнэ, хэрэв дунд нь үсэг орсон байвал False заана!
result=name.isalpha() #энэ нь гараас өгөгдөл оруулахад бүгд үсэг байгаа тохиолдолд True харин тоо болоод зай байгаа тохиолдолд False гэсэн утга хэвлэнэ.
result=phone_number.count("-")

phone_number=phone_number.replace("-","")
print(phone_number)
