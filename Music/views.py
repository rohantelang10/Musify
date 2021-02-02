from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import Album,Song
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.views.generic import View
from .forms import UserForm

class HomeView(generic.ListView):
    template_name = 'Home.html'

    def get_queryset(self):
        '''
        if request.method == "GET":
            pass
        else:
            return Album.objects.all()
        '''
        return Album.objects.all()

class PlayerView(generic.DetailView):
    model=Album
    template_name='player.html'

class AlbumCreate(CreateView):
    model=Album
    template_name='album_form.html'
    fields = ['artist','album_title','genre','album_logo']

class AlbumUpdate(UpdateView):
    model=Album
    template_name='album_form.html'
    fields = ['artist','album_title','genre','album_logo']

class AlbumDelete(DeleteView):
    model=Album
    success_url=reverse_lazy('Home')

class UserFormView(View):
    form_class=UserForm
    template_name='registration_form.html'

    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            user=form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user=authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('Home')
        return render(request,self.template_name,{'form':form})

class SongAdd(CreateView):
    model = Song
    template_name = 'song_form.html'
    fields = ['song_title','song_file']

    def get_success_url(self):
        return reverse("player", kwargs={'pk': self.kwargs['pk']})



    def form_valid(self, form):
        album = Album.objects.get(pk=self.kwargs['pk'])
        form.instance.album = album
        return super(SongAdd, self).form_valid(form)

class SongDelete(DeleteView):
    model=Song


    #def post(self,request):
    #print(self.kwargs['pk'])
    #print(request.POST["song_album_id"])
    success_url = reverse_lazy('Home')
    #def get_success_url(self):
        #print(request.POST["song_album_id"])
        #success_url = reverse_lazy('Home')
        #print("this is the printed primary key",self.kwargs['pk'])
        #return reverse("player", kwargs={'pk': self.kwargs['pk']})
