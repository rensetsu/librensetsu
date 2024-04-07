from dataclasses import dataclass
from typing import Optional, Union, Literal, List, Dict
from datetime import datetime

Iso31661A2 = Literal[
    "AD", "AE", "AF", "AG", "AI", "AL", "AM", "AO", "AQ", "AR", "AS",
    "AT", "AU", "AW", "AX", "AZ", "BA", "BB", "BD", "BE", "BF", "BG",
    "BH", "BI", "BJ", "BL", "BM", "BN", "BO", "BQ", "BR", "BS", "BT",
    "BV", "BW", "BY", "BZ", "CA", "CC", "CD", "CF", "CG", "CH", "CI",
    "CK", "CL", "CM", "CN", "CO", "CR", "CU", "CV", "CW", "CX", "CY",
    "CZ", "DE", "DJ", "DK", "DM", "DO", "DZ", "EC", "EE", "EG", "EH",
    "ER", "ES", "ET", "FI", "FJ", "FK", "FM", "FO", "FR", "GA", "GB",
    "GD", "GE", "GF", "GG", "GH", "GI", "GL", "GM", "GN", "GP", "GQ",
    "GR", "GS", "GT", "GU", "GW", "GY", "HK", "HM", "HN", "HR", "HT",
    "HU", "ID", "IE", "IL", "IM", "IN", "IO", "IQ", "IR", "IS", "IT",
    "JE", "JM", "JO", "JP", "KE", "KG", "KH", "KI", "KM", "KN", "KP",
    "KR", "KW", "KY", "KZ", "LA", "LB", "LC", "LI", "LK", "LR", "LS",
    "LT", "LU", "LV", "LY", "MA", "MC", "MD", "ME", "MF", "MG", "MH",
    "MK", "ML", "MM", "MN", "MO", "MP", "MQ", "MR", "MS", "MT", "MU",
    "MV", "MW", "MX", "MY", "MZ", "NA", "NC", "NE", "NF", "NG", "NI",
    "NL", "NO", "NP", "NR", "NU", "NZ", "OM", "PA", "PE", "PF", "PG",
    "PH", "PK", "PL", "PM", "PN", "PR", "PS", "PT", "PW", "PY", "QA",
    "RE", "RO", "RS", "RU", "RW", "SA", "SB", "SC", "SD", "SE", "SG",
    "SH", "SI", "SJ", "SK", "SL", "SM", "SN", "SO", "SR", "SS", "ST",
    "SV", "SX", "SY", "SZ", "TC", "TD", "TF", "TG", "TH", "TJ", "TK",
    "TL", "TM", "TN", "TO", "TR", "TT", "TV", "TW", "TZ", "UA", "UG",
    "UM", "US", "UY", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU",
    "WF", "WS", "YE", "YT", "ZA", "ZM", "ZW"
]
"""ISO 3166-1 alpha-2 approved country codes"""

@dataclass
class Date:
    """Information regarding release dates"""
    year: Optional[int]
    """The year of the release"""
    month: Optional[int]
    """The month of the release"""
    day: Optional[int]
    """The day of the release"""
    hour: Optional[int]
    """The hour of the release"""
    minute: Optional[int]
    """The minute of the release"""
    second: Optional[int]
    """The second of the release""" 
    timezone: Optional[str]
    """The timezone of the release, in format of +/-HH:MM"""

    @staticmethod
    def from_iso(iso: str) -> 'Date':
        """
        Create a Date object from an ISO 8601 string.
        
        Format: YYYY-MM-DDTHH:MM:SSZZZZ (with ZZZZ being the timezone offset in the format of +/-HH:MM)
        """
        return Date.from_datetime(datetime.fromisoformat(iso))

    @staticmethod
    def from_datetime(dt: datetime) -> 'Date':
        """Create a Date object from a datetime object"""
        return Date(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            timezone=dt.strftime("%z")
        )

@dataclass
class PictureUrls:
    """Information regarding picture URLs"""
    original: Optional[str]
    """An original picture URL"""
    large: Optional[str]
    """A large picture URL"""
    medium: Optional[str]
    """A medium picture URL"""
    small: Optional[str]
    """A small picture URL"""
    tiny: Optional[str]
    """A tiny picture URL"""

