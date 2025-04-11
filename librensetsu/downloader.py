"""
Better Downloader module
"""

from json import loads
from os.path import exists
from time import time
from traceback import print_exc
from typing import Any

import requests as rqp
from alive_progress import alive_bar as abr
from cloudscraper import CloudScraper as CSP

from .grammar import pluralize as plz
from .humanclock import convert_float_to_time as cftt
from .prettyprint import PrettyPrint, Status


class Downloader:
    """Download data from the internet."""

    def __init__(
        self,
        pprint_instance: PrettyPrint,
        url: str,
        save_as: str,
        user_agent: str = "",
        headers: dict[str, str] = {},
        params: dict[str, str] = {},
        do_not_load: bool = False,
    ) -> None:
        """
        Initialize the Downloader class.

        :param pprint_instance: The PrettyPrint instance to use for printing.
        :type pprint_instance: PrettyPrint
        :param url: The URL to download from.
        :type url: str
        :param save_as: The file to save the downloaded data to.
        :type save_as: str
        :param user_agent: The User-Agent to use for the request, defaults to ""
        :type user_agent: str, optional
        :param headers: The headers to use for the request, defaults to {}
        :type headers: dict[str, str], optional
        :param params: The parameters to use for the request, defaults to {}
        :type params: dict[str, str], optional
        :param do_not_load: Whether to not load the data from local
        :type do_not_load: bool, optional
        """
        self.url = url
        self.headers = headers
        self.params = params
        self.save_as = save_as
        self.pr = pprint_instance
        self.dnl = do_not_load

        if user_agent:
            self.headers["User-Agent"] = user_agent

        self.pr.print(Status.READY, f"Downloader initialized with URL {self.url}")

    def _load_from_local(self) -> str:
        """
        Load the data from a local file.

        :return: The loaded data.
        :rtype: Any
        """
        if self.dnl:
            return ""
        # check if the file exists
        if not exists(self.save_as):
            self.pr.print(Status.ERR, f"File {self.save_as} does not exist")
            raise FileNotFoundError(f"File {self.save_as} does not exist")
        with open(self.save_as, "r") as file:
            return file.read()

    def _unified_resp(self, resp: rqp.Response) -> str:
        """
        Unified response for requests and cloudscraper.

        :param resp: The response object.
        :type resp: rqp.Response
        :return: The downloaded data.
        :rtype: str
        """
        resp.raise_for_status()
        dlen = int(resp.headers.get("content-length", 0)) // 1024
        dlen2 = (dlen + 1) if dlen not in [0, None] else dlen
        self.pr.print(Status.INFO, f"Downloading from {self.url}")
        start_time = time()
        chk = 0
        with open(self.save_as, "wb") as file, abr(total=dlen2, unit="B", scale="IEC") as bar:  # type: ignore
            for chunk in resp.iter_content(chunk_size=8192):
                if chunk:
                    file.write(chunk)
                    chk += 1
                    bar(8192)
        end_time = time()
        self.pr.print(
            Status.INFO,
            f"Downloaded {plz(chk, 'chunk')} in {cftt(end_time - start_time)}",
        )
        return self._load_from_local()

    def _unified_exception(self, excepts: Exception) -> None:
        """
        Unified exception for requests and cloudscraper.

        :param excepts: The exception object.
        :type excepts: Exception
        """
        self.pr.print(Status.ERR, f"Failed to download data from {self.url}: {excepts}")
        print_exc()

    def _download_with_requests(self) -> str:
        """
        Download the data using the requests module.

        :return: The downloaded data.
        :rtype: str
        """
        try:
            with rqp.get(
                self.url, headers=self.headers, params=self.params, stream=True
            ) as rsp:
                return self._unified_resp(rsp)
        except rqp.exceptions.RequestException as err:
            self._unified_exception(err)
            raise err

    def _download_with_cloudscraper(self) -> str:
        """
        Download the data using the CloudScraper module.

        :return: The downloaded data.
        :rtype: str
        """
        try:
            with CSP() as scraper:
                with scraper.get(
                    self.url, headers=self.headers, params=self.params, stream=True
                ) as rsp:
                    return self._unified_resp(rsp)
        except Exception as err:
            self._unified_exception(err)
            raise err

    def download(self, use_cloudscraper: bool = False) -> str:
        """
        Download the data from the URL.

        :param use_cloudscraper: Whether to use CloudScraper to bypass Cloudflare protection, defaults to False
        :type use_cloudscraper: bool, optional
        :return: The downloaded data.
        :rtype: str
        """
        try:
            if use_cloudscraper:
                data = self._download_with_cloudscraper()
            data = self._download_with_requests()
            return data
        except Exception:
            self.pr.print(Status.WARN, "Loading from old downloaded file")
            return self._load_from_local()

    def json(self, use_cloudscraper: bool = False) -> Any:
        """
        Download the data from the URL and parse it as JSON.

        :param use_cloudscraper: Whether to use CloudScraper to bypass Cloudflare protection, defaults to False
        :type use_cloudscraper: bool, optional
        :return: The downloaded data.
        :rtype: Any
        """
        if self.save_as.endswith(".json"):
            return loads(self.download(use_cloudscraper))
        self.pr.print(Status.ERR, "File is not a JSON file")
        raise ValueError("File is not a JSON file")

    def __str__(self) -> str:
        return f"Downloader({self.url})"

    def __repr__(self) -> str:
        return f"Downloader({self.url})"

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Downloader) and self.url == other.url

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)
