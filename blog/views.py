from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import CommentForm, PostForm


class PostList(generic.ListView):

    """
    A view to display all posts on main blog page.
    """

    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 4


def home_view(request):

    """
    Sets the homepage template to render.
    """

    return render(request, 'index.html')


class PostContent(View):

    """
    A view to display the content for each post.
    """

    def get(self, request, slug):
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

    def post(self, request, slug):
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

    """
    A view to like posts.
    """

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(username=request.user.username).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_content', args=[slug]))


class UserPost(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    """
    A view to allow users to create a post.
    """

    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = '/'
    success_message = """ Your post has been submitted successfully!
                        We'll review it and post it soon.
                        In the meantime, why not going for another
                        dive on our blog? """

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdatePost(LoginRequiredMixin, SuccessMessageMixin,
                 UserPassesTestMixin, UpdateView):

    """
    A view to allow users to update a post.
    """

    template_name = 'post_form.html'
    success_url = '/'
    success_message = "Your post has been updated successfully!"

    model = Post
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    """
    A view to allow users to delete a post.
    """

    template_name = 'post_confirm_delete.html'
    success_url = '/'
    success_message = "Your post has been deleted successfully!"

    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
