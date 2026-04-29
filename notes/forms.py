from django import forms 
from .models import Notes, Tag

class NotesForm(forms.ModelForm):
    tags_input = forms.CharField(
        required=False,
        help_text='Separate tags with commas, for example: work, ideas, urgent',
    )

    class Meta:
        model = Notes
        fields = ('title', 'text')

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)
        if instance and instance.pk:
            self.fields['tags_input'].initial = ', '.join(
                instance.tags.values_list('name', flat=True)
            )

    def save(self, commit=True):
        note = super().save(commit=commit)
        tags = self.cleaned_data.get('tags_input', '')
        tag_names = [tag.strip() for tag in tags.split(',') if tag.strip()]
        resolved_tags = [Tag.objects.get_or_create(name=name)[0] for name in tag_names]
        if commit:
            note.tags.set(resolved_tags)
        else:
            self._resolved_tags = resolved_tags
        return note

    def save_tags(self, note):
        note.tags.set(getattr(self, '_resolved_tags', []))

    # def clean_title(self):
    #     title = self.cleaned_data
    #     if 'Django' not in title:
    #         raise forms.ValidationError('We only accepts notes about Django')
    #     return title
    
