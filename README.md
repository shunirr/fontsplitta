# web-font-splitter

This is a CLI tool for splitting fonts and generating CSS.

## Requirements

- Python 3

## Getting Started

Install the dependency libraries:

```console
poetry install
```

Generate `unicode_ranges.txt` using Google Fonts' CSS:

```console
poetry run python ./get_unicode_ranges_from_google_fonts.py
```

Split fonts and generate CSS:

```console
poetry run python ./web_font_splitter.py FONT_FILE
```

## Using a custom CSS template file

If you want to modify the output CSS, you can create a new `font-face.css.template` file:

```
@font-face {
  font-family: "${font_family}";
  font-style: ${font_style};
  font-weight: ${font_weight};
  src: url(http://localhost:8080/output/${font_filename}) format("${font_format}");
  unicode-range: ${unicode_range};
}
```

Basically, you should use your environment's hostname in the `src` section.

And then,

```console
poetry run python ./web_font_splitter.py FONT_FILE --css_template=YOUR_CSS_TEMPLATE
```

## Using custom unicode ranges

If you want to use custom unicode ranges, you can use the `--unicode_ranges_file` option:

```console
poetry run python ./web_font_splitter.py FONT_FILE --unicode_ranges_file=YOUR_UNICODE_RANGES_FILE
```

You can generate the unicode ranges using your web page contents.

## Test with local web server

```console
poetry run python test_server.py
```
