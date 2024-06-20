# Installation

---

## Setup Virtual Environment

Using virtual environments is important for several reasons:

- Dependency Isolation: Different projects may require different versions of libraries and dependencies. Virtual
  environments create isolated package management environments for each project, preventing dependency conflicts.

- Simplified Project Management: Virtual environments keep each project's dependency list and configuration separate,
  making development, testing, and deployment easier.

- Avoiding System Pollution: Installing packages in a virtual environment prevents changes to the global Python
  environment, avoiding issues caused by global package version changes.

- Portability: Virtual environments make it easy to replicate project environments. By exporting and importing
  dependency lists, you can ensure consistent operation across different development and production environments.

In summary, virtual environments make Python development more efficient, reliable, and manageable by isolating and
managing dependencies.

```shell
python -m venv .venv
```

/// tab | Windows

```shell
.venv/Scripts/activate
```

///

/// tab | Macos
```shell
source .venv/bin/activate
```
///

---

## Install VisAPI

```shell
pip install visapi
```

---


