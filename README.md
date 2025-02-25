# web-font-splitter

This is a CLI tool for splitting fonts and generating CSS like a Google Fonts.

## Requirements

- Python 3

## Getting Started

Install the dependency libraries:

```console
pip install -r requirements.txt
```

Generate `unicode_ranges.txt` using Google Fonts' CSS:

```console
python ./get_unicode_ranges_from_google_fonts.py
```

Split fonts and generate CSS:

```console
python ./web_font_splitter.py FONT_FILE
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
python ./web_font_splitter.py FONT_FILE --css_template=YOUR_CSS_TEMPLATE
```

## Using custom unicode ranges

If you want to use custom unicode ranges, you can use the `--unicode_ranges_file` option:

```console
python ./web_font_splitter.py FONT_FILE --unicode_ranges_file=YOUR_UNICODE_RANGES_FILE
```

For example, you can generate the unicode ranges using your web page contents.

## Test with local web server

You can check the generated fonts and the generated css on your browser:

```console
python ./test_server.py
```

And then, access to `http://localhost:8080/`.
