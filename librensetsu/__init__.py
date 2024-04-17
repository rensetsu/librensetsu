from .const import (
    GITHUB_EVENT_NAME,
    GITHUB_WORKSPACE,
    IS_GITHUB_WORKFLOW,
    IS_GITHUB_WORKFLOW_DISPATCH,
)
from .download_unidic import download_unidic
from .grammar import pluralize
from .humanclock import convert_float_to_time, translate_season, Season
from .models import (
    ConventionalMapping,
    Date,
    IdSlugPair,
    MediaInfo,
    PictureUrls,
    RelationMaps,
)
from .prettyprint import Platform, PrettyPrint, Status, translate_hex_to_rgb
from .slugify import slugify
from .transliterate import char_maps, transliterate_no_accent

__version__ = "0.2.0"

__all__ = [
    "char_maps",
    "ConventionalMapping",
    "convert_float_to_time",
    "Date",
    "download_unidic",
    "GITHUB_EVENT_NAME",
    "GITHUB_WORKSPACE",
    "IdSlugPair",
    "IS_GITHUB_WORKFLOW_DISPATCH",
    "IS_GITHUB_WORKFLOW",
    "MediaInfo",
    "PictureUrls",
    "Platform",
    "pluralize",
    "PrettyPrint",
    "RelationMaps",
    "Season",
    "slugify",
    "Status",
    "translate_hex_to_rgb",
    "translate_season",
    "transliterate_no_accent",
]
