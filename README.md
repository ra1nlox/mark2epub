# mark2epub

mark2epub is a simple Python script for converting Markdown files, images, and
css files to a single ePub book.

## Installation and use

### Dependencies

mark2epub requires:

- Python (>= 3.4)
- markdown (>= 3.1)
- BeautifulSoup4 (>= 4.14.3)
- lxml (>= 6.0.2)

### Running mark2epub

The syntax for mark2epub is the following:

    $ python md2epub.py <markdown_directory> <output_file.epub>

The output file path can contain unexisting directories, as the code will handle their creation.

The directory `epub_md` is a sample markdown directory for mark2epub.

Note that the directory `markdown_directory` **must** contain

- Markdown `.md` files. Each file represent a chapter in the resulting ePub.
  They are processed by name order, and will appear correspondingly in the e-book.

- An `images` folder, containing the images to be included. Only GIF (`.gif`
  extension), JPEG (`.jpg` or `.jpeg` extensions), and PNG (`.png` extension)
  files are currently supported. This folder is _not_ processed recursively, so
  all images should be placed at the root of this folder.

- A `css` folder, containing the CSS files. This folder is _not_ processed
  recursively, so all css files should be placed at the root of this folder.

- A `description.json` containing meta-information about the e-book. The key
  `cover_image` should indicate the name of the cover image.
  The key `default_css` is a list of css file names that are applied by default
  on all chapters.
  The key `chapters` is a list of dictionaries, each one containing a key `markdown`
  indicating the name of the corresponding markdown file, and a key `css` indicating
  the name of the css file that should be applied specifically to this chapter.
  See the example in the repository for a typical `description.json` file.

## Specific class names for elements

After your text, on every line (at the end of it) you can add class names to that element, as a list separated by whitespaces, included in curly braces, as follows:

```markdown
# Chapter 1 {name1 name-2 names-of-names etc}
```

Class names can consist of latin letters, digits, hyphens and underscores.

After compiling the braces and their insides will be removed.

The code won't handle any typos in class names, so it's up to you to handle it.

## Obsidian tags

You can safely use obsidian tags in your markdown files, as the preprocessor will handle their exclusion from the final built epub.

You can also specify which style of new line you use (before the tag, after it, or without any newline before or after the tag) in the description.json, `tag_new_line_style` field. This new line will be excluded along with the tag.

The valid values are: `before`, `after` and `zero`, respectively, in upper, lower or mixed case (you do you!).

## No cover

To not set any cover, simply leave the `"cover_image": ""`.

## Limitations/Features to be addressed

- Robustness checks in the `mark2epub.py` script
- Recursive processing of the `images` and `css` folders
- Support for additional fonts
- Support for mathematical notation

## TODO

- [ ] Error handling for class names parsing
- [x] Add support for symlinks
- [x] Add support for obsidian tags
