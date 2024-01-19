from django.shortcuts import render,redirect
from .forms import ContactForm
from django.urls import reverse
# Create your views here.
def contact(request):
    contact_form = ContactForm(request.POST or None)
    if contact_form.is_valid():
        name = contact_form.cleaned_data['name']
        email = contact_form.cleaned_data['email']
        content = contact_form.cleaned_data['content']
        # Process the form data here
        return redirect(reverse('contact')+'?ok')

    return render(request, "contact/contact.html", {'form': contact_form})