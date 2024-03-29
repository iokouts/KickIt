from django.db import models
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSiteSetting):
    instagram_account = models.CharField(max_length=255, help_text="Full Instagram account url", blank=True,
                                       verbose_name="Instagram Account")
    facebook_page = models.CharField(max_length=255, help_text="Full Facebook Page url", blank=True,
                                       verbose_name="Facebook Page")
    twitter_account = models.CharField(max_length=255, help_text="Full Twitter account url", blank=True,
                                       verbose_name="Twitter Account")
    fb_app_id = models.CharField(max_length=255, help_text="Facebook App ID", blank=True, default="",
                                 verbose_name="Facebook App ID")

@register_setting
class GeneralConfigurations(BaseSiteSetting):
    cookies_conscent_text = models.CharField(max_length=500, help_text="Cookie popup text", blank=False,
                                        default="This website uses cookies to make your experience better.",
                                        verbose_name="Cookie Conscent Text")
