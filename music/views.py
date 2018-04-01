from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render_to_response
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from music.download_music import SearchMusicinYoutube, ServerMusic, download_parralel,RequestSearch
from music.forms import SearchForm, SongForm
from music import models
from django.contrib.auth import get_user_model
from account import models as md
from django.http import Http404, HttpResponse
import json
from django.template import RequestContext
import datetime
import multiprocessing
import time

User = get_user_model()


def homepage(request):

    """Return start page"""
    
    
    audio = ServerMusic()
    form = SearchForm(request.POST or None)

    templ = {'songs' : audio, 'form' : form, 'message' : "Hi"}
    
    return render(request, "music/index.html",templ)

class PlayListView(LoginRequiredMixin, ListView):

    model = models.Song
    template_name = "music/user_list.html"

    def get_queryset(self):
        try:
            self.song_user = User.objects.prefetch_related("song").get(
                username__iexact=self.kwargs.get("username")
            )
        except User.DoesNotExist:
            raise Http404
        else:
                
            return self.song_user.song.order_by("pk").reverse()

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['form'] = SearchForm
        return context
    
def addsong(request):
    
    if request.POST:
        model = models.Song.objects.get_or_create(name=request.POST.get("song_name"),
                            url=request.POST.get("song_url"),
                            user=request.user,youtube_url=request.POST.get("youtube_url"))

        return HttpResponse("<h1>ТЫ КТО???????</h1>")

    return render_to_response('search_music', RequestContext(request))

def deleteSong(request):
    
    if request.POST:
        user = User.objects.get(username=request.user.username)
        instance = models.Song.objects.filter(name = request.POST.get("song_name"),
                                              user = user)
        instance.delete()

        return HttpResponse("instance")
        
    return render_to_response('user_page', RequestContext(request))

def search_music(request):

    form = SearchForm(request.POST or None)
    audio = []
    if request.method == "POST":
        if form.is_valid():
            all_video = RequestSearch(form.cleaned_data['search'],2)
            audio = SearchMusicinYoutube(all_video)
            
    templ = {'songs' : audio, 'form' : form}
    
    return render(request, "music/index.html",templ)


class BrandPlayListView(ListView):
    
    model = models.Song
    template_name = "music/brand.html"

    def get_queryset(self):
        self.song_user = User.objects.get(username="BrandMusic")
        return self.song_user.song.order_by("pk").reverse()

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['form'] = SearchForm
        return context


def DownloadBrand_music():

    while True:
        
        l = ["https://www.youtube.com/user/thesoundyouneed1","https://www.youtube.com/channel/UC3ifTl5zKiCAhHIBQYcaTeg",
            "https://www.youtube.com/channel/UCXKr4vbqJkg4cXmdvaAEjYw","https://www.youtube.com/user/UDUBSTEPHD/videos?disable_polymer=1"]
        
        for song in download_parralel(l):
            models.Song.objects.get_or_create(name=song.name,url=song.url,
            user=User.objects.get(username="BrandMusic"),youtube_url=song.youtube_url)
        time.sleep(3599)

t1 = multiprocessing.Process(target=DownloadBrand_music)
t1.start()