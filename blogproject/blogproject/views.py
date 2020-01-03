from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    response = HttpResponse("Trang chủ của Son Blog")
    return response
def thongtin(request):
    header ="Trang lấy thông tin khách"
    list_of_most_frequented=[]
    list_of_most_frequented.append("Mark Nguyen")
    list_of_most_frequented.append("Luong Bao Yen")
    list_of_most_frequented.append("Quan Nguyen")
    context = {
        'header':header,
        'number':111,
        'list_frequented':list_of_most_frequented,
    }
    
    # context={
    #     'header':header
    # }
    return render(request,'info.html',context=context)
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

            return render(request,'hoatran.html',context=context)
        else:
            return render(request,'friends.html')







       

    
    
   

