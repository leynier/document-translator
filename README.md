# Document Translator

Tool to translate big documents using LLMs.

**Usage**:

```console
document-translator [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `word`

## Translate Word documents

**Usage**:

```console
document-translator word [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `-i, --input FILE`: Input file path  [required]
* `-o, --output TEXT`: Output file path  [required]
* `-s, --language-source TEXT`: Source language. For example: 'spanish'  [required]
* `-t, --language-target TEXT`: Target language. For example: 'english'  [required]
* `--translator [openai]`: Translator  [default: openai]
* `--help`: Show this message and exit.
