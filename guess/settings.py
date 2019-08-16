from django.conf import settings

GUESS_SETTINGS = getattr(settings, "GUESS_SETTINGS", {})
GUESS_SETTINGS.setdefault("VIEW_ID", "")
GUESS_SETTINGS.setdefault("CREDENTIALS", getattr(settings, "BASE_DIR") + "/credentials.json")
GUESS_SETTINGS.setdefault("PREFETCH_CONFIG", {'4g': 15, '3g': 30, '2g': 45, 'slow-2g': 60})
GUESS_SETTINGS.setdefault("COMMAND_CONFIG", {'RATIO_TO_EVALUATE': 0.95, 'LOWER_LIMIT_TRANSITION_PROBABILITY': 0.05})
