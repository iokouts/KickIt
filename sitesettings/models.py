from django.db import models
from wagtail.contrib.settings.models import BaseSetting, register_setting


@register_setting
class SocialMediaSettings(BaseSetting):
	twitter = models.CharField(max_length=255, help_text="Twitter username without @", blank=True)

	mailchimp_list_id = models.CharField(max_length=255, help_text="Maichimp List ID", blank=True)
	mailchimp_api_key = models.CharField(max_length=255, help_text="Maichimp API Key", blank=True)
