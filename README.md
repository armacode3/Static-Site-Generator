# Static-Site-Generator

A custom-built static site generator that converts raw Markdown content into a fully functional HTML website. This project handles recursive directory scanning, static asset management, and robust Markdown parsing.

## Features

* **Markdown Parsing**: Converts Markdown files to HTML, supporting various block types (headings, paragraphs, lists, blockquotes, code blocks).
* **Inline Formatting**: Supports bold, italic, inline code, links, and images.
* **Recursive Generation**: Crawls the `content/` directory to generate pages while preserving the directory structure.
* **Static Asset Management**: Automatically copies images and CSS from `static/` to the public directory.
* **Templating**: Wraps generated content in a configurable `template.html` file.

## Project Structure

* `src/`: Contains the source code (Python).
* `content/`: Stores the raw Markdown files.
* `static/`: Stores static assets like images and CSS.
* `docs/`: The output directory for the generated site.
* `public/`: (Optional) staging directory for serving.

##  Usage

### Prerequisites

* Python 3.x

### Running the Generator

To build the site and start a local server, use the provided script:

```bash
./main.sh
