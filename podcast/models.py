from django.db import models
from wagtail.core.models import Page, Orderable

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtailmetadata.models import MetadataPageMixin

from babel.dates import format_date

# Create your models here.


class PodcastIndexPage(MetadataPageMixin, Page):
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('icon'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        podcasts = self.get_children().live().order_by('-first_published_at')

        context['podcasts'] = podcasts

        return context

    def get_template(self, request):
        if request.is_ajax():
            # Template to render objects retrieved via Ajax
            return 'podcast/podcasts_grid_paginate.html'
        else:
            # Original template
            return 'podcast/podcast_index_page.html'


class PodcastPage(Page):
    podcast_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    date = models.DateField("Podcast date", default=models.fields.datetime.date.today)
    media_url = models.CharField(max_length=250)
    description_tag = models.CharField(max_length=250, default='')

    content_panels = Page.content_panels + [
        ImageChooserPanel('podcast_image'),
        FieldPanel('date'),
        FieldPanel('media_url'),
        FieldPanel('description_tag'),
    ]

    # search_fields = Page.search_fields + [
    #     index.SearchField('intro'),
    #     index.SearchField('body'),
    #     index.SearchField('author'),
    #     index.SearchField('tags'),
    # ]

    # def get_context(self, request):
    #     # Update context to include only published posts, ordered by reverse-chron
    #     context = super().get_context(request)
    #     blogpages = BlogPage.objects.live().order_by('-first_published_at')[:3]
    #     context['blogpages'] = blogpages

    def greek_date(self):
        return format_date(self.date, locale='el_GR')

    def get_meta_image(self):
        """A relevant Wagtail Image to show. Optional."""

        if self.podcast_image:
            return self.podcast_image
        else:
            return None

    def get_meta_description(self):
        """
        A short text description of this object.
        This should be plain text, not HTML.
        """
        return self.title


