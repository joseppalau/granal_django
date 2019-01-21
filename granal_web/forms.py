from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    from_email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['subject'].label = 'Asunto:'
        self.fields['from_email'].label = 'Email:'
        self.fields['message'].label = 'Mensaje:'