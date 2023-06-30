from django import forms
from . import models, parsing


class ParserForm(forms.Form):
    MEDIA_CHOICES = (("manas.kg", "manas.kg"),)
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            "media_type",
        ]

    def parser_data(self):
        if self.data["media_type"] == "manas.kg":
            film_parser = parsing.parser()
            for i in film_parser:
                models.ManasKg.objects.create(**i)