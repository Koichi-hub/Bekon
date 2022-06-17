from django.shortcuts import render, redirect


def index(request):
    if request.user.is_authenticated:
        return redirect('account', user_id=request.user.id)
    return render(request=request, template_name='index.html')
