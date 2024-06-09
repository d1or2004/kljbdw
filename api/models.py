from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(null=True)
    # listened = models.PositiveSmallIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=["id"])
        ]
    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)
    cover = models.URLField(null=True)
    # listened = models.PositiveSmallIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=["id"])
        ]

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    cover = models.URLField(null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    listened = models.PositiveSmallIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        indexes = [
            models.Index(fields=["id"])
        ]

    def __str__(self):
        return f"{self.title} - {self.album}"
