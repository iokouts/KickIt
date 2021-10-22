from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField

from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.search import index

from wagtail.embeds.embeds import get_embed
from wagtail.embeds.exceptions import EmbedException
from wagtailmetadata.models import MetadataPageMixin

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase, Tag as TaggitTag

from babel.dates import format_date
from unidecode import unidecode
# Create your models here.


class BlogTagIndexPage(Page):
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('icon'),
    ]

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
        blogpages = self.get_children().live().order_by('-first_published_at')

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
    video_url = models.CharField(max_length=250, default='', blank=True)
    post_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )
    author = models.ForeignKey(
         'blog.AuthorPage', null=True, blank=True,
         on_delete=models.SET_NULL, related_name='+'
     )

    # override full_clean to get nice slug urls, without greek characters
    def full_clean(self, *args, **kwargs):
        # first call the built-in cleanups (including default slug generation)
        super(BlogPage, self).full_clean(*args, **kwargs)

        # convert greek characters to english
        if self.slug:
            self.slug = unidecode(self.slug)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)

        blogpages = None
        # find the posts with the most common tags
        tag_ids = self.tags.values_list('id', flat=True)
        if tag_ids:
            query = f"""select b.page_ptr_id, p.title, count(bt.tag_id) as tag_count from blog_blogpage b 
join wagtailcore_page p on b.page_ptr_id = p.id 
join blog_blogpagetag bt on bt.content_object_id = b.page_ptr_id 
join taggit_tag t on t.id = bt.tag_id 
where tag_id in ({','.join(list(map(str,tag_ids)))})
and b.page_ptr_id != {self.page_ptr_id}
group by (page_ptr_id, p.id) 
order by tag_count desc, p.first_published_at desc
limit 3"""
            blogpages = BlogPage.objects.raw(query)
        
        if blogpages is None:
            blogpages = BlogPage.objects.live().exclude(pk=self.id).order_by('-first_published_at')[:3]

        context['blogpages'] = blogpages

        return context

    def get_embed_video(self):
        try:
            if self.video_url.strip():
                embed = get_embed(self.video_url)
                return embed.url
        except EmbedException:
            return self.video_url+'Something went wrong while embeding the video! Invalid or not existing video URL!'

    def greek_date(self):
        return format_date(self.date, locale='el_GR')

    def get_meta_url(self):
        """The URL of this object, including protocol and domain"""
        return self.get_full_url()

    def get_meta_image(self):
        """A relevant Wagtail Image to show. Optional."""
        # gallery_item = self.gallery_images.first()
        if self.post_image:
            return self.post_image
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
        ImageChooserPanel('post_image'),
        FieldPanel('intro'),
        FieldPanel('body'),
        FieldPanel('video_url'),
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
