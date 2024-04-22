# Hey, Look at me! 👇

**Please delete this part after you read it.**

If you are first create this repository, please read [DELETE_ME.md](./DELETE_ME.md) to get started.

# ai-pet

<div align="center">

[![Build status](https://github.com/andeya/ai-pet/workflows/build/badge.svg?branch=main&event=push)](https://github.com/andeya/ai-pet/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/ai_pet.svg)](https://pypi.org/project/ai_pet/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/andeya/ai-pet/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/andeya/ai-pet/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/andeya/ai-pet/releases)
[![License](https://img.shields.io/github/license/andeya/ai-pet)](https://github.com/andeya/ai-pet/blob/main/LICENSE)
![Coverage Report](assets/images/coverage.svg)

Awesome `ai-pet` is a AI pet chat application

</div>

## Quick start

Conda package manager is recommended. Create a conda environment.

```bash
conda create -n ai_pet python==3.10
```

Activate conda environment and install poetry

```bash
conda activate ai_pet
pip install poetry
```

Then you can run the client using the following command:

```bash
ai_pet --help
```

or with `Poetry`:

````bash
poetry run ai_pet --help
```

### Makefile usage

[`Makefile`](https://github.com/andeya/ai-pet/blob/main/Makefile) contains a lot of functions for faster development.


<details>
<summary>Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
````

Pre-commit hooks coulb be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>Codestyle and type checks</summary>
<p>

Automatic formatting uses `ruff`.

```bash
make polish-codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `ruff` and `darglint` library

</p>
</details>

<details>
<summary>Code security</summary>
<p>

> If this command is not selected during installation, it cannnot be used.

```bash
make check-safety
```

This command launches `Poetry` integrity checks as well as identifies security issues with `Safety` and `Bandit`.

```bash
make check-safety
```

</p>
</details>

<details>
<summary>Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>All linters</summary>
<p>

Of course there is a command to run all linters in one:

```bash
make lint
```

the same as:

```bash
make check-codestyle && make test && make check-safety
```

</p>
</details>

<details>
<summary>Docker</summary>
<p>

```bash
make docker-build
```

which is equivalent to:

```bash
make docker-build VERSION=latest
```

Remove docker image with

```bash
make docker-remove
```

More information [about docker](https://github.com/andeya/py-layout/tree/main/%7B%7B%20cookiecutter.project_name%20%7D%7D/docker).

</p>
</details>

<details>
<summary>Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypycache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 🛡 License

[![License](https://img.shields.io/github/license/andeya/ai-pet)](https://github.com/andeya/ai-pet/blob/main/LICENSE)

This project is licensed under the terms of the `Apache Software License 2.0` license. See [LICENSE](https://github.com/andeya/ai-pet/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{ai_pet,
  author = {andeya},
  title = {Awesome `ai-pet` is a AI pet chat application},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/andeya/ai-pet}}
}
```

## Credits [![🚀 Your next Python package needs a bleeding-edge project structure.](https://img.shields.io/badge/py-layout-%F0%9F%9A%80-brightgreen)](https://github.com/andeya/py-layout)

This project was generated with [`py-layout`](https://github.com/andeya/py-layout)
