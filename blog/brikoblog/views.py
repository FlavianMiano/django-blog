from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.
#def home(request):
 #   return render(request, 'home.html', {})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwags):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwags)
        context['cat_menu'] = cat_menu
        return context

class ArticleDetailview(DetailView):
    model = Post
    template_name = 'article_detail.html'

    def get_context_data(self, *args, **kwags):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailview, self).get_context_data(*args, **kwags)
        context['cat_menu'] = cat_menu
        return context

class AppPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class AppCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts' : category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all() 
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

#def LikeView(request, pk):
 #   post = get_object_or_404(Post, id=request.POST.get('post_id'))
  #  if post.likes.filter(id=request.user.id).exists():
   #     post.likes.remove(request.user)
    #else:
     #   post.likes.add(request.user)
    #return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))
