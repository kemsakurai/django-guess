from django.conf import settings

GUESS_SETTINGS = getattr(settings, "GUESS_SETTINGS", {})
GUESS_SETTINGS.setdefault("VIEW_ID", "")
GUESS_SETTINGS.setdefault("CREDENTIALS", getattr(settings, "BASE_DIR") + "/credentials.json")
GUESS_SETTINGS.setdefault("PREFETCH_CONFIG", {'4g': 0.15, '3g': 0.3, '2g': 0.45, 'slow-2g': 0.6})
GUESS_SETTINGS.setdefault("COMMAND_CONFIG", {'RATIO_TO_EVALUATE': 0.95, 'LOWER_LIMIT_TRANSITION_PROBABILITY': 0.05})
