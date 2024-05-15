from datetime import datetime, timezone
from enum import Enum
from typing import List, Literal, Optional, Union

from pydantic import UUID4, BaseModel, ConfigDict, Field, HttpUrl
from pydantic_extra_types.country import CountryAlpha2
from pydantic_extra_types.language_code import LanguageAlpha2


class DateTime(BaseModel):
    year: Optional[int] = Field(
        None, description="The year of the release", ge=1917, le=2100
    )
    """The year of the release"""
    month: Optional[int] = Field(
        None, description="The month of the release", ge=1, le=12
    )
    """The month of the release"""
    day: Optional[int] = Field(None, description="The day of the release", ge=1, le=31)
    """The day of the release"""
    hour: Optional[int] = Field(
        None, description="The hour of the release", ge=0, le=23
    )
    """The hour of the release"""
    minute: Optional[int] = Field(
        None, description="The minute of the release", ge=0, le=59
    )
    """The minute of the release"""
    second: Optional[int] = Field(
        None, description="The second of the release", ge=0, le=59
    )
    """The second of the release"""
    timezone: Optional[str] = Field(None, description="The timezone of the release")
    """The timezone of the release"""

    @staticmethod
    def from_iso(iso: str) -> "DateTime":
        """Create a DateTime object from an ISO 8601 string"""
        return DateTime.from_datetime(datetime.fromisoformat(iso))

    @staticmethod
    def from_timestamp(timestamp: Union[int, float, str]) -> "DateTime":
        """Create a DateTime object from a timestamp"""
        if isinstance(timestamp, str) or isinstance(timestamp, int):
            timestamp = float(timestamp)
        return DateTime.from_datetime(datetime.fromtimestamp(timestamp, tz=timezone.utc))

    @staticmethod
    def from_datetime(dt: datetime) -> "DateTime":
        """Create a DateTime object from a datetime object"""
        return DateTime(
            year=dt.year,
            month=dt.month,
            day=dt.day,
            hour=dt.hour,
            minute=dt.minute,
            second=dt.second,
            timezone=dt.tzinfo.tzname(None) if dt.tzinfo else None,
        )


class PictureUrls(BaseModel):
    """Information about the picture"""

    original: Optional[HttpUrl] = Field(None, description="An original picture URL")
    """An original picture URL"""
    large: Optional[HttpUrl] = Field(None, description="A large picture URL")
    """A large picture URL"""
    medium: Optional[HttpUrl] = Field(None, description="A medium picture URL")
    """A medium picture URL"""
    small: Optional[HttpUrl] = Field(None, description="A small picture URL")
    """A small picture URL"""
    tiny: Optional[HttpUrl] = Field(None, description="A tiny picture URL")
    """A tiny picture URL"""


class IdSlugPair(BaseModel):
    """A pair of an ID and a slug"""

    id: Optional[Union[int, str, UUID4]] = Field(
        None, description="The ID of the media"
    )
    """The ID of the media"""
    slug: Optional[str] = Field(None, description="The slug of the media")
    """The slug of the media"""


class ConventionalMediaType(str, Enum):
    """The type of the media in conventional media databases"""

    tv = series = shows = "shows"
    """TV shows"""
    movie = movies = "movies"
    """Movies"""


class ConventionalMapping(IdSlugPair):
    """Mapping information on conventional media databases"""

    media_type: Optional[ConventionalMediaType] = Field(
        None, description="The type of the media in conventional media databases"
    )
    """The type of the media in conventional media databases"""
    season: Optional[int] = Field(
        None, description="The season number of the media, if applicable"
    )
    """The season number of the media, if applicable"""


