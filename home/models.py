from .blocks import *

from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock

class HomePage(Page):
    sectionOneA = StreamField([
        ('paragraph', blocks.RichTextBlock('texter')),
        ('image', ImageChooserBlock('imager')),
    ],null=True,blank=True)
    sectionOneB = StreamField([
        ('paragraph', blocks.RichTextBlock('texter')),
        ('image', ImageChooserBlock('imager')),
    ],null=True,blank=True)
    sectionOneC = StreamField([
        ('paragraph', blocks.RichTextBlock('texter')),
        ('image', ImageChooserBlock('imager')),
    ],null=True,blank=True)

    sectionTwoA = StreamField([
        ('paragraph', blocks.RichTextBlock('texter2')),
        ('image', ImageChooserBlock('imager2')),
    ],null=True,blank=True)
    sectionTwoB = StreamField([
        ('paragraph', blocks.RichTextBlock('texter2')),
        ('image', ImageChooserBlock('imager2')),
    ],null=True,blank=True)
    sectionTwoC = StreamField([
        ('paragraph', blocks.RichTextBlock('texter2')),
        ('image', ImageChooserBlock('imager2')),
    ],null=True,blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('sectionOneA'),
        StreamFieldPanel('sectionOneB'),
        StreamFieldPanel('sectionOneC'),
        StreamFieldPanel('sectionTwoA'),
        StreamFieldPanel('sectionTwoB'),
        StreamFieldPanel('sectionTwoC'),
    ]


class ContactPage(Page):
    section = StreamField([
        ('heading', blocks.CharBlock(classname="full title",icon="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock(icon="image")),
        ('two_columns', TwoColumnBlock()),
        ('embedded_video', EmbedBlock(icon="media")),
    ],null=True,blank=True)

    content_panels = Page.content_panels + [ StreamFieldPanel('section') ]
