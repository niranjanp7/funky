from django.db import models


class Game(models.Model):
    game_name = models.CharField(max_length=100)
    game_description = models.TextField(max_length=500, null=True)  # Game Description
    html_file = models.CharField(max_length=100, null=True)  # HTML File path in templates
    css_file = models.CharField(max_length=100, null=True)  # CSS File path in templates
    js_file = models.CharField(max_length=100, null=True)  # JS File path in templates

    def __str__(self) -> str:
        return self.game_name
