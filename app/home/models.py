from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

from .blocks import TwoColumnBlock, ThreeColumnBlock


class HomePage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(
            label='Paragraphe', features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr']
        )),
        ('image', ImageChooserBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
    ], verbose_name='Contenu', null=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]
    
    max_count = 1

    class Meta:
        verbose_name = "page d'accueil"


class ClassicPage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(
            label='Paragraphe', features=['h1', 'h2', 'h3', 'bold', 'italic', 'link', 'hr']
        )),
        ('image', ImageChooserBlock()),
        ('two_columns', TwoColumnBlock()),
        ('three_columns', ThreeColumnBlock()),
    ], verbose_name='Contenu')

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = "Page classique"
