from django.views.generic import ListView
from .models import Post

class HomePagePost(ListView):
    model = Post
    template_name = 'home_post.html'
    context_object_name = 'all_posts_list'

# Create your views here.
