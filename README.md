# mkdocs-timetoread-plugin

mkdocs-timetoread-plugin is a lightweight *'estimated time to read'* generator for MkDocs inspired by @alanhamlett's [readtime](https://github.com/alanhamlett/readtime) and Medium's [read time formula](https://help.medium.com/hc/en-us/articles/214991667-Read-time).

## Setup

Install the plugin using pip:

`pip install mkdocs-timetoread-plugin`

Activate the plugin in `mkdocs.yml`:

```yaml
plugins:
  - search
  - timetoread
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

## mkdocs.yml Configuration

* `wpm` - Sets the 'words per minute' value for calculating estimated read time.
  * Default value is `255`
  * Possible value range: `1` - `999`

* `allPages` - Sets all markdown files to have their read times' calculated unless explicitly disabled in the files' Front Matter.
  * Default value is `True`
  * Possible values: `True` or `False`

* `textColor` - Sets the CSS color for styling the 'Estimated read time:' text.
  * Default value is `bdbdbd`
  * Possible value range: `000000` - `ffffff`

* textBeforeMinutes - Sets the text before the 'minute' value
  * Default value is `null`

* textAfterMinutes - Sets the text after the 'minute' value
  * Default value is `min read`

### Example Configuration

``` yaml
plugins:
  - timetoread:
      wpm: 190
      allPages: True
      textColour: 000000
```

## Front Matter

Other configuration options are available by defining the following in a YAML front matter block in each markdown file.

``` yaml
// Disable timetoread on a per file basis if `allPages is set to True
timetoread: False
```

``` yaml
// Enable timetoread on a per file basis if `allPages` is set to False
timetoread: True
```

## Usage

Once activated `mkdocs-timetoread-plugin` will automatically add a new line, with the estimated time to read the document, after the `</h1>` tag in the HTML output generated by MkDocs.
