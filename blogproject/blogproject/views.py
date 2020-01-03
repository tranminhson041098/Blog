from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    response = HttpResponse("Trang chủ của Son Blog")
    return response
def thongtin(request):
    header ="Trang lấy thông tin khách"
    context = {
        'header':header,
    }
    return render(request,'info.html',context)
def xulythongtin(request):
    if request.method=="GET":
        name = request.GET.get("name",'')
        gender = request.GET.get("gender","bạn")
        response = HttpResponse(f'Salute {gender} {name} ')
        
        return response
    else:
        name = request.POST.get("name",'')
        gender = request.POST.get("gender","bạn")

        if name=="Hoa Tran" and gender=="F":
            header = "Trang đặc biệt cho Hoa Tran"
            context={
                'header':header,
            }

            return render(request,'hoatran.html',context)
        else:
            return render(request,'friends.html')







       

    
    
   

