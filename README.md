# librensetsu

Collection of common functions and classes for Rensetsu's service scraper

## Usage

Simply install the package as git on `pip`.

```bash
pip install git+https://github.com/rensetsu/librensetsu.git
```

## Additional notes

This library will download all orphaned dependencies for you to utilize it
without any additional setup, so only this package is needed to be installed.

Why? This is because the library itself acted similarly like SDK instead to
develop a scraper/web crawler for individual services to be used in Rensetsu
unifieddatabase.

### Installed dependencies

- `alive-progress`: Progress bar for long running tasks
- `beautifulsoup4`: HTML parser
- `cloudscraper`: Cloudflare bypassing library
- `cutlet`: Handle Japanese text transliteration to Latin
- `fake-useragent`: Random user agent generator
- `fuzzywuzzy`: Fuzzy string matching library
- `python-Levenshtein`: Levenshtein distance calculation library, required by
  `fuzzywuzzy`
- `requests`: HTTP client library

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
for details.
