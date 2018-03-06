from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs = { 'class': 'form-control', 'placeholder': 'John Smith' }))
    contact_email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs = { 'class': 'form-control', 'placeholder': 'johnsmith@gmail.com'}))
    contact_subject = forms.CharField(required=False, widget=forms.TextInput(
        attrs = { 'class': 'form-control', 'placeholder': 'Loan Interest Rate Inquiry'}))
    content = forms.CharField(
            required=False,
            widget=forms.Textarea(
                attrs = { 'class': 'form-control',
                          'placeholder': 'I am interested in seeing what my current interest rate would be for a thirty year fixed rate loan and an adjustable rate loan based on my credit score.'}))

