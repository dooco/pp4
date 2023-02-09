from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Board_feature, Review
from .forms import ReviewForm


class Board_featureList(generic.ListView):
    model = Board_feature
    queryset = Board_feature.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class Board_Detail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Board_feature.objects.filter(status=1)
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
        queryset = Board_feature.objects.filter(status=1)
        detail = get_object_or_404(queryset, slug=slug)
        comments = detail.comments.filter(approved=True).order_by('-created_on')
        liked = False
        if detail.likes.filter(id=self.request.user.id).exists():
            liked = True
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            user = User.objects.get(username=request.user)
            review = review_form.save(commit=False)
            review.detail = detail
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
                "review_form": review_form,
                "liked": liked,
            },
        )


class BoardLike(View):
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Board_feature, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('board_detail', args=[slug]))


# class BoardLike(View):
#     def post(self, request, slug, *args, **kwargs):
#         post = get_object_or_404(Board_feature, slug=slug)
#         if post.avg_rating.filter(id=request.user.id).exists():
#             post.avg_rating.remove(request.user)
#         else:
#             post.avg_rating.add(request.user)

        # return HttpResponseRedirect(reverse('board_detail', args=[slug]))
