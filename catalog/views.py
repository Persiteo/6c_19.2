from django.shortcuts import render



def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('Textarea1')
        email = request.POST.get('Email1')
        message = request.POST.get('Textarea2')
        with open('log.txt', 'a') as f:
            f.writelines(f'{name} желает записаться на: {message} (Для связи: {email})\n')
    return render(request, 'catalog/contacts.html')


def howtogo(request):
    return render(request, 'catalog/howtogo.html')
