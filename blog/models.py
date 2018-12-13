from django.db import models
from django import forms

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.search import index

from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel
from wagtailmetadata.models import MetadataPageMixin

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag as TaggitTag

from babel.dates import format_date

# Create your models here.


class BlogTagIndexPage(Page):
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        posts = BlogPage.objects.live().filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['posts'] = posts
        return context

    def get_template(self, request):
        if request.is_ajax():
            # Template to render objects retrieved via Ajax
            return 'blog/posts_grid_paginate.html'
        else:
            # Original template
            return 'blog/blog_tag_index_page.html'

    def get_meta_image(self):
        pass


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='post_tags', on_delete=models.CASCADE)


class BlogIndexPage(MetadataPageMixin, Page):
    intro = RichTextField(blank=True)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    main_color = models.CharField(max_length=7, default='#000')
    mobile_banner = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        ImageChooserPanel('icon'),
        ImageChooserPanel('mobile_banner'),
        FieldPanel('main_color'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = self.get_children().order_by('-first_published_at')

        context['blog_featured'] = blogpages[:3]
        # context['page_template'] = 'home/article_thumbnail.html'
        context['posts'] = blogpages[3:]

        return context

    def get_template(self, request):
        if request.is_ajax():
            # Template to render objects retrieved via Ajax
            return 'blog/posts_grid_paginate.html'
        else:
            # Original template
            return 'blog/blog_index_page.html'


class BlogPage(MetadataPageMixin, Page):
    date = models.DateField("Post date", default=models.fields.datetime.date.today)
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    show_in_homepage_slider = models.BooleanField(
        verbose_name='show in homepage slider',
        default=False
    )
    author = models.ForeignKey(
         'blog.AuthorPage', null=True, blank=True,
         on_delete=models.SET_NULL, related_name='+'
     )
    video = models.ForeignKey(
        'wagtail_embed_videos.EmbedVideo',
        verbose_name="Video",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = BlogPage.objects.live().order_by('-first_published_at')[:3]
        context['blogpages'] = blogpages

        return context

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def greek_date(self):
        return format_date(self.date, locale='el_GR')

    def get_meta_image(self):
        """A relevant Wagtail Image to show. Optional."""
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    def get_meta_description(self):
        """
        A short text description of this object.
        This should be plain text, not HTML.
        """
        return self.intro

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
        index.SearchField('author'),
        index.SearchField('tags'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('show_in_homepage_slider'),
            PageChooserPanel('author'),
        ], heading="Post information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        EmbedVideoChooserPanel('video'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class AuthorPage(MetadataPageMixin, Page):
    name = models.CharField("Name", max_length=254)
    description = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('name'),
        FieldPanel('description'),
        ImageChooserPanel('image'),
        FieldPanel('body')
    ]

    search_fields = [
        index.SearchField('name'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        author_posts = BlogPage.objects.live().filter(author=self)

        context['posts'] = author_posts

        return context

    def thumb_image(self):
        # Returns an empty string if there is no profile pic or the rendition
        # file can't be found.
        try:
            return self.image.get_rendition('fill-50x50').img_tag()
        except:
            return ''

    def get_template(self, request):
        if request.is_ajax():
            # Template to render objects retrieved via Ajax
            return 'blog/posts_grid_paginate.html'
        else:
            # Original template
            return 'blog/author_page.html'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class AuthorIndexPage(MetadataPageMixin, Page):

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        author_pages = self.get_children().order_by('-first_published_at')

        context['authors'] = author_pages

        return context


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
