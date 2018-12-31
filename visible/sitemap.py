from django.contrib import sitemaps
from django.contrib.sitemaps import GenericSitemap
from django.urls import reverse

from visible.models import Post


class StaticViewSitemap(sitemaps.Sitemap):
    protocol = "https"
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'register', 'event_guide', 'blog']

    def location(self, item):
        return reverse(item)


blog_map = GenericSitemap({
    'queryset': Post.objects.all()
}, priority=0.6, protocol='https')

sitemaps = {
    'static': StaticViewSitemap,
    'blog': blog_map,
}
