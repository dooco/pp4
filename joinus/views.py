from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.template.defaultfilters import slugify
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
from .models import BoardFeature, Review, Category
from .forms import ReviewForm, PostForm


class BoardFeatureList(ListView):
    model = BoardFeature
    queryset = BoardFeature.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class BoardDetail(DetailView):
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
                "detail": detail,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "review_form": ReviewForm()
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
            review_form.instance.email = request.user.email
            review_form.instance.name = self.request.user
            review = review_form.save(commit=False)
            review.detail = detail
            review.save()
            review = review_form.save()
            messages.success(
                request, "Thank you, your review has been sent.")
        else:
            review_form = ReviewForm()

        return render(
            request,
            "board_detail.html",
            {
                "detail": detail,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "review_form": review_form,
            },
        )


class BoardLike(DetailView):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(BoardFeature, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('board_detail', args=[slug]))


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    feature = category.feature.filter(status=1)
    return render(request, 'category_detail.html', {
        'category': category,
        'feature': feature,
    })


class CategoryDetail(DetailView):
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
                "detail": detail,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "review_form": ReviewForm()
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
                "detail": detail,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "review_form": review_form,
            },
        )


def feature_detail(request, category_slug, slug):
    feature = get_object_or_404(BoardFeature, slug=slug)
    return render(request, 'board_detail.html', {
        'feature': feature
    })


class PostCreate(CreateView):
    model = BoardFeature
    fields = ['board_name', 'category', 'manufacturer', 'special_features', 'excerpt', 'featured_image',]
    template_name = 'post_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)

    # def get(self, request):
    #     form = self.(None)
    #     return render(request, self.template_name, {'form': form})

    # def form_valid(self, form):
    #     self.object = form.save(commit=False)
    #     self.object.author = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)
    
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     form.instance.slug = slugify(self.request.board_name)
    #     return super(PostCreate, self).form_valid(form)


class PostUpdate(UpdateView):
    model = BoardFeature
    fields = ['board_name', 'category', 'manufacturer', 'special_features', 'excerpt', 'featured_image',]
    success_url = reverse_lazy('home')


class PostDelete(DeleteView):
    model = BoardFeature
    success_url = reverse_lazy('home')
