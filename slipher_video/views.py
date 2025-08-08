from django.shortcuts import render,HttpResponse
from django.template import loader
from httplib2 import ServerNotFoundError
from django.contrib.auth.decorators import login_required


from .youtube_search import (video_search,playlist_search)



def home(request):
    return render(request,'slipher_video/home.html')

def search(request):
    video_type = request.GET.get('type','')

    if video_type == 'video':
        try:
            query = request.GET.get('q','')
            video_length = request.GET.get('video_length','medium')
            videos = video_search(query,video_length=video_length)
        except ServerNotFoundError:
            return HttpResponse("there must be a problem with the internet : check if you are connected to wifi or the data is on!")
        template = loader.get_template('slipher_video/search_result.html')
        context = {'videos':videos}
        return HttpResponse(template.render(context,request))

    elif video_type == 'playlist':
        try :
            query = request.GET.get('q','')
            playlists = playlist_search(query)
        except ServerNotFoundError:
            return HttpResponse("there must be a problem with the internet : check if you are connected to wifi or the data is on!")
        template = loader.get_template('slipher_video/playlist_result.html')
        context = {'playlists':playlists}
        return HttpResponse(template.render(context,request))
    
    elif video_type == 'channel':
        return HttpResponse("channel search is not implemented yet")
    elif video_type == 'all':
        return HttpResponse("all search is not implemented yet")

def watch_video(request,video_id):
    return render(request,"slipher_video/watch_video.html",{"video_id":video_id})


    
