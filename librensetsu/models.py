from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Literal, Optional, Union

Iso31661A2 = Literal[
    "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR",
    "AS", "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE",
    "BF", "BG", "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ",
    "BR", "BS", "BT", "BV", "BW", "BY", "BZ", "CA", "CC", "CD",
    "CF", "CG", "CH", "CI", "CK", "CL", "CM", "CN", "CO", "CR",
    "CU", "CV", "CW", "CX", "CY", "CZ", "DE", "DJ", "DK", "DM",
    "DO", "DZ", "EC", "EE", "EG", "EH", "ER", "ES", "ET", "FI",
    "FJ", "FK", "FM", "FO", "FR", "GA", "GB", "GD", "GE", "GF",
    "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ", "GR", "GS",
    "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT", "HU",
    "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT",
    "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN",
    "KP", "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK",
    "LR", "LS", "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME",
    "MF", "MG", "MH", "MK", "ML", "MM", "MN", "MO", "MP", "MQ",
    "MR", "MS", "MT", "MU", "MV", "MW", "MX", "MY", "MZ", "NA",
    "NC", "NE", "NF", "NG", "NI", "NL", "NO", "NP", "NR", "NU",
    "NZ", "OM", "PA", "PE", "PF", "PG", "PH", "PK", "PL", "PM",
    "PN", "PR", "PS", "PT", "PW", "PY", "QA", "RE", "RO", "RS",
    "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG", "SH", "SI",
    "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST", "SV",
    "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK",
    "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA",
    "UG", "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI",
    "VN", "VU", "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"
]
"""ISO 3166-1 alpha-2 approved country codes"""

Iso639S2 = Literal[
    "ab", "aa", "af", "ak", "sq", "am", "ar", "an", "hy", "as",
    "av", "ae", "ay", "az", "bm", "ba", "eu", "be", "bn", "bi",
    "bs", "br", "bg", "my", "ca", "ch", "ce", "ny", "zh", "cu",
    "cv", "kw", "co", "cr", "hr", "cs", "da", "dv", "nl", "dz",
    "en", "eo", "et", "ee", "fo", "fj", "fi", "fr", "fy", "ff",
    "gd", "gl", "lg", "ka", "de", "el", "kl", "gn", "gu", "ht",
    "ha", "he", "hz", "hi", "ho", "hu", "is", "io", "ig", "id",
    "ia", "ie", "iu", "ik", "ga", "it", "ja", "jv", "kn", "kr",
    "ks", "kk", "km", "ki", "rw", "ky", "kv", "kg", "ko", "kj",
    "ku", "lo", "la", "lv", "li", "ln", "lt", "lu", "lb", "mk",
    "mg", "ms", "ml", "mt", "gv", "mi", "mr", "mh", "mn", "na",
    "nv", "nd", "nr", "ng", "ne", "no", "nb", "nn", "ii", "oc",
    "oj", "or", "om", "os", "pi", "ps", "fa", "pl", "pt", "pa",
    "qu", "ro", "rm", "rn", "ru", "se", "sm", "sg", "sa", "sc",
    "sr", "sn", "sd", "si", "sk", "sl", "so", "st", "es", "su",
    "sw", "ss", "sv", "tl", "ty", "tg", "ta", "tt", "te", "th",
    "bo", "ti", "to", "ts", "tn", "tr", "tk", "tw", "ug", "uk",
    "ur", "uz", "ve", "vi", "vo", "wa", "cy", "wo", "xh", "yi",
    "yo", "za", "zu"
]


@dataclass
class Date:
    """Information regarding release dates"""

    year: Optional[int] = None
    """The year of the release"""
    month: Optional[int] = None
    """The month of the release"""
    day: Optional[int] = None
    """The day of the release"""
    hour: Optional[int] = None
    """The hour of the release"""
    minute: Optional[int] = None
    """The minute of the release"""
    second: Optional[int] = None
    """The second of the release"""
    timezone: Optional[str] = None
    """The timezone of the release, in format of +/-HH:MM"""

    @staticmethod
    def from_iso(iso: str) -> "Date":
        """
        Create a Date object from an ISO 8601 string.

        Format: YYYY-MM-DDTHH:MM:SSZZZZ (with ZZZZ being the timezone offset in the format of +/-HH:MM)
        :param iso: String value in ISO 8601 format
        :type iso: str
        :return: Date object
        :rtype: Date
        """
        return Date.from_datetime(datetime.fromisoformat(iso))

    @staticmethod
    def from_timestamp(timestamp: int | float | str) -> "Date":
        """
        Create an instance of Date object from a timestamp in UTC
        :param timestamp: Value of timestamp to convert from
        :type timestamp: int | float | str
        :return: Date object
        :rtype: Date
        """
        if isinstance(timestamp, str):
            timestamp = int(timestamp)
        if not isinstance(timestamp, float):
            timestamp = float(timestamp)
        return Date.from_datetime(datetime.utcfromtimestamp(timestamp))

    @staticmethod
    def from_datetime(dt: datetime) -> "Date":
        """Create a Date object from a datetime object"""
        return Date(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            timezone=dt.strftime("%z"),
        )


