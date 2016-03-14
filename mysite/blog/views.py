from django.views.generic import ListView, DetailView, FormView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


from blog.models import Post, Comment
from forms import NoUserCommentForm, UserCommentForm
# , UserCommentForm


class PostsListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated():
            context['form'] = UserCommentForm(
                initial={'post_id': context['post'].id})
        else:
            context['form'] = NoUserCommentForm(
                initial={'post_id': context['post'].id})
        return context


class CommentFormView(FormView):
    # form_class = UserCommentForm
    # success_url = '/'
    def get_form_class(self):
        if self.request.user.is_authenticated():
            return UserCommentForm
        else:
            return NoUserCommentForm

    def get_success_url(self):
        return reverse('blog:post-detail',
                       args=(self.request.POST['post_id'],))

    def form_valid(self, form):
        data = form.cleaned_data
        if self.request.user.is_authenticated():
            data['author'] = self.request.user
        Comment.objects.create(**data)
        return HttpResponseRedirect(self.get_success_url())
