from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (FieldPanel, MultiFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel

from blog.models import BlogPage


class HomePage(Page):
    body = RichTextField(blank=True)
    parallax_text = models.CharField(max_length=250, default='DEFAULT PARALLAX')
    parallax_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('parallax_text'),
            ImageChooserPanel('parallax_image'),
        ], heading="Parallax"),
        FieldPanel('body', classname="full"),
    ]

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        featured_posts = BlogPage.objects.live().order_by('-first_published_at')[:2]
        context['featured_posts'] = featured_posts

        return context

