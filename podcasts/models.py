from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.search import index

from wagtailmetadata.models import MetadataPageMixin

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag as TaggitTag

from babel.dates import format_date


class PodcastsIndexPage(Page):
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('icon'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        podcasts = self.get_children().order_by('-first_published_at')

        context['podcasts'] = podcasts

        return context

    # def get_template(self, request):
    #     if request.is_ajax():
    #         # Template to render objects retrieved via Ajax
    #         return 'blog/posts_grid_paginate.html'
    #     else:
    #         # Original template
    #         return 'blog/blog_index_page.html'


class PodcastsPage(Page):
    podcast_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    date = models.DateField("Podcast date", default=models.fields.datetime.date.today)
    media_url = models.CharField(max_length=250)

    content_panels = Page.content_panels + [
        ImageChooserPanel('podcast_image'),
        FieldPanel('date'),
        FieldPanel('media_url'),
    ]

    # def get_context(self, request):
    #     # Update context to include only published posts, ordered by reverse-chron
    #     context = super().get_context(request)
    #     blogpages = BlogPage.objects.live().order_by('-first_published_at')[:3]
    #     context['blogpages'] = blogpages


