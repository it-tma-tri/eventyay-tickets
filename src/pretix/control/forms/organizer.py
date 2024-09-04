from django import forms

from pretix.base.models import Organizer
from pretix.base.models.organizer import OrganizerFooterLinkModel
from pretix.control.forms.organizer_forms import (
    BaseOrganizerFooterLinkFormSet, OrganizerFooterLinkForm,
)

OrganizerFooterLinkFormset = forms.inlineformset_factory(
    Organizer, OrganizerFooterLinkModel,
    OrganizerFooterLinkForm,
    formset=BaseOrganizerFooterLinkFormSet,
    can_order=False, can_delete=True, extra=0
)
