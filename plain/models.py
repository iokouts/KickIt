from django.db import models
from wagtail.core.models import Page
from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

# Create your models here.
class RadioPage(MetadataPageMixin,Page):
    radio_embed_url = models.CharField(max_length=250, default='')
    chat_embed_url = models.CharField(max_length=250, default='')
    radio_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('radio_embed_url'),
        FieldPanel('chat_embed_url'),
        ImageChooserPanel('radio_image'),
    ]