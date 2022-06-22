from django.shortcuts import render, redirect


def chat(request):
    if request.user.is_authenticated:
        return render(request, 'chat/index.html', {'user': request.user})
    return redirect('home')
