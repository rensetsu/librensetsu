"""Pretty print for the proccess"""

from datetime import datetime
from enum import Enum
from typing import Optional


class Platform(Enum):
    """Platform color to be used for pretty printing."""

    ALLCINEMA = 0xEC0A0A
    ANIBRAIN = 0x24A8F0
    ANIDB = 0x2A2F46
    ANILIST = 0x2F80ED
    ANIMENEWSNETWORK = 0x2D50A7
    ANIMEPLANET = 0xE75448
    ANISEARCH = 0xFDA37C
    ANISON = 0xFE0000
    ANNICT = 0xF65B73
    BANGUMI = 0xFBC6C6
    DOUBAN = 0x007722
    DOUJINSHI = 0xFAFAFA
    IMDB = 0xF5C518
    KAIZE = 0x692FC2
    KINOPOISK = 0xF75505
    KITSU = 0xF85235
    KUROZORA = 0xFF9400
    LETTERBOXD = 0x00A0E4
    LIVECHART = 0x67A427
    MANGADEX = 0xFF6740
    MANGAUPDATES = 0x2E51A2
    MYANIMELIST = 0x2F51A3
    NAUTILJON = 0x3C5891
    NOTIFY = 0xDEA99E
    NOVELUPDATES = 0x2D3E50
    OTAKOTAKU = 0xBE2222
    ROTTENTOMATOES = 0xF93209
    SHIKIMORI = 0x2E2E2E
    SHOBOI = 0xE3F0FD
    SILVERYASHA = 0x0172BB
    SIMKL = 0x0B0F10
    SYOBOI = 0xE3F0FD
    SYSTEM = 0x000000
    TMDB = 0x09B4E2
    TRAKT = 0xED1B25
    TVDB = 0x6CD491
    VNDB = 0x29527E
    WIKIDATA = 0x252728
    WORLDART = 0x990000


class Status(Enum):
    """
    Status color to be used for pretty printing.

    Supported status:
        - Pass
        - Fail
        - Err
        - Warn
        - Info
        - Debug
        - Notice
        - Log
        - Ready
        - Assert
    """

    # Use Hex color codes instead of ANSI color codes
    SUCCESS = PASS = 0x2ECC71
    FAIL = 0xE74C3C
    ERROR = ERR = 0xFF0000
    WARN = 0xFFA500
    INFO = 0x3498DB
    DEBUG = 0xBFBFBF
    LOG = 0x1A1A1A
    READY = 0x228B22
    NOTICE = 0x1E90FF
    ASSERT = 0x808080
    BUILD = 0x4B0082


def translate_hex_to_rgb(hex_: int) -> tuple[int, int, int]:
    """Translate hex to rgb"""
    return ((hex_ >> 16) & 0xFF, (hex_ >> 8) & 0xFF, hex_ & 0xFF)


class PrettyPrint:
    """Pretty print for the proccess"""

    def __init__(
        self,
        platform: Platform = Platform.SYSTEM,
        show_date: bool = True,
        show_time: bool = True,
    ) -> None:
        """
        Initialize the pretty print class

        :param platform: The platform to be used, defaults to Platform.SYSTEM
        :type platform: Platform, optional
        :param show_date: Show the date, defaults to True
        :type show_date: bool, optional
        :param show_time: Show the time, defaults to True
        :type show_time: bool, optional
        """
        self.platform = platform
        self.show_date = show_date
        self.show_time = show_time
        self.previously_clear = False

    @staticmethod
    def _get_date() -> str:
        """
        Get the date

        :return: The date
        :rtype: str
        """
        # example: Jun 31
        return datetime.now().strftime("%b %d")

    @staticmethod
    def _get_time() -> str:
        """
        Get the time

        :return: The time
        :rtype: str
        """
        # example: 12:00:00 AM
        return datetime.now().strftime("%I:%M:%S %p")

    def _format_date(self) -> str:
        """
        Format the data

        :return: The formatted date
        :rtype: str
        """
        date = f"\033[104m {self._get_date()} \033[0m " if self.show_date else ""
        time = f"\033[104m {self._get_time()} \033[0m " if self.show_time else ""
        return f"{date}{time}"

    def _format_to_hex(self, enums: Platform | Status) -> str:
        """
        Format the text block to hex

        :param enums: The enum to be formatted
        :type enums: Platform | Status
        :return: The formatted text block
        :rtype: str
        """
        col = translate_hex_to_rgb(enums.value)
        sp = "  "
        if isinstance(enums, Platform):
            sp = " "
        return f"\033[48;2;{col[0]};{col[1]};{col[2]}m{sp}{enums.name}{sp}\033[0m"

    def print(
        self,
        status: Status,
        *args: str,
        clean_line: bool = False,
        platform: Optional[Platform] = None,
        end: str = "\n",
        sep: str = " ",
    ) -> None:
        """
        Print the data

        :param status: The status to be used
        :type status: Status
        :param args: The arguments to be printed
        :type args: str
        :param clean_line: Clean the line, defaults to False
        :type clean_line: bool, optional
        :param platform: The platform to be used, defaults to None (`Platform.SYSTEM`)
        :type platform: Platform, optional
        :param end: The end character, defaults to "\\n"
        :type end: str, optional
        :param sep: The separator, defaults to " "
        :type sep: str, optional
        :raises ValueError: clean_line and end cannot be used together
        """
        if clean_line and end == "\n":
            raise ValueError("clean_line and end cannot be used together")
        anullen = ""
        if not platform:
            platform = self.platform
        if clean_line:
            anullen = "\033[2K\r"
            self.previously_clear = True
        elif self.previously_clear:
            anullen = "\n"
            self.previously_clear = False
        cr_ = "\r" if end == "" else ""
        message = sep.join(args)
        print(
            f"{anullen}{cr_}{self._format_date()}{self._format_to_hex(platform)} {self._format_to_hex(status)} {message}",
            end=end,
        )


__all__ = ["PrettyPrint", "Platform", "Status"]
