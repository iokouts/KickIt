from django.db import models
from wagtail.core.models import Page
from wagtailmetadata.models import MetadataPageMixin
from wagtail.admin.edit_handlers import FieldPanel

# Create your models here.
class RadioPage(MetadataPageMixin,Page):
    radio_embed_url = models.CharField(max_length=250, default='')
    chat_embed_url = models.CharField(max_length=250, default='')
    radio_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    def get_meta_image(self):
        """A relevant Wagtail Image to show. Optional."""
        if self.radio_image:
            return self.radio_image
        else:
            return None

    content_panels = Page.content_panels + [
        FieldPanel('radio_embed_url'),
        FieldPanel('chat_embed_url'),
        FieldPanel('radio_image'),
    ]