class RelationMaps(BaseModel):
    """Information about the direct relations of the media in other databases"""

    model_config = ConfigDict(extra="allow")

    allcinema: Optional[int] = Field(
        None, description="allcinema ID (Regional, JP): https://www.allcinema.net/"
    )
    """allcinema ID (Regional, JP): https://www.allcinema.net/"""
    anibrain: Optional[int] = Field(
        None,
        description="AniBrain.ai ID: https://anibrain.ai/, should be 1:1 with AniList",
    )
    """AniBrain.ai ID: https://anibrain.ai/, should be 1:1 with AniList"""
    anidb: Optional[int] = Field(None, description="AniDB ID: https://anidb.net/")
    """AniDB ID: https://anidb.net/"""
    anilist: Optional[int] = Field(None, description="AniList ID: https://anilist.co/")
    """AniList ID: https://anilist.co/"""
    animenewsnetwork: Optional[int] = Field(
        None, description="Anime News Network ID: https://www.animenewsnetwork.com/"
    )
    """Anime News Network ID: https://www.animenewsnetwork.com/"""
    animeplanet: Optional[str] = Field(
        None, description="Anime-Planet slug: https://www.anime-planet.com/"
    )
    """Anime-Planet slug: https://www.anime-planet.com/"""
    animethemes: Optional[IdSlugPair] = Field(
        None, description="AnimeThemes ID: https://animethemes.moe/"
    )
    """AnimeThemes ID: https://animethemes.moe/"""
    anisearch: Optional[int] = Field(
        None,
        description="AniSearch ID (Regional, DE ES FR JP IT): https://www.anisearch.com/",
    )
    """AniSearch ID (Regional, DE ES FR JP IT): https://www.anisearch.com/"""
    anison: Optional[int] = Field(
        None, description="Anison ID (Regional, JP): https://www.anison.info/"
    )
    """Anison ID (Regional, JP): https://www.anison.info/"""
    annict: Optional[int] = Field(
        None, description="Annict ID (Regional, JP): https://annict.com/"
    )
    """Annict ID (Regional, JP): https://annict.com/"""
    aozora: Optional[str] = Field(
        None,
        description="Discontinued Aozora ID, acquired by Kitsu for its mobile app; superceded by Kurozora",
    )
    """Discontinued Aozora ID, acquired by Kitsu for its mobile app; superceded by Kurozora"""
    bangumi: Optional[int] = Field(
        None, description="Bangumi ID (Regional, CN): https://bgm.tv/"
    )
    """Bangumi ID (Regional, CN): https://bgm.tv/"""
    douban: Optional[int] = Field(
        None, description="Douban ID (Regional, CN): https://www.douban.com/"
    )
    """Douban ID (Regional, CN): https://www.douban.com/"""
    doujinshi: Optional[IdSlugPair] = Field(
        None, description="Doujinshi.info ID: https://www.doujinshi.info/"
    )
    """Doujinshi.info ID: https://www.doujinshi.info/"""
    imdb: Optional[ConventionalMapping] = Field(
        None, description="IMDb ID: https://www.imdb.com/"
    )
    """IMDb ID: https://www.imdb.com/"""
    kaize: Optional[IdSlugPair] = Field(None, description="Kaize ID: https://kaize.io/")
    """Kaize ID: https://kaize.io/"""
    kitsu: Optional[IdSlugPair] = Field(None, description="Kitsu ID: https://kitsu.io/")
    """Kitsu ID: https://kitsu.io/"""
    kinopoisk: Optional[int] = Field(
        None, description="Kinopoisk ID (Regional, RU): https://www.kinopoisk.ru/"
    )
    """Kinopoisk ID (Regional, RU): https://www.kinopoisk.ru/"""
    kurozora: Optional[int] = Field(
        None, description="Kurozora ID: https://kurozora.app/"
    )
    """Kurozora ID: https://kurozora.app/"""
    lain: Optional[int] = Field(
        None, description="Lain ID (Regional, JP): https://lain.gr.jp/"
    )
    """Lain ID (Regional, JP): https://lain.gr.jp/"""
    livechart: Optional[int] = Field(
        None, description="LiveChart ID: https://www.livechart.me/"
    )
    """LiveChart ID: https://www.livechart.me/"""
    letterboxd: Optional[str] = Field(
        None, description="Letterboxd slug: https://letterboxd.com/"
    )
    """Letterboxd slug: https://letterboxd.com/"""
    mangadex: Optional[UUID4] = Field(
        None, description="MangaDex UUID: https://mangadex.org/"
    )
    """MangaDex UUID: https://mangadex.org/"""
    mangaupdates: Optional[int] = Field(
        None, description="MangaUpdates ID: https://www.mangaupdates.com/"
    )
    """MangaUpdates ID: https://www.mangaupdates.com/"""
    myanimelist: Optional[int] = Field(
        None, description="MyAnimeList ID: https://myanimelist.net/"
    )
    """MyAnimeList ID: https://myanimelist.net/"""
    nautiljon: Optional[IdSlugPair] = Field(
        None, description="Nautiljon ID (Regional, FR): https://www.nautiljon.com/"
    )
    """Nautiljon ID (Regional, FR): https://www.nautiljon.com/"""
    notify: Optional[str] = Field(
        None, description="Notify.moe Base64: https://notify.moe/"
    )
    """Notify.moe Base64: https://notify.moe/"""
    novelupdates: Optional[str] = Field(
        None, description="NovelUpdates slug: https://www.novelupdates.com/"
    )
    """NovelUpdates slug: https://www.novelupdates.com/"""
    otakotaku: Optional[IdSlugPair] = Field(
        None, description="Otak Otaku ID (Regional, ID): https://otakotaku.com/"
    )
    """Otak Otaku ID (Regional, ID): https://otakotaku.com/"""
    rottentomatoes: Optional[str] = Field(
        None, description="Rotten Tomatoes slug: https://www.rottentomatoes.com/"
    )
    """Rotten Tomatoes slug: https://www.rottentomatoes.com/"""
    silveryasha: Optional[int] = Field(
        None,
        description="Silveryasha DB Tontonan Indonesia ID (Regional, ID): https://db.silveryasha.web.id",
    )
    """Silveryasha DB Tontonan Indonesia ID (Regional, ID): https://db.silveryasha.web.id"""
    shikimori: Optional[IdSlugPair] = Field(
        None,
        description="""
    Shikimori ID, mirrors MyAnimeList (Regional, RU): https://shikimori.one

    Slug most of the time is equal to ID, however, some title may have additiona
    alphabet as the prefix (eg. `z28977`). Use slug to redirect user without
    HTTP 301, eg: https://shikimori.one/animes/z28977
    """,
    )
    """
    Shikimori ID, mirrors MyAnimeList (Regional, RU): https://shikimori.one

    Slug most of the time is equal to ID, however, some title may have additiona
    alphabet as the prefix (eg. `z28977`). Use slug to redirect user without
    HTTP 301, eg: https://shikimori.one/animes/z28977
    """
    syoboical: Optional[int] = Field(
        None, description="Syoboi Calendar ID (Regional, JP): https://cal.syoboi.jp/"
    )
    """Syoboi Calendar ID (Regional, JP): https://cal.syoboi.jp/"""
    tmdb: Optional[ConventionalMapping] = Field(
        None, description="The Movie Database ID: https://www.themoviedb.org/"
    )
    """The Movie Database ID: https://www.themoviedb.org/"""
    trakt: Optional[ConventionalMapping] = Field(
        None, description="Trakt ID: https://trakt.tv/"
    )
    """Trakt ID: https://trakt.tv/"""
    tvdb: Optional[ConventionalMapping] = Field(
        None, description="TheTVDB ID: https://www.thetvdb.com/"
    )
    """TheTVDB ID: https://www.thetvdb.com/"""
    vndb: Optional[int] = Field(None, description="VNDB ID: https://vndb.org/")
    """VNDB ID: https://vndb.org/"""
    wikidata: Optional[str] = Field(
        None, description="Wikidata ID: https://www.wikidata.org/"
    )
    """Wikidata ID: https://www.wikidata.org/"""
    worldart: Optional[int] = Field(
        None, description="World Art ID (Regional, RU): https://world-art.ru/"
    )
    """World Art ID (Regional, RU): https://world-art.ru/"""


