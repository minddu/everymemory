# 뷰: 기능을 담당(페이지 단위)
# 화면이 나타나는 뷰, 화면이 없는 뷰
# 화면이 있건 없건 주소 URL은 있어야 한다. 

# 뷰 내용(함수, 클래스), URL이 있으면 동작한다.

# 뷰의 코드 형식 : 함수형, 클래스형
# 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수, 
#           내가 원하는대로 동작들을 설계하고 만들고 싶을 때
# 클래스형 : CRUD 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고
#           상속받아서 사용한다.
# 장고의 제네릭 뷰를 많이 사용
# from django.http import HttpResponse
from django.shortcuts import render
def index(request): 
    return render(request, 'index.html')

def memory(request):
    return render(request, 'memory.html')