from __future__ import unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import RichTextFieldPanel


class HomePage(Page):
    body = RichTextField(blank=True, default='')

HomePage.content_panels = Page.content_panels + [
    RichTextFieldPanel('body')
]