@dataclass
class PictureUrls:
    """Information regarding picture URLs"""

    original: Optional[str] = None
    """An original picture URL"""
    large: Optional[str] = None
    """A large picture URL"""
    medium: Optional[str] = None
    """A medium picture URL"""
    small: Optional[str] = None
    """A small picture URL"""
    tiny: Optional[str] = None
    """A tiny picture URL"""


@dataclass
class IdSlugPair:
    """Information regarding ID and slug pairs"""

    id: Optional[Union[int, str]] = None
    """The ID of the media"""
    slug: Optional[str] = None
    """The slug of the media"""


@dataclass
class ConventionalMapping(IdSlugPair):
    """Mapping information for conventional media databases"""

    media_type: Optional[Literal["tv", "movie", "shows", "movies"]] = None
    """The type of media"""
    season: Optional[int] = None
    """The season of the media, if applicable"""


@dataclass
class RelationMaps:
    """Information regarding direct relation maps"""

    allcinema: Optional[int] = None
    """AllCinema ID (Regional, JP): https://www.allcinema.net"""
    anibrain: Optional[int] = None
    """AniBrain ID: https://anibrain.ai"""
    anidb: Optional[int] = None
    """aniDB ID: https://anidb.net"""
    anilist: Optional[int] = None
    """AniList ID: https://anilist.co"""
    animenewsnetwork: Optional[int] = None
    """Anime News Network ID: https://www.animenewsnetwork.com"""
    animeplanet: Optional[str] = None
    """Anime-Planet slug: https://www.anime-planet.com"""
    animethemes: Optional[IdSlugPair] = None
    """AnimeThemes ID: https://animethemes.moe"""
    anisearch: Optional[int] = None
    """AniSearch ID (Regional, DE ES FR JP IT): https://www.anisearch.com"""
    anison: Optional[int] = None
    """Anison ID (Regional, JP): https://www.anison.info"""
    annict: Optional[int] = None
    """Annict ID (Regional, JP): https://annict.com"""
    aozora: Optional[str] = None
    """Discontinued Aozora ID, acquired by Kitsu for its mobile app"""
    bangumi: Optional[int] = None
    """Bangumi (bgm.tv) ID (Regional, CN): https://bgm.tv"""
    douban: Optional[int] = None
    """Douban ID (Regional, CN): https://movie.douban.com"""
    doujinshi: Optional[IdSlugPair] = None
    """Doujinshi.info Unique ID: https://doujinshi.info"""
    imdb: Optional[ConventionalMapping] = None
    """IMDb ID: https://www.imdb.com"""
    kaize: Optional[IdSlugPair] = None
    """Kaize ID: https://kaize.io"""
    kitsu: Optional[IdSlugPair] = None
    """Kitsu ID: https://kitsu.io"""
    kinopoisk: Optional[int] = None
    """Kinopoisk ID (Regional, RU): https://kinopoisk.ru"""
    kurozora: Optional[int] = None
    """Kurozora ID, successor to Aozora: https://kurozora.app"""
    lain: Optional[int] = None
    """Lain ID (Regional, JP): https://lain.gr.jp"""
    livechart: Optional[int] = None
    """LiveChart ID: https://www.livechart.me"""
    letterboxd: Optional[str] = None
    """Letterboxd slug: https://letterboxd.com"""
    mangadex: Optional[str] = None
    """MangaDex UUID: https://mangadex.org"""
    mangaupdates: Optional[int] = None
    """MangaUpdates ID: https://www.mangaupdates.com"""
    myanimelist: Optional[int] = None
    """MyAnimeList ID: https://myanimelist.net"""
    nautiljon: Optional[IdSlugPair] = None
    """Nautiljon ID (Regional, FR): https://www.nautiljon.com"""
    notify: Optional[str] = None
    """Notify.moe Base64 ID: https://notify.moe"""
    novelupdates: Optional[str] = None
    """NovelUpdates slug: https://www.novelupdates.com"""
    otakotaku: Optional[IdSlugPair] = None
    """Otak Otaku ID (Regional, ID): https://otakotaku.com"""
    rottentomatoes: Optional[str] = None
    """Rotten Tomatoes slug: https://www.rottentomatoes.com"""
    silveryasha: Optional[int] = None
    """Silver-Yasha DB Tontonan Indonesia (Regional, ID): https://db.silveryasha.web.id"""
    shikimori: Optional[IdSlugPair] = None
    """
    Shikimori ID, mirrors MyAnimeList (Regional, RU): https://shikimori.one

    Slug most of the time is equal to ID, however, some title may have additiona
    alphabet as the prefix (eg. `z28977`). Use slug to redirect user without
    HTTP 301, eg: https://shikimori.one/animes/z28977
    """
    syoboical: Optional[int] = None
    """Syoboi Calender ID (Regional, JP): https://cal.syoboi.jp"""
    tmdb: Optional[ConventionalMapping] = None
    """The Movie Database ID: https://www.themoviedb.org"""
    tvdb: Optional[ConventionalMapping] = None
    """The TVDB ID: https://www.thetvdb.com"""
    trakt: Optional[ConventionalMapping] = None
    """Trakt ID: https://trakt.tv"""
    vndb: Optional[int] = None
    """VNDB ID: https://vndb.org"""
    wikidata: Optional[str] = None
    """Wikidata ID: https://www.wikidata.org"""
    worldart: Optional[int] = None
    """World Art ID (Regional, RU): http://www.world-art.ru"""
    others: Optional[Dict[str, Union[int, str]]] = None
    """Other IDs"""


