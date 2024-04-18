import os.path as path
from typing import Any

import requests as req


class GraphQL:
    """
    A class to handle GraphQL queries.
    """

    def __init__(self, url: str, headers: dict[str, str] | None = None) -> None:
        """
        Constructor for the GraphQL class.
        :param url: The URL of the GraphQL API.
        :type url: str
        :param headers: The headers to be sent with the request.
        :type headers: dict[str, str], optional
        """
        self.url = url
        self.headers = headers

    def query(self, query: str, variables: dict[str, Any] = {}) -> dict[str, Any]:
        """
        Send a query to the GraphQL API.
        :param query: The query to be sent.
        :type query: str
        :param variables: The variables to be sent with the query.
        :type variables: dict[str, Any], optional
        :return: The response from the API.
        :rtype: dict[str, Any]
        """
        response = req.post(
            self.url,
            json={"query": query, "variables": variables},
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def query_from_file(
        self, file: str, variables: dict[str, Any] = {}
    ) -> dict[str, Any]:
        """
        Send a query to the GraphQL API from a file.
        :param file: The file containing the query.
        :type file: str
        :param variables: The variables to be sent with the query.
        :type variables: dict[str, Any], optional
        :return: The response from the API.
        :rtype: dict[str, Any]
        """
        if not path.exists(file):
            raise FileNotFoundError(f"File '{file}' not found.")
        with open(file, "r") as f:
            query = f.read()
        return self.query(query, variables)
