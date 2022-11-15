from django.forms import ModelForm

from shortner.models import ShortUrl


class CreateUrlForm(ModelForm):
    class Meta:
        model = ShortUrl
        fields = ['link']


    def __init__(self, *args, **kwargs):
        super(CreateUrlForm, self).__init__(*args, **kwargs)

        for k, field in self.fields.items():
            field.widget.attrs.update(
                {'class': 'input', 'placeHolder': "Enter the Long url"})

    # fields['link'].a