@dataclass
class RelationMaps:
    """Information regarding direct relation maps"""
    anidb: Optional[int] = None
    """aniDB ID"""
    anilist: Optional[int] = None
    """AniList ID"""
    animeplanet: Optional[str] = None
    """Anime-Planet slug"""
    anisearch: Optional[int] = None
    """AniSearch ID"""
    annict: Optional[int] = None
    """Annict ID"""
    aozora: Optional[str] = None
    """Discontinued Aozora ID, acquired by Kitsu for its mobile app"""
    bangumi: Optional[int] = None
    """Bangumi (bgm.tv) ID"""
    doujinshi: Optional[str] = None
    """Doujinshi.info Unique ID"""
    doujinshi_slug: Optional[str] = None
    """Doujinshi.info slug"""
    imdb: Optional[str] = None
    """IMDb ID"""
    kaize: Optional[int] = None
    """Kaize ID"""
    kaize_slug: Optional[str] = None
    """Kaize slug"""
    kitsu: Optional[int] = None
    """Kitsu ID"""
    kurozora: Optional[int] = None
    """Kurozora ID, successor to Aozora"""
    livechart: Optional[int] = None
    """LiveChart ID"""
    mangadex: Optional[str] = None
    """MangaDex UUID"""
    mangaupdates: Optional[int] = None
    """MangaUpdates ID"""
    myanimelist: Optional[int] = None
    """MyAnimeList ID"""
    nautiljon: Optional[int] = None
    """Nautiljon ID"""
    nautiljon_slug: Optional[str] = None
    """Nautiljon slug"""
    notify: Optional[str] = None
    """Notify.moe Base64 ID"""
    novelupdates: Optional[int] = None
    """NovelUpdates ID"""
    otakotaku: Optional[int] = None
    """Otak Otaku ID"""
    otakotaku_slug: Optional[str] = None
    """Otak Otaku slug"""
    shikimori: Optional[int] = None
    """Shikimori ID, mirrors MyAnimeList"""
    syoboical: Optional[int] = None
    """Syoboi Calender ID"""
    tmdb: Optional[int] = None
    """The Movie Database ID"""
    tvdb: Optional[int] = None
    """The TVDB ID"""
    tvdb_slug: Optional[str] = None
    """The TVDB slug"""
    trakt: Optional[int] = None
    """Trakt ID"""
    trakt_slug: Optional[str] = None
    """Trakt slug"""
    vndb: Optional[int] = None
    """VNDB ID"""
    wikidata: Optional[str] = None
    """Wikidata ID"""
    others: Dict[str, Union[int, str]] = None
    """Other IDs"""

@dataclass
class MediaInfo:
    """Information regarding media"""
    uuid: str
    """The UUID of the media, used to correlate with the provider"""
    title_display: str
    """The title of the media to be displayed, in order: transliterated, English, native"""
    media_id: Optional[str]
    """The ID of the media in the provider's database"""
    media_slug: Optional[str]
    """The slug of the media in the provider's database"""
    title_native: Optional[str]
    """The title of the media in its native language"""
    title_transliteration: Optional[str]
    """The title of the media transliterated into the Latin alphabet"""
    title_english: Optional[str]
    """The title of the media in English"""
    is_adult: Optional[bool]
    """Whether the media is adult content, `None` if service does not provide this information"""
    media_type: Optional[Literal["anime", "manga", "lightnovel", "shows", "movies", "books", "other"]]
    """The type of media"""
    media_sub_type: Optional[str]
    """The sub-type of media, if applicable"""
    year: Optional[int]
    """The year of the release"""
    release_date: Optional[Date]
    """The release date of the media"""
    unit_counts: Optional[int]
    """The number of units (episodes, chapters) in the media"""
    subunit_counts: Optional[int]
    """The number of subunits (minutes, pages) in the media, total"""
    season_order: Optional[int]
    """Order of the season of following entry, if applicable"""
    volume_counts: Optional[int]
    """The number of volumes in the media. On TV shows this is the number of seasons, if applicable"""
    season: Optional[Literal["winter", "spring", "summer", "fall"]]
    """The season of the release, if applicable"""
    picture_urls: Optional[List[PictureUrls]]
    """List of picture URLs from the provider"""
    CountryOfOrigin: Optional[Iso31661A2]
    """The country of origin of the media"""
    mappings: RelationMaps
    """Direct relation maps"""