from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.http import JsonResponse

def sendmessage(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        message = request.POST.get('message')

        # Составляем тело сообщения
        email_subject = f"Новое сообщение от {name}"
        email_message = (
            f"🔔 *Новое сообщение с сайта antiprovokator*\n\n"
            f"📌 **Детали сообщения:**\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"👤 **Имя:** {name}\n"
            f"✉️ **Почта:** {email}\n"
            f"📞 **Телефон:** {phone}\n"
            f"📅 **Дата:** {date}\n"
            f"⏰ **Время:** {time}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"📝 **Сообщение:**\n"
            f"{message}\n"
            f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📍 *Отправлено через контактную форму.*"
        )

     
        send_mail(
            email_subject,                # Тема письма
            email_message,                # Тело письма
            'antiprovokator',             # Отправитель
            ['antiprovokator.kz@gmail.com'], # Получатель
            fail_silently=False,
        )
        return redirect('main:index')
