from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from . import modelscategory
from . import modelsproduct

# Create your views here.
def index(request):
    title="商品管理"
    product = modelsproduct.Product()
    datas = product.all()
    # print(datas)
    return render(request,'product/index.html',locals())

def create(request):
    title="商品新增"
    # print(request.method);
    #POST
    if request.method == "POST" and request.FILES["ProductImage"]:
        #上傳檔案
        myFile = request.FILES["ProductImage"]
        fs = FileSystemStorage()
        fs.save(myFile.name, myFile)
        
        #取得表單透過POST傳過來的資料
        ModelNumber = request.POST['ModelNumber']
        ModelName = request.POST['ModelName']
        Description = request.POST['Description']
        UnitCost = request.POST['UnitCost']
        CategoryID = request.POST['CategoryID']
        ProductImage = myFile.name

        #todo 把資料寫進資料庫
        product = modelsproduct.Product()
        data = tuple([CategoryID,ModelNumber,ModelName,UnitCost,ProductImage,Description])
        product.create(data)
       
        return redirect('/product')
        
    #GET
    #回傳一個網頁，讓使用者可以輸入資料
    category = modelscategory.Category()
    datas = category.all()
    # print(datas)  #((),(),())
    return render(request,'product/create.html',locals())

def update(request):
    title="商品修改"
    return render(request,'product/update.html',locals())