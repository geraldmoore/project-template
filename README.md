# Project Template

A [Copier](https://copier.readthedocs.io/) template for Python projects using [uv](https://docs.astral.sh/uv/) and [prek](https://prek.j178.dev/) for git hook management.

## Prerequisites

- [copier](https://copier.readthedocs.io/)
- [copier-template-extensions](https://github.com/copier-org/copier-template-extensions)
- [python-slugify](https://github.com/un33k/python-slugify)

```bash
pip install copier
pip install copier-template-extensions
pip install python-slugify
```

## Usage

### Generate a new project

```bash
copier copy --trust gh:geraldmoore/project-template /path/to/your/project
```

### Update an existing project

In the project repository:

```bash
copier update
```
