from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Board_feature
from .forms import ReviewForm


class Board_featureList(generic.ListView):
    model = Board_feature
    queryset = Board_feature.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class BoardDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Board_feature.objects.filter(status=1)
        board = get_object_or_404(queryset, slug=slug)
        comments = board.comments.filter(approved=True).order_by('created_on')
        liked = False
        if board.avg_rating.filter(id=self.request.user.id).exists():
            rate = True

        return render(
            request, 
            "board_detail.html",
            {
                "board": board,
                "comments": comments,
                "commented": False,
                "rate": rate,
                "review_form": ReviewForm()
            },
        )

    def board(self, request, slug, *args, **kwargs):
        queryset = Board_feature.objects.filter(status=1)
        board = get_object_or_404(queryset, slug=slug)
        comments = board.comments.filter(approved=True).order_by('created_on')
        liked = False
        if board.avg_rating.filter(id=self.request.user.id).exists():
            rate = True
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.post = post
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request, 
            "board_detail.html",
            {
                "board": board,
                "comments": comments,
                "commented": True,
                "rate": rate,
                "review_form": ReviewForm()
            },
        )



def login(request):
    return render(request, 'login.html')
