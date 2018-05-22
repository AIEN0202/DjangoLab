from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import modelscategory

# Create your views here.
def index(request):
    title="商品管理"
    
    return render(request,'product/index.html',locals())

def create(request):
    title="商品新增"
    # print(request.method);
    #POST
    if request.method == "POST" and request.FILES["ProductImage"]:
        myFile = request.FILES["ProductImage"]
        fs = FileSystemStorage()
        fs.save(myFile.name, myFile)

        # ModelNumber = request.POST['ModelNumber']
        # ModelName = request.POST['ModelName']
        # Description = request.POST['Description']
        # UnitCost = request.POST['UnitCost']
        # CategoryID = request.POST['CategoryID']
        # ProductImage = request.POST['ProductImage']

        #todo 把資料寫進資料庫
    
    #GET
    #回傳一個網頁，讓使用者可以輸入資料
    category = modelscategory.Category()
    datas = category.all()
    print(datas)
    return render(request,'product/create.html',locals())

def update(request):
    title="商品修改"
    return render(request,'product/update.html',locals())