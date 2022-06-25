from django.shortcuts import (
                            render,
                            get_object_or_404,
                            reverse,
                            )
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 4


def HomeView(request):
    return render(request, 'index.html')


class PostContent(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(username=self.request.user.username).exists():
            liked = True

        return render(
            request,
            'post_content.html',
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(username=self.request.user.username).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            'post_content.html',
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked,
            },
        )


class PostLike(View):

    def post(self, request, slug, *arg, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(username=request.user.username).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_content', args=[slug]))


class UserPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = '/'
    success_message = """ Your post has been submitted successfully!
                        We'll review it and post it soon.
                        In the meantime, why not going for another
                        dive on our blog? """

    # fields = ['image', 'title', 'content']
    # summernote_fields = ('content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, SuccessMessageMixin,
                 UserPassesTestMixin, UpdateView):

    template_name = 'post_form.html'
    success_url = '/'
    success_message = "Your post has been updated successfully!"

    model = Post
    form_class = PostForm
    # fields = ['image', 'title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    template_name = 'post_confirm_delete.html'
    success_url = '/'
    success_message = "Your post has been deleted successfully!"

    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
