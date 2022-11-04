import json
import time
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"posts/index.html")

def posts(request):
    start= int(request.GET["start"] or 0)
    end = int(request.GET["end"] or (start+9))
    
    data=[]
    for i in range(start,end+1):
        data.append(f"Post #{i}")

    time.sleep(1)
    # return HttpResponse(json.dumps(data));
    return JsonResponse(data,safe=False)