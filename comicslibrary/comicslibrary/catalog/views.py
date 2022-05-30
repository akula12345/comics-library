from django.shortcuts import render
from .models import Genre, Comic, Publisher
from django.views import generic



def index(request):
	num_comics = Comic.objects.all().count()
	num_publishers = Publisher.objects.all().count()

	return render(request, 'index.html' ,context={'num_comics': num_comics, 'num_publishers': num_publishers},)


class ComicListView(generic.ListView):
    model = Comic
    paginate_by = 10

class ComicDetailView(generic.DetailView):
    model = Comic


class PublisherListView(generic.ListView):
    model = Publisher
    paginate_by = 10

class PublisherDetailView(generic.DetailView):
    model = Publisher