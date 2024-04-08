from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Union, Literal, List, Dict

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
    doujinshi: Optional[str] = None
    """Doujinshi.info Unique ID: https://doujinshi.info"""
    doujinshi_slug: Optional[str] = None
    """Doujinshi.info slug: https://doujinshi.info"""
    imdb: Optional[str] = None
    """IMDb ID: https://www.imdb.com"""
    kaize: Optional[int] = None
    """Kaize ID: https://kaize.io"""
    kaize_slug: Optional[str] = None
    """Kaize slug: https://kaize.io"""
    kitsu: Optional[int] = None
    """Kitsu ID: https://kitsu.io"""
    kurozora: Optional[int] = None
    """Kurozora ID, successor to Aozora: https://kurozora.app"""
    lain: Optional[int] = None
    """Lain ID: https://lain.gr.jp"""
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
    nautiljon: Optional[int] = None
    """Nautiljon ID (Regional, FR): https://www.nautiljon.com"""
    nautiljon_slug: Optional[str] = None
    """Nautiljon slug (Regional, FR): https://www.nautiljon.com"""
    notify: Optional[str] = None
    """Notify.moe Base64 ID: https://notify.moe"""
    novelupdates: Optional[str] = None
    """NovelUpdates slug: https://www.novelupdates.com"""
    otakotaku: Optional[int] = None
    """Otak Otaku ID (Regional, ID): https://otakotaku.com"""
    otakotaku_slug: Optional[str] = None
    """Otak Otaku slug (Regional, ID): https://otakotaku.com"""
    rotten_tomatoes: Optional[str] = None
    """Rotten Tomatoes slug: https://www.rottentomatoes.com"""
    silveryasha: Optional[int] = None
    """Silver-Yasha DB Tontonan Indonesia (Regional, ID): https://db.silveryasha.web.id"""
    shikimori: Optional[int] = None
    """Shikimori ID, mirrors MyAnimeList (Regional, RU): https://shikimori.one"""
    syoboical: Optional[int] = None
    """Syoboi Calender ID (Regional, JP): https://cal.syoboi.jp"""
    tmdb: Optional[int] = None
    """The Movie Database ID: https://www.themoviedb.org"""
    tvdb: Optional[int] = None
    """The TVDB ID: https://www.thetvdb.com"""
    tvdb_slug: Optional[str] = None
    """The TVDB slug: https://www.thetvdb.com"""
    trakt: Optional[int] = None
    """Trakt ID: https://trakt.tv"""
    trakt_slug: Optional[str] = None
    """Trakt slug: https://trakt.tv"""
    vndb: Optional[int] = None
    """VNDB ID: https://vndb.org"""
    wikidata: Optional[str] = None
    """Wikidata ID: https://www.wikidata.org"""
    others: Dict[str, Union[int, str]] = {}
    """Other IDs"""

@dataclass
class BasicMediaInfo:
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
    is_adult: Optional[bool]
    """Whether the media is adult content, `None` if service does not provide this information"""
    media_type: Literal["anime", "manga", "lightnovel", "shows", "movies", "books", "other"]
    """The type of media"""
    media_sub_type: Optional[str]
    """The sub-type of media, if applicable"""
    year: Optional[int]
    """The year of the release"""
    release_date: Optional[Date]
    """The release date of the media"""
    unit_order: Optional[int]
    """Order of the unit of following entry. On TV shows this is the episode number, if applicable"""
    unit_counts: Optional[int]
    """The number of units (episodes, chapters) in the media"""
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

@dataclass
class MediaInfo(BasicMediaInfo):
    """Extended information regarding media, used for individual media entries from a provider"""
    media_id: Optional[Union[int, str]]
    """The ID of the media in the provider's database"""
    media_slug: Optional[str]
    """The slug of the media in the provider's database"""