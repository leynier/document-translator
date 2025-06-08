# DocuLingo

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/pypi/v/doculingo?color=%2334D058&label=Version)](https://pypi.org/project/doculingo)
[![Last commit](https://img.shields.io/github/last-commit/leynier/doculingo.svg?style=flat)](https://github.com/leynier/doculingo/commits)
[![Commit activity](https://img.shields.io/github/commit-activity/m/leynier/doculingo)](https://github.com/leynier/doculingo/commits)
[![Stars](https://img.shields.io/github/stars/leynier/doculingo?style=flat&logo=github)](https://github.com/leynier/doculingo/stargazers)
[![Forks](https://img.shields.io/github/forks/leynier/doculingo?style=flat&logo=github)](https://github.com/leynier/doculingo/network/members)
[![Watchers](https://img.shields.io/github/watchers/leynier/doculingo?style=flat&logo=github)](https://github.com/leynier/doculingo)
[![Contributors](https://img.shields.io/github/contributors/leynier/doculingo)](https://github.com/leynier/doculingo/graphs/contributors)

A **command-line tool** to translate large documents using language models. It preserves the file formatting and simplifies migrating documentation to other languages.

---

## Table of Contents

* [Overview](#overview)
* [Key Features](#key-features)
* [Installation](#installation)
* [Quick Start](#quick-start)
* [CLI Reference](#cli-reference)
* [Development](#development)
* [Environment Variables](#environment-variables)
* [License](#license)

---

## Overview

`doculingo` helps you translate documents while preserving their formatting. It currently works with Word files and aims to support additional formats in the future, making it ideal for projects that require multiple language versions without losing the original layout.

---

## Key Features

* ✨ **Automatic Translation** — uses OpenAI to safely translate paragraphs.
* 📝 **Preserves Styles** — copies fonts, colors, and alignment to the translated version.
* 📄 **Document Support** — currently handles large `.docx` files with more formats planned.
* 🔁 **Automatic Retries** — retries when the API fails.
* ⚙️ **Simple CLI** — clear commands with built-in help.

---

## Installation

Run instantly with [uv](https://github.com/astral-sh/uv) without installing:

```bash
uvx doculingo --help
```

Or install from PyPI:

```bash
pip install doculingo
```

---

## Quick Start

Translate a Word document from Spanish to English:

```bash
doculingo word \
  --input file.docx \
  --output translated.docx \
  --language-source spanish \
  --language-target english
```

---

## CLI Reference

Get the full list of options with:

```bash
doculingo --help
```

The main subcommand is `word`, designed for `.docx` files.

---

## Development

Install the dependencies and run the tool locally:

```bash
uv lock
uv sync --all-groups --all-extras
uv run doculingo --help
```

---

## Environment Variables

Copy `.env.example` to `.env` and set `OPENAI_API_KEY` with your OpenAI key.

---

## License

Distributed under the MIT license. See the [`license`](license) file.
