from django.db import models
from wagtail.core.models import Page, Orderable

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtailmetadata.models import MetadataPageMixin

from babel.dates import format_date

# Create your models here.


class EventIndexPage(MetadataPageMixin, Page):
    main_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('main_image'),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context['events'] = EventPage.objects.live().order_by('date')

        return context


class EventPage(MetadataPageMixin, Page):
    event_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    date = models.DateField("Event date", default=models.fields.datetime.date.today)
    event_link = models.CharField(max_length=250, blank=True)
    venue = models.CharField(max_length=250)
    venue_map_link = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        ImageChooserPanel('event_image'),
        FieldPanel('date'),
        FieldPanel('event_link'),
        FieldPanel('venue'),
        FieldPanel('venue_map_link'),
        FieldPanel('description'),
    ]

    def greek_date(self):
        return format_date(self.date, locale='el_GR')

    def get_meta_image(self):
        """A relevant Wagtail Image to show. Optional."""

        if self.event_image:
            return self.event_image
        else:
            return None

    def get_meta_description(self):
        """
        A short text description of this object.
        This should be plain text, not HTML.
        """
        return self.title
