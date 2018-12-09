from django import template
register = template.Library()
from guess.models import GuessResult

@register.inclusion_tag("includes/link_rel.html")
def prefetch(url):
    results = GuessResult.objects.filter(previous_page_path=url)
    return {"guess_result": results}
