"""forms for library app."""

from django import forms

from.models import RackModel, BookModel


class RackAdminForm(forms.ModelForm):
    """Custom form for admin panel."""

    class Meta:
        """Meta rack object for the form."""

        model = RackModel
        fields = ['name']


class BookAdminForm(forms.ModelForm):
    """Custom book form for admin panel."""

    class Meta:
        """Meta object for the form."""

        model = BookModel
        
        fields = ['title', 'author', 'published', 'rack']

    def clean(self):
        """Clean data."""
        rack = self.cleaned_data.get("rack")

        # TODO: obtaining books_count need improvement.
        books_count = self.Meta.model.objects.same_rack_count(rack=rack)

        if books_count < rack.can_hold:
            return self.cleaned_data
        else:
            raise forms.ValidationError({'rack': ["Rack can't hold any more books!",]})
