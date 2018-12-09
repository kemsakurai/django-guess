from django.conf import settings

GUESS_SETTINGS = getattr(settings, "GUESS_SETTINGS", {})
GUESS_SETTINGS.setdefault("VIEW_ID", "")
GUESS_SETTINGS.setdefalut("CREDENTIALS", getattr(settings, "BASE_DIR") + "/credentials.json")
