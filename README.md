# IndyDevTools
> An Opinionated Agentic Engineering toolbox for developers powered by LLM Agents to solve problems autonomously.
>
> Applications: 
>   - Youtube Metadata Generation

![IndyDevTools Logo](/imgs/indydevtools.png)

## Table of Contents
- [IndyDevTools](#indydevtools)
  - [Table of Contents](#table-of-contents)
  - [Principles](#principles)
    - [\> USE THE RIGHT TOOL (AGENT) FOR THE JOB](#-use-the-right-tool-agent-for-the-job)
    - [\> EVERYTHING IS A FUNCTION](#-everything-is-a-function)
    - [\> GREAT QUESTIONS YIELD GREAT ANSWERS](#-great-questions-yield-great-answers)
    - [\> CREATE REUSABLE BUILDING BLOCKS](#-create-reusable-building-blocks)
    - [\> Prompts (Agents) are THE new fundamental unit of programming](#-prompts-agents-are-the-new-fundamental-unit-of-programming)
  - [Tools](#tools)
    - [📹 Multi Agent Youtube Metadata Generation (`idt yt`)](#-multi-agent-youtube-metadata-generation-idt-yt)
      - [Use case](#use-case)
      - [Get Started](#get-started)
      - [`yt` Commands](#yt-commands)
        - [`yt titles` Commands](#yt-titles-commands)
        - [`yt script` Commands](#yt-script-commands)
        - [`yt desc` Commands](#yt-desc-commands)
        - [`yt tags` Commands](#yt-tags-commands)
        - [`yt refs` Commands](#yt-refs-commands)
        - [`yt thumb` Commands](#yt-thumb-commands)
      - [Application Flow Diagram](#application-flow-diagram)
      - [`idt yt` Improvements / What's Next](#idt-yt-improvements--whats-next)
  - [The Configuration File](#the-configuration-file)
    - [Structure](#structure)
  - [Developer Commands](#developer-commands)
    - [Deploy](#deploy)
    - [Install](#install)
  - [Resources](#resources)


## Principles
> Principles drive decisions, decisions drive actions, actions drive results.
> Understanding the principles behind a tool will help you understand how to use it, and how to use it effectively.

### > USE THE RIGHT TOOL (AGENT) FOR THE JOB
- Every tool in this toolbox consists of one or more agents designed to solve a specific set of problems.
- Agent > Code > Manual Input
- CRUD/2 -> Prefer Create, Read over Update, Delete when using AI Agents

### > EVERYTHING IS A FUNCTION
- Every tool in this toolbox is a function that takes inputs and returns outputs.
- Every function can be called on it's own in isolation, or used in combination with other functions to create a more complex process.
- By treating every critical unit of code as a function, we can create a library of reusable building blocks that can be used to solve many problems.

### > GREAT QUESTIONS YIELD GREAT ANSWERS
- At the core of every product, there is a question that it attempts to answer.
- The quality of the answer is directly proportional to the quality of the question.
- IndyDevTools attempts to answer the question: **"What's the best way to build multi-agent systems that can solve problems autonomously on my behalf?"**
- The harsh truth is that the answer to your question is buried in questions, experiments, failed attempts, and iterations. IndyDevTools is an ongoing experiment to answer the question of how to build multi-agent systems that can solve problems autonomously on your behalf.

### > CREATE REUSABLE BUILDING BLOCKS
- In the age of AI where code, data, and models are becoming a commodity, the most valuable thing you can create is a reusable building block that can be used to solve many problems.
- Build small, composable, and reusable functions that can be used together, or only one at a time.

### > Prompts (Agents) are THE new fundamental unit of programming
- Just like loops, variables, and functions, we treat prompts as a fundamental unit of programming.
- In the age of AI, prompts are the most powerful way to design, build, and engineer systems that can solve problems autonomously on your behalf.
- They should be treated with the same level of respect (as time goes on, even more) and care as any other fundamental unit of programming.

## Tools
### 📹 Multi Agent Youtube Metadata Generation (`idt yt`)
- This tool generates the metadata for a youtube video.

#### Use case
- You've just finished rendering a video to upload to youtube, and you need to generate the metadata for the video. This tool will help you generate the title, description, tags, and thumbnail for the video.
- It's not meant to be a 100% replacement for your metadata, but it's meant to jump start you to 80% completion.
- The best command to run is `idt yt gen-meta-auto` which will walk you through key steps to generate the metadata for your video. It will
  - Transcribe the video
  - Prompt you for key information like
    - Rough Draft Title
    - SEO Keywords
    - How many iterations of the title, description, and thumbnail you want to generate
  - Generate multiple titles, descriptions, and thumbnails for you to choose from
  - The description will combine the hashtags, references, and the description
  - Generate the final metadata for you to upload to youtube
  - In addition to outputting these assets to the `final/` directory, it will also output the drafts to the `drafts/` directory so you can review them and make any changes if necessary.
- The goal is to make it as easy as possible to generate the metadata for your video, and to make it as easy as possible to make changes to the metadata if necessary.

#### Get Started
1. Install IndyDevTools
    ```bash
    pip install indydevtools
    ```
2. View and initialize the configuration file
    ```bash
    idt yt config
    ```
    - Should print something like
      ```yml
      yt:
        config_file_path: <path to this config file for you to open and edit>
        openai_api_key: <your openai api key will fallback to env var OPENAI_API_KEY>
        operating_dir: <Path to your rendered video/audio, also the output path where the assets that will be generated>
      ```
    - This will create the configuration file if it doesn't exist and the `/drafts` and `/final` directories in the operating directory.
3. Edit the configuration file to add your openai key and path to your audio/video files
4. Run a test command
    ```bash
    idt yt thumb create -p "bird writing code"
    ```
    or
    ```bash
    idt yt titles create -r "Using AI Coding Assistants to code faster than ever"
    ```
5. Make sure the thumbnail was created in the `<config.yt.operating_dir>/drafts` directory
6. Run the full metadata generation command
    ```bash
    idt yt gen-meta-auto
    ```
7. See [Commands](#yt-commands) for more information

#### `yt` Commands
  - `idt yt --help` 
    - view all available commands
  - `idt yt config`
    - Dump the configuration file to the console, creates the file if it doesn't exist
##### `yt titles` Commands
  - `idt yt titles create -r <rough_draft_title> -s? <script_file.txt> -c? <count> -k? <seo_keywords>`
    - Generate a title for a youtube video
    - Inputs
      - `-r`: The rough draft title
      - `-s` (optional): The script file to use
      - `-c` (optional, default `1`): The number of titles to generate
      - `-k` (optional): The SEO keywords
    - Outputs
      - A file with the generated titles in `<config.yt.operating_dir>/drafts/titles.json`
##### `yt script` Commands
  - `idt yt script transcribe --file <video_file> --json? <create_json_file> --seconds? <duration_limit_in_sec>`
    - Transcribe the audio of a video file into text.
    - Inputs
      - `-f`: The path to the video file to transcribe.
      - `-j` (optional, default `False`): Create an additional JSON file of the transcript with segments and word timestamps.
      - `-s` (optional, default `120`): The maximum seconds to process.
    - Outputs
      - A transcript of the video's audio. If `-j` is used, a JSON file with the transcript will be created in the `<config.yt.operating_dir>/transcripts` directory.
##### `yt desc` Commands
  - `idt yt desc compose`
    - Compose a description given a completed draft directory.
    - Inputs
      - `<config.yt.operating_dir>/draft/descriptions.json`
      - `<config.yt.operating_dir>/draft/hashtags.json`
      - `<config.yt.operating_dir>/draft/references.txt` (optional)
    - Outputs
      - The finalized description ready for youtube in `<config.yt.operating_dir>/final/description.txt`
  - `idt yt desc create -s <script_file> -r? <rough_draft_title> -c? <count> -k? <seo_keywords>`
    - Create a new description for a video.
    - Inputs
      - `-s`: The path to the script file.
      - `-r` (optional): The rough draft title of the video.
      - `-c` (optional, default `3`): The number of descriptions to generate.
      - `-k` (optional): SEO keywords to be included in the description.
    - Outputs
      - A file with the generated descriptions in `<config.yt.operating_dir>/drafts/descriptions.json`
  - `idt yt desc iterate <prompt> <description>`
    - Iterate over the description to improve it. (Note: This command is currently not implemented.)
##### `yt tags` Commands
  - `idt yt tags compose`
    - Compose the final set of hashtags for a video.
    - Inputs
      - `/draft/hashtags.json`
    - Outputs
      - Finalized `/final/hashtags.txt` with a list of tags to use in the video.
  - `idt yt tags create --title <rough_draft_title> --keywords <seo_keywords>`
    - Generate hashtags for a video (list of 10 comma sep, and top three).
    - Inputs
      - `--r`: The rough draft title of the video.
      - `--k`: The SEO keywords for the video.
    - Outputs
      - Tags and top three hashtags for the video output to `/draft/hashtags.json`.
##### `yt refs` Commands
  - `idt yt refs format -r <references> -t <rough_draft_title> -k? <seo_keywords>`
    - Format the references for a video.
    - Inputs
      - `-r`: The references (links) to format.
      - `-t`: The rough draft title of the video.
      - `-k` (optional): The SEO keywords for the video.
    - Outputs
      - Formatted references output to `/draft/references.txt`.
##### `yt thumb` Commands
  - `idt yt thumb compose`
    - Compose the final thumbnail for a video.
    - Inputs
        - `/draft/thumbnail_<count>.png`
    - Outputs
        - Finalized `/final/thumbnail.png` thumbnail to use in the video.
  - `idt yt thumb create_from_prompt -c <count>`
    - Create thumbnails from a generated prompt.
    - Inputs
        - `-c`: The number of thumbnails to create from a selected prompt.
    - Outputs
        - `/drafts/thumbnail_<count>.png` thumbnail drafts to potentially use in the video.
  - `idt yt thumb create_prompt -r <rough_draft_title> -k <seo_keywords> -c <count> -a <art_style>`
    - Create a prompt for generating a thumbnail.
    - Inputs
        - `-r`: The rough draft title of the video.
        - `-k`: The SEO keywords for the video.
        - `-c`: The number of thumbnail prompts to create.
        - `-a`: The art style to be used in the thumbnail.
    - Outputs
        - `/draft/thumbnail_prompt.json` with the generated thumbnail prompts.
  - `idt yt thumb create -p <prompt> -c <count>`
    - Create an image with the specified prompt and download it.
    - Inputs
        - `-p`: The prompt to create thumbnail with.
        - `-c`: The number of thumbnails to create.
    - Outputs
        - `/draft/thumbnail_<count>.png` thumbnail drafts to potentially use in the video.
  - `idt yt thumb rescale -f <image_file_path> -w <width> -h <height> -o <output_file>`
    - Rescale an image to the specified width and height. Defaults to youtube thumbnail size.
    - Inputs
        - `-f`: The path to the input image file.
        - `-w` (default 1280): The width to rescale the image to.
        - `-h` (default 720): The height to rescale the image to.
        - `-o` (default input file path): The path to the output image file.
    - Outputs
        - The rescaled image saved to the specified output file.

#### Application Flow Diagram

```mermaid 
graph LR
Z[Rendered YouTube Video]

subgraph Youtube Metadata Automation Tool
    A[Generate Youtube Metadata]
    B(Transcribe - CODE)
    C{Script Ready}
    D(Generate Title - LLM AGENT)
    E(Generate Description - LLM AGENT)
    F(Generate Thumbnails - LLM AGENT)
    G(Resize Thumbnails - CODE)
    H{Title Ready}
    I{Description Ready}
    K{Resized Thumbnails Ready}
    L[[Review for Upload - MANUAL INPUT]]
    N(Format References - CODE)
    O{References Ready}
    P(Generate Hashtags - LLM AGENT)
    Q{Hashtags Ready}
    R(Compose Hashtags - CODE)
    S(Compose Description - CODE)
    T(Compose Title - CODE)
    U(Compose Thumbnail - CODE)
end

M[Upload to YouTube]

Z --> A
A --> B
B --> C
C --> D
C --> E
A --> F
F --> G
A --> B
D --> H
E --> I
G --> K
L --> M
A --> N
N --> O
A --> P
P --> Q
O --> S
R --> L
S --> L
T --> L
U --> L
I --> S
H --> T
K --> U
Q --> R
Q --> S
```

#### `idt yt` Improvements / What's Next
- [] Stream text responses and print them to the console as they come in.
- [] Add support for Gemini models
- [] Create 'Trending' agents to find topics that are trending based on a few keywords
  - `idt yt trending -k <keywords> -n <number of results>`
- [] Create SEO Keyword Agent that can generate SEO keywords for a video based on a topic or the script
  - `idt yt script research -t <topic> -s <script file> -n <number of results>`
- [] Add logging so we can see where the log is coming from (what file + function)
  - https://chat.openai.com/c/d2ae52f4-0706-4cec-b047-3364bea3bd05
- [] Add 'tone' to description to reduce buzzwordyness
- [] Implement `thumb iterate` to improve an image
- [] Implement `desc iterate` to improve a description
- [] Implement `titles iterate` to improve a description
- [] Make the code run in parallel, right now it's running one by one, this is inefficient
- [] Add a loader to let users know which state the application is in

## The Configuration File
> The configuration file is the primary source of truth for all the tools in the IndyDevTools suite.

### Structure
```yaml
yt:
  config_file_path: <path to this config file for you to open and edit>
  openai_api_key: <your openai api key will fallback to env var OPENAI_API_KEY>
  operating_dir: <Path to your rendered video/audio, also the output path where the /draft and /final assets that will be generated>
```

## Developer Commands
(deploy, publish)

### Deploy
- Bump version in `pyproject.toml: version`
- publish to test pypi
  - `poetry run python scripts/publish_testpypi.py`
- publish to pypi
  - `poetry run python scripts/publish_pypi.py`

### Install
- Install bleeding edge test version from [TestPyPi](https://test.pypi.org/)
  - `pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple indydevtools`
- Install public version from [PyPi](https://pypi.org/)
  - `pip install indydevtools`

## Resources
- Chat with async + parralelzation + threading
  - https://chat.openai.com/c/73d1859d-fb3a-430e-9e04-be68b4d8a7bd
- Typer Docs For Multi Sub Commands
  - https://typer.tiangolo.com/tutorial/subcommands/add-typer/
- Python openai
  - https://github.com/openai/openai-python