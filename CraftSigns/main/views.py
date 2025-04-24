from django.shortcuts import render
from .models import Production
from .models import OurWorks
from .models import Services
from django.core.mail import EmailMessage 
import os

def index(request):
    return render(request, 'main/index.html')

def production(request):
    context_object_name = 'article'
    selected_product = request.GET.get('product', '') 
    products = ["Объёмные буквы", "Световой баннер", "Печать баннеров", "Неоновая вывеска", "Указатели и штендеры", "P.O.S. Материалы", "Фрезеровка материалов", "Ремонт баннера", "Утилизация баннера"]
    production = Production.objects.all()
    return render(request, 'main/production.html', {'Production': production,
    'selected_product': selected_product,
    'products': products
})

def services(request):
    context_object_name = 'article'
    services = Services.objects.all()
    return render(request, 'main/services.html', {'Services': services})

def contacts(request):
    selected_product = request.GET.get('product', '') 
    products = ["Объёмные буквы", "Световой баннер", "Печать баннеров", "Неоновая вывеска", "Указатели и штендеры", "P.O.S. Материалы", "Фрезеровка материалов", "Ремонт баннера", "Утилизация баннера"]
    
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        production_select = request.POST['productionSelect']

        filename = 'form_data.txt'
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f'Имя: {name}\n')
            f.write(f'Номер: {phone}\n')
            f.write(f'Email: {email}\n')
            f.write(f'Выбранный продукт: {production_select}\n')

        email_message = EmailMessage(
            'Новый заказчик хочет связаться с вами!',
            'Просмотрите данные, которые оставил заказчик в форме.',
            'your_mail@yandex.ru', 
            ['your_mail@mail.ru']
        )
        email_message.attach_file(filename)

        try:
            email_message.send()
            print("Электронная почта отправлена.")
        except Exception as e:
            print(f"Ошибка при отправке электронной почты: {e}")

        os.remove(filename)

    return render(request, 'main/contacts.html', {
    'selected_product': selected_product,
    'products': products
})

def our_works(request):
    context_object_name = 'article'
    ourworks = OurWorks.objects.all()
    return render(request, 'main/our_works.html', {'OurWorks': ourworks})
