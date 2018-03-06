from django.shortcuts import render
from .forms import ContactForm

def index(request):
    return render(request, 'index.html')

def glossary(request):
    return render(request, 'glossary.html')

def contact(request):
    form_class = ContactForm
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_business_name = request.POST.get('contact_business_name', '')
            contact_email = request.POST.get('contact_email', '')
            contact_telephone = request.POST.get('contact_telephone', '')
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_business_name': contact_business_name,
                'contact_email': contact_email,
                'contact_telephone': contact_telephone,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['scottabrown89@gmail.com'],
                headers = {'Reply-To': contact_email }
            )

            email.send()
            return redirect('index')
    return render(request, 'contact.html', {'form': form_class,})

