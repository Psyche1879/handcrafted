from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Figure
from .forms import ReviewForm
from django.db.models import Q
from django_filters import FilterSet


class FigureFilter(FilterSet):
    class Meta:
        model = Figure
        fields = {
            'name': ['icontains'],
            'category': ['exact'],

        }

def figure_list(request):
    figures = Figure.objects.all()
    figure_filter = FigureFilter(request.GET, queryset=figures)
    context = {
        'figures': figure_filter.qs,
        'filter': figure_filter,
    }
    return render(request, 'store/figure_list.html', context)

def figure_detail(request, slug):
    figure = get_object_or_404(Figure, slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.figure = figure
            review.user = request.user
            review.save()
            return redirect('figure_detail', slug=slug)
    else:
        form = ReviewForm()
    recommendations = Figure.objects.filter(category=figure.category).exclude(slug=slug).order_by('?')[:3]

    context = {
        'figure': figure,
        'form': form,
        'recommendations': recommendations,
    }
    return render(request, 'store/figure_detail.html', context)