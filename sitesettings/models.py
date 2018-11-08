from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
	twitter = models.CharField(max_length=255, help_text="Twitter username without @", blank=True)
