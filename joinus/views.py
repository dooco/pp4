from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .models import BoardFeature, Review, Category
from .forms import ReviewForm, PostForm


def all_posts(request):
    """
    A view to show all posts 
    and display filtered category posts
    """
    
    category = request.GET.get('category')
    posts = BoardFeature.objects.all()
    if category:
        posts = posts.filter(category__slug=category)
    context = {
        'posts': posts,
    }
    return render(request, 'all_posts.html', context)


    def post(self, request, slug, *args, **kwargs):
        """
        A function to handle likes and commenting on articles
        """

        queryset = BoardFeature.objects.filter(status=1)
        board = BoardFeature.objects.get(slug=slug)
        detail = get_object_or_404(queryset, slug=slug)
        liked = False
        if detail.likes.filter(id=self.request.user.id).exists():
            liked = True
        form = ReviewForm(request.POST)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.name = request.user
            new_review.board = board
            new_review.save()
            messages.success(
                request, "Thank you, your review has been sent.")
        else:
            form = ReviewForm()

        comments = Review.objects.filter(board=board).order_by('-created_on')
        return render(
            request,
            "board_detail.html",
            {
                "board": board,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "form": form,
            },
        )


class BoardDetail(DetailView):
    """
    A view to handle detail view of article
    """
    def get(self, request, slug, *args, **kwargs):

        queryset = BoardFeature.objects.filter(status=1)
        detail = get_object_or_404(queryset, slug=slug)
        board = BoardFeature.objects.get(slug=slug)
        form = ReviewForm()
        comments = Review.objects.filter(board=board).order_by('-created_on')

        liked = False
        if detail.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "board_detail.html",
            {
                "board": board,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "form": form
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = BoardFeature.objects.filter(status=1)
        board = BoardFeature.objects.get(slug=slug)
        detail = get_object_or_404(queryset, slug=slug)
        liked = False
        if detail.likes.filter(id=self.request.user.id).exists():
            liked = True
        form = ReviewForm(request.POST)

        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.name = request.user
            new_review.board = board
            new_review.save()
            messages.success(
                request, "Thank you, your review has been sent.")
        else:
            form = ReviewForm()

        comments = Review.objects.filter(board=board).order_by('-created_on')
        return render(
            request,
            "board_detail.html",
            {
                "board": board,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "form": form,
            },
        )



class BoardLike(DetailView):
    """
    A view to handle likes
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(BoardFeature, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('board_detail', args=[slug]))


class CategoryDetail(DetailView):
    """
    A view to handle category detail dispaly
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = BoardFeature.objects.filter(status=1)
        detail = get_object_or_404(queryset, slug=slug)
        comments = detail.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if detail.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "board_detail.html",
            {
                "board": board,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "form": form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = BoardFeature.objects.filter(status=1)
        detail = get_object_or_404(queryset, slug=slug)
        comments = detail.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if detail.likes.filter(id=self.request.user.id).exists():
            liked = True
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = self.request.user.email
            review_form.instance.name = self.request.user
            review_form.instance.slug = slugify(self.request.board_name)
            review = review_form.save(commit=False)
            review.detail = detail
            print(review.detail)
            review.save()
            messages.success(
                request, "Thank you, your review has been sent.")
        else:
            review_form = ReviewForm()

        return render(
            request,
            "board_detail.html",
            {
                "board": board,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "form": form,
            },
        )


def feature_detail(request, category_slug, slug):
    """
    A view to handle feature detail display
    """
    feature = get_object_or_404(BoardFeature, slug=slug)
    return render(request, 'board_detail.html', {
        'feature': feature
    })


class PostCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A view to add new article
    """
    model = BoardFeature
    form_class = PostForm
    template_name = 'post_new.html'
    success_url = reverse_lazy('all_posts')
    success_message = "Your article has been saved. It will be published when Admin review."

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    """
    A view to edit an article
    """
    model = BoardFeature
    template_name = 'post_edit.html'
    fields = ['board_name', 'category', 'manufacturer', 'special_features', 'excerpt', 'featured_image', ]
    success_message = "Your article has been updated."

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('board_detail', kwargs={'slug': slug})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    """ 
    A view to delete an article
    """
    model = BoardFeature
    template_name = 'post_delete.html'
    success_url = reverse_lazy('all_posts')
    success_message = "Your article has been deleted."
    

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
