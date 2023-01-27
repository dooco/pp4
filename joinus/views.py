from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
from .models import Board_feature
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
        comments = detail.board.filter(approved=True).order_by('created_on')
        rate = False
        if detail.avg_rating.filter(id=self.request.user.id).exists():
            rate = True

        return render(
            request,
            "board_detail.html",
            {
                "detail": detail,
                "comments": comments,
                "commented": False,
                "rate": rate,
                "review_form": ReviewForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Board_feature.objects.filter(status=1)
        detail = get_object_or_404(queryset, slug=slug)
        comments = detail.board.filter(approved=True).order_by('-created_on')
        rate = False
        if detail.avg_rating.filter(id=self.request.user.id).exists():
            rate = True
            
        review_form = ReviewForm(data=request.POST)

        if review_form.is_valid():
            review_form.instance.email = request.user.email
            review_form.instance.name = request.user.username
            review = review_form.save(commit=False)
            review.detail = detail
            review.save()
        else:
            review_form = ReviewForm()

        return render(
            request,
            "board_detail.html",
            {
                "detail": detail,
                "comments": comments,
                "commented": True,
                "rate": rate,
                "review_form": ReviewForm()
            },
        )


class BoardLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Board_feature, slug=slug)
        if post.avg_rating.filter(id=request.user.id).exists():
            post.avg_rating.remove(request.user)
        else:
            post.avg_rating.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