@dataclass
class MediaInfo:
    """Information regarding media"""

    uuid: str
    """The UUID of the media, used to correlate with the provider"""
    title_display: str
    """The title of the media to be displayed, in order: transliterated, English, native"""
    title_native: Optional[str]
    """The title of the media in its native language"""
    title_transliteration: Optional[str]
    """The title of the media transliterated into the Latin alphabet"""
    title_english: Optional[str]
    """The title of the media in English"""
    synonyms: Optional[List[str]]
    """Synonyms of the media"""
    is_adult: Optional[bool]
    """Whether the media is adult content, `None` if service does not provide this information"""
    media_type: Literal[
        "anime", "manga", "lightnovel", "shows", "movies", "books", "other"
    ]
    """The type of media"""
    media_sub_type: Optional[str]
    """The sub-type of media, if applicable"""
    year: Optional[int]
    """The year of the release"""
    start_date: Optional[Date]
    """The release date of the media"""
    end_date: Optional[Date]
    """The end date of the media"""
    unit_order: Optional[int]
    """Order of the unit of following entry. On TV shows this is the episode number, if applicable"""
    unit_counts: Optional[int]
    """The number of units (episodes, chapters) in the media"""
    subunit_order: Optional[int]
    """Order of the subunit of following entry. On video media this is the minute per episode, if applicable"""
    subunit_counts: Optional[int]
    """The number of subunits (minutes, pages) in the media, in total"""
    volume_order: Optional[int]
    """Order of the volume of following entry. On TV shows this is the season number, if applicable"""
    volume_counts: Optional[int]
    """The number of volumes in the media. On TV shows this is the number of seasons, if applicable"""
    season: Optional[Literal["winter", "spring", "summer", "fall"]]
    """The season of the release, if applicable"""
    picture_urls: List[PictureUrls]
    """List of picture URLs from the provider"""
    country_of_origin: Optional[Iso31661A2]
    """The country of origin of the media"""
    mappings: RelationMaps
    """Direct relation maps"""
    source_data: Literal[
        "allcinema",
        "anibrain",
        "anidb",
        "anilist",
        "animenewsnetwork",
        "animeplanet",
        "animethemes",
        "anisearch",
        "anison",
        "annict",
        "bangumi",
        "douban",
        "doujinshi",
        "imdb",
        "kaize",
        "kinopoisk",
        "kitsu",
        "kurozora",
        "letterboxd",
        "livechart",
        "mangadex",
        "mangaupdates",
        "myanimelist",
        "nautiljon",
        "notify",
        "novelupdates",
        "otakotaku",
        "rottentomatoes",
        "silveryasha",
        "shikimori",
        "syoboical",
        "tmdb",
        "tvdb",
        "trakt",
        "vndb",
        "wikidata",
        "worldart",
        "others",
        "rensetsu",
    ] = "rensetsu"
    """The source of the data"""
