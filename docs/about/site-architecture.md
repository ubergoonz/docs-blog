---
icon: octicons/stack-16
---

# :octicons-stack-16: Site Architecture

## Overview

This website is hosted on [GitHub Pages](https://pages.github.com){target="_blank"}.

Contents are created in [Markdown](https://www.markdownguide.org){target="_blank"} and uses [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/){target="_blank"} as the Static Page Generator to render the Markdown files into [HTML](https://en.wikipedia.org/wiki/HTML){target="_blank"} files.

The source files are stored into a Git repository hosted on GitHub.com and uses [GitHub Action](https://github.com/features/actions){target="_blank"} as automation to build and deploy into GitHub Pages.

## Workflow

<figure markdown="span">
```puml
@startuml

title "Workflow"

package "Local Development" {
    actor dev
    file markdown
    
    dev -> markdown : create/update
}

package  "GitHUb.com" {
    database "repository"
    component  "GitHb Action" as  action
    file html
    component "GitHub Pages" as pages 

}

markdown -> repository : git push
repository -> action 
action -> html  : build
html -> pages : deploy (publish)

@enduml
```

<figcaption>Workflow </figcaption>
</figure>