from django.shortcuts import render


def index(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
    #     print(f'You have new message from {name}({email}): {message}')
    return render(request, 'catalog/index.html')


def contacts(request):
    # if request.method == 'POST':
    #     name = request.POST.get('name')
    #     email = request.POST.get('email')
    #     message = request.POST.get('message')
    #     print(f'You another one new message from {name}({email}): {message}')
    return render(request, 'catalog/contacts.html')


def howtogo(request):
    return render(request, 'catalog/howtogo.html')