Date = DateTime


class MediaInfo(BaseModel):
    """Information about the media"""

    uuid: UUID4 = Field(
        ..., description="The UUID of the media, used to correlate with provider"
    )
    """The UUID of the media, used to correlate with provider"""
    title_display: str = Field(
        ...,
        description="The title of the media to be displayed, in order: transliterated, English, native",
    )
    """The title of the media to be displayed, in order: transliterated, English, native"""
    title_native: Optional[str] = Field(
        None, description="The native title of the media"
    )
    """The native title of the media"""
    title_transliterated: Optional[str] = Field(
        None, description="The transliterated title of the media into Latin script"
    )
    """The transliterated title of the media into Latin script"""
    title_english: Optional[str] = Field(
        None, description="The English title of the media"
    )
    """The English title of the media"""
    synonyms: Optional[List[str]] = Field(None, description="The synonyms of the media")
    """The synonyms of the media"""
    is_adult: Optional[bool] = Field(
        None, description="Whether the media is adult-only"
    )
    """Whether the media is adult-only"""
    media_type: Literal[
        "anime", "manga", "lightnovel", "shows", "movies", "books", "other"
    ] = Field(..., description="The type of the media")
    """The type of the media"""
    media_sub_type: Optional[str] = Field(
        None,
        description="The sub-type of the media: TV, OVA, ONA, movie, manga, novel, etc.",
    )
    """The sub-type of the media: TV, OVA, ONA, movie, manga, novel, etc."""
    year: Optional[int] = Field(
        None, description="The year of the release", ge=1917, le=2100
    )
    """The year of the release"""
    start_date: Optional[DateTime] = Field(
        None, description="The start date of the media"
    )
    """The start date of the media"""
    end_date: Optional[DateTime] = Field(None, description="The end date of the media")
    """The end date of the media"""
    unit_order: Optional[int] = Field(
        None,
        description="Order of the unit of following entry. On TV shows this is the episode number, if applicable",
    )
    """Order of the unit of following entry. On TV shows this is the episode number, if applicable"""
    unit_counts: Optional[int] = Field(
        None, description="The number of (episodes, chaters) units in the media"
    )
    """The number of (episodes, chaters) units in the media"""
    subunit_order: Optional[int] = Field(
        None,
        description="Order of the subunit of following entry. On TV shows this is the minute of the episode, if applicable",
    )
    """Order of the subunit of following entry. On TV shows this is the minute of the episode, if applicable"""
    subunit_counts: Optional[int] = Field(
        None, description="The number of subunits (minutes, pages) in the media"
    )
    """The number of subunits (minutes, pages) in the media"""
    volume_order: Optional[int] = Field(
        None,
        description="Order of the volume of following entry. On TV shows, this is the season number, if applicable",
    )
    """Order of the volume of following entry. On TV shows, this is the season number, if applicable"""
    volume_counts: Optional[int] = Field(
        None, description="The number of volumes/seasons in the media"
    )
    """The number of volumes/seasons in the media"""
    season: Optional[Literal["winter", "spring", "summer", "fall"]] = Field(
        None, description="The season of the release"
    )
    """The season of the release"""
    picture_urls: List[PictureUrls] = Field(
        ..., description="List of picture URLs of the media"
    )
    country_of_origin: Optional[CountryAlpha2] = Field(
        None, description="The country of origin of the media"
    )
    mappings: Optional[RelationMaps] = Field(
        None,
        description="Information about the direct relations of the media in other databases",
    )
    languages: Optional[List[LanguageAlpha2]] = Field(
        None, description="The languages of the media"
    )
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
    ] = Field("rensetsu", description="The source of the data")
    """The source of the data"""
