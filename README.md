# IndyDevTools
> An Agentic Engineering toolbox for independent developers that are transforming into Agentic Engineers.

## Table of Contents
- [IndyDevTools](#indydevtools)
  - [Table of Contents](#table-of-contents)
  - [Principles](#principles)
  - [*Start From Gold* CLI API](#start-from-gold-cli-api)
    - [Youtube Generate Metadata `idt yt generate-meta`](#youtube-generate-metadata-idt-yt-generate-meta)
  - [The Configuration File](#the-configuration-file)
    - [Structure](#structure)
  - [Goal \& Architecture](#goal--architecture)
  - [Questions to answer](#questions-to-answer)
  - [Local Dev Commands (excluded from dist)](#local-dev-commands-excluded-from-dist)
  - [Resources](#resources)

## Principles
- **Heavy Agentic Engineering Bias**
  - Every tool asks and answers the question: *how can AI agents do this for me?*
  - Every tool utilizes an intuitive, step by step CLI that asks for the minimum amount of information to get started.
  - Every tool in this toolbox is an app that creates on your behalf.
  - Every tool will boost your productivity by utilize great design and the incredible generation abilities of LLMs.
  - Every tool is powered by LLM technology.
- **Simple, single configuration file**
  - One config file to control all the tools.
- **Many agentic tools, one top level command**
  - Every user will have a single command to run all the tools.
- **Best CLI documentation ever**
  - Visit a single, simple, agent controlled and generated website that has all the documentation for all the tools.
- **Open-Core Business Model**
  - Free Version
    - Open Source
    - Limited Features
  - Paid Version
    - Closed Source
    - Full Features

## *Start From Gold* CLI API

### Youtube Generate Metadata `idt yt generate-meta`
- Description
  - This tool generates the metadata for a youtube video.
- The simple idea is that, you don't need to give any information if you don't want to. The AI agents will do it for you by transcribing the video and generating the metadata. But the more information you give, the better the AI agents can do their job, and the more processes you can work on in parallel.
- This process outputs a few files, the premetadata generation and the combined, finalized youtube title, description, and thumbnail.
- Over each generation, the AI Agents will have more information to work with, and the output will be better and better.
- Every prompt will optionally include each section of the metadata, and include whatever is available in their respective prompts.
- The metadata file looks like this.
  ```yaml
  title: "The Final Title"
  description: "The Final Description"
  thumbnail: "The Final Thumbnail"
  resources: "The Final Resources"
  chapters: "The Final Chapters"
  seo_keywords: "The Final SEO Keywords"
  ```
- `idt yt generate-meta`
  - System Flow
    - scans every dir in `yt.generate_meta.source_dirs` for new videos (last 24 hours)
    - prompts user to select video -> `video_file, video_file_title`
    - prompts user for rough draft title (skippable but highly recommended) -> `rough_draft_title?`
    - prompts user for SEO keywords comma sep (skippable but highly recommended) -> `seo_keywords?`
    - prompts user for thumbnail prompt (skippable but highly recommended) -> `thumbnail_prompt?`
      - with no initial prompt, we only have the `video_file_title` to work with
    - start transcribing video -> `transcription`
    - start generating thumbnails -> `thumbnails`
    - if there's nothing to do the cli will say 'loading... <"transcribing video": go between everything thats happening over a 2s interval>'
      - We'll probably want a loader here for the transcription that will show a rough percentage of completion based on current position of the transcription and the length of the video - if possible.
  - AI Agents
    - Title generator(video_file_title, rough_draft_title) -> `titles`
    - SEO keyword generator(seo_keywords,) -> `seo_keywords`





## The Configuration File
> The configuration file is the single source of truth for all the tools in the IndyDevTools suite.
>
> Located `~/.indydevtools/config.yml`

### Structure
```yaml
- idt:
    - models:
        - openai:
            - model: "gpt-4-turbo"
            - api_key: "sk-1234..."
- yt:
    - generate_meta:
        # Locations to look for newly renderered videos
        - source_dirs: ["~/Videos", "~/Downloads", "~/Desktop"]
        # Where to save the generated meta
        - output_dir: "~/Videos/yt-meta"
        - 
```













## Goal & Architecture
- Goal
    - Reduce time spent building YT Meta
        - Title
        - Thumbnail
        - Description
        - Resources
        - Chapters
        - SEO Keywords???
    - Beginning of IndyDevTools.
    - Well tested?
- Architecture
    - single yml file for configuration
    - a simple step by step cli that asks for:
        - rough draft title
        - seo
        - location of video
    - and that’s it - you can the ‘edit’ the configuration file or choose to start generating immediately



## Questions to answer
- Using the open-core business model - how can I separate the paid version from the free version without leaking the pro code?

## Local Dev Commands (excluded from dist)
- run locally
  - `poetry run idt`
- test versions
  - `poetry run python scripts/run_tox.py`
- publish to test pypi
  - `poetry run python scripts/publish_testpypi.py`
- publish to pypi
  - `poetry run python scripts/publish_pypi.py`

## Resources
- Chat with async + parralelzation + threading
  - https://chat.openai.com/c/73d1859d-fb3a-430e-9e04-be68b4d8a7bd
- Typer Docs For Multi Sub Commands
  - https://typer.tiangolo.com/tutorial/subcommands/add-typer/
- Python openai
  - https://github.com/openai/openai-python