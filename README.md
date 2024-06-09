# Mad Libs Story Generator

This repository contains a Python script to generate a custom story based on user input. The script reads a template story from a file, identifies placeholders for specific parts of speech (adjective, noun, verb, etc.), and replaces them with words provided by the user.

## How It Works

1. **Reading the Template:**
   The script reads a story template from a file called `story.txt`. The template contains placeholders in the format `<adjective1>`, `<noun1>`, etc.

2. **Identifying Placeholders:**
   The script scans the template to find all unique placeholders enclosed in angle brackets (`<` and `>`).

3. **User Input:**
   For each placeholder, the script prompts the user to enter a word that matches the part of speech indicated by the placeholder.

4. **Generating the Story:**
   The script replaces each placeholder in the template with the corresponding word provided by the user and prints the final story.

## Usage

1. **Prepare the Template:**
   Create a file named `story.txt` in the same directory as the script. The file should contain the story template with placeholders for parts of speech.

2. **Run the Script:**
   Execute the script using Python. The script will prompt you to enter words for each placeholder and will then print the completed story.

## Example

### Template (`story.txt`):

In a <adjective1> town, a <noun1> decided to <verb1> a <adjective2> <noun2>. Everyone was <adjective3> to see the <noun2> <verb2>. 
It became the most <adjective1> event in town, with people <verb3> and <verb2> in amazement.

(Note: this is a sample template using ChatGPT, the story can be changed to fit individual needs)

## Requirements

- Python 3.x

## Running the Script

1. Ensure you have Python 3.x installed on your system.
2. Place your story template in a file named `story.txt` in the same directory as the script.
3. Run the script:

```sh
python mad_libs.py
