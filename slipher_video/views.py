from django.shortcuts import render,HttpResponse
from django.template import loader
from httplib2 import ServerNotFoundError
from django.contrib.auth.decorators import login_required


from . import youtube_search



def home(request):
    return render(request,'slipher_video/home.html')

def search(request):
    query = request.GET.get('q','')

    if query:
        try:
            videos = youtube_search.youtube_search(query)
        except ServerNotFoundError:
            return HttpResponse("there must be a problem with the internet : check if you are connected to wifi or the data is on!")

    template = loader.get_template('slipher_video/search_result.html')
    context = {'videos':videos}
    return HttpResponse(template.render(context,request))

def watch_video(request,video_id):
    return render(request,"slipher_video/watch_video.html",{"video_id":video_id})


    
