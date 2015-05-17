from django.contrib.gis.db import models
from django.utils.text import slugify


__all__ = [
    'Location',
    'LocatedFile'
]


class BaseModel(models.Model):
    name = models.CharField(max_length=32)
    slug = models.SlugField(max_length=128, unique=True, blank=True)
    geometry = models.GeometryField()
    objects = models.GeoManager()

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def _generate_slug(self):
        if self.slug == '' or self.slug is None:
            try:
                name = unicode(self.name)
            except NameError:
                name = self.name
            self.slug = slugify(name)

    def clean(self):
        self._generate_slug()

    def save(self, *args, **kwargs):
        self._generate_slug()
        super(BaseModel, self).save(*args, **kwargs)


class Location(BaseModel):
    pass


class LocatedFile(BaseModel):
    file = models.FileField(upload_to='located_files', blank=True, null=True)
