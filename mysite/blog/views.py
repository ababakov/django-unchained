from blog.models import Post
from django.views.generic import ListView, DetailView, FormView
from forms import NoUserCommentForm
# , UserCommentForm


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = NoUserCommentForm
        return context


class NoUserCommentFormView(FormView):
    form_class = NoUserCommentForm
    success_url = '/'
