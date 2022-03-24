from django.forms import ModelForm, CharField, ChoiceField, RadioSelect
from .models import Post

class PostForm(ModelForm):

    slug = CharField(
        label='Slug',
        help_text='É a parte da URL que identifica uma página ex. "webpage.com.br/slug"',
    )
    status = ChoiceField(
        label='Status',
        widget=RadioSelect(),
        choices=[
            ['0', 'Rascunho'],
            ['1', 'Publicado'],
        ],
    )

    class Meta:
        model = Post
        fields = ['author', 'title','text','status','slug']