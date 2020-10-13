from django.contrib import auth
from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import register
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Article, Comment
from django.views.generic import ListView
from .serializer import ArticleSerializer
from .forms import ArticleForm, CommentForm, EmailForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .utils import ObjectDetailMixin



def post_list(request):
    object_list = Article.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, 'article_list.html', {'articles': articles, 'page': page})




class ArticleUpdateView(UpdateView):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')




class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_create.html'
    fields = ('title', 'body', 'image')


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)



class CommentCreateView(CreateView):
    model = Comment
    template_name = 'new_comment.html'
    fields = ('body',)


    def form_valid(self, form):
        form.instance.comment = self.request.user
        form.instance.comment = get_object_or_404(Comment,
                                                  id=self.kwargs.get('article_pk'))
        return super().form_valid(form)





class ArticleDetailView(DetailView):

    model = Article
    template_name = 'article_detail.html'


@login_required
def post_share(request, article_id):
    post = get_object_or_404(Article, id=article_id)
    sent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = '{} ({}) recommends you reading "{}"'.format(cd['name'], cd['email'], post.title)
            message = 'Read "{}" at \n{}\'s comments: {}'.format(post.title, cd['name'], cd['comments'])
            send_mail(subject, message, 'myrzakanovsultan0@gmail.com',[cd['to']])
            sent = True
    else:
        form = EmailForm()
    return render(request, '    share.html', {'post': post,
                                                    'form': form,
                                                    'sent': sent})


# def post_search(request):
#
#     form = SearchForm(request.GET)
#
#     cd = form.cleaned_data
#
#     results = Article.objects.filter(content=cd['query']).load_all()
#     total_results = results.count()
#     return render(request,
#                   'search.html',
#                   {'form': form,
#                    'cd': cd,
#                    'results': results,
#                    'total_results': total_results})

# def post_search(request):
#     form = SearchForm()
#     if 'query' in request.GET:
#         form = SearchForm(request.GET)
#         cd = form.cleaned_data
#         results = SearchQuerySet().models(Article).filter(content=cd['query']).load_all()
#             # count total results
#         total_results = results.count()
#         return render(request,
#                   'search.html',
#                   {'form': form,
#                    'cd': cd,
#                    'results': results,
#                    'total_results': total_results})
#
