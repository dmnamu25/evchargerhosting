from django.shortcuts import render

f = open("/workspace/hosting/mysite/static/data.csv", 'r', encoding='cp949')
l=[]
lines = f.readlines()
for line in lines:
    l.append(line.split(','))
f.close

data =  l[1:300]

def index(request):
    return render(request, 'main/index.html', {'data':data})