# mark2epub

mark2epub is a simple Python script for converting Markdown files, images, and
css files to a single ePub book.

## Installation and use

### Dependencies

mark2epub requires:

- Python (>= 3.4)
- markdown (>= 3.1)
- BeautifulSoup4 (>= 4.14.3)

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

## Limitations/Features to be addressed

- Robustness checks in the `mark2epub.py` script
- Recursive processing of the `images` and `css` folders
- Support for additional fonts
- Support for mathematical notation

## TODO

- [ ] Error handling for class names parsing
- [ ] Add support for symlinks
- [ ] `File "mark2epub.py", line 263, in <module> FileNotFoundError: [Errno 2] No such file or directory: '' ` because of no `./` in output path
