# Getting Started with Material for MkDocs

Welcome to the Material for MkDocs getting started guide! This document will help you set up your MkDocs project with the Material theme and get you on your way to creating beautiful documentation.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (version 3.6 or higher)
- pip (Python package installer)

## Installation

1. **Install MkDocs**: Open your terminal and run the following command:

   ```
   pip install mkdocs
   ```

2. **Install the Material theme**: Next, install the Material for MkDocs theme by running:

   ```
   pip install mkdocs-material
   ```

## Creating a New MkDocs Project

To create a new MkDocs project, run the following command in your terminal:

```
mkdocs new my-project
```

This will create a new directory called `my-project` with the basic structure of an MkDocs project.

## Configuring MkDocs

Navigate to your project directory:

```
cd my-project
```

Open the `mkdocs.yml` file in your favorite text editor and configure it to use the Material theme. Here’s a basic example:

```yaml
site_name: My Project
theme:
  name: material
nav:
  - Home: index.md
  - About: about.md
  - Guides:
      - Getting Started: guides/getting-started.md
```

## Building and Serving Your Documentation

To build and serve your documentation locally, run:

```
mkdocs serve
```

This will start a local development server at `http://127.0.0.1:8000/`. Open this URL in your web browser to see your documentation in action.

## Next Steps

Now that you have your MkDocs project set up with the Material theme, you can start adding content to your documentation. Explore the other guides and resources to learn more about customizing your documentation further.

Happy documenting!