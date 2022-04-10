## Introduction

This is a project to translate the Phantasy Star Text Adventure from english to portuguese, but could be used to translate to any other language. This series has 8 chapters and the structure of each game are very similar between them, so the code is shared whenever possible.

To be able to run the code and build the binaries you need the following tools:

- ***Python***: Here I'm using python 3.9, but could be any version from 3.6+
- ***Bass Assembler***: This is the assembler I use to build the assembly code (if any) and to insert the binaries. It needs to be in your PATH.

Below is the *Bass* repository where you can download the compiled binaries for Windows:

```
https://github.com/Dgdiniz/bass
```

If you are using Linux or Mac you can easily compile Bass only running *make*.

*Bass* needs to be in your PATH. If you don't know how to do this, what this video (in portuguese):

[https://youtu.be/rgt7bDrmv3o](https://youtu.be/rgt7bDrmv3o)

## Folders

Here is describe the meaning of each folder:

### Folder extract

This folder contains the code for extracting the script for all the chapters. For now only the *Amia* chapter is implemented. The extracted script goes to the *scripts* folder.

### Folder games

In this folder you need to put all the eight chapters. The names are:

- amia.bin

So for now only the *Amia* chapter is implemented.

Puting the binaries here is mandatory, because the code needs to load each chapter. Where you can find the chapters is up to you.

## Folder insert

Here is located the code that use the translated scripts and generate the binaries blocks for the dialogs and pointers. These object will be writen to the *obj* folder.

## Folder obj

This folder will contain the temporary dialogs and pointers blocks that will be inserted in the final translated chapters.

## Folder scripts

Here is where the scripts for each chapter are located. These are the files we need to translate from english to any other language.

## Folder table

Here we have the *table* file that converts the Latin-1 charecteres to the game encoding.

## Table translated

Here is where all the final translated chapters will be located. 

## How to build each chapter?

To build a specific chapter just run the corresponding ***.bat*** file to call the insertion code and the assembler to build the final binary.

For example run the *amia_build.bat* to translate the *Amia* chapter.

## What is missing?

- Only the Amia chapter is currently implemented.
- The insertion is partially working, because we still need to insert the line breaks. This requires to find the vwf (variable width font) to find the caracter widths, so we can insert the line breaks in the correct location.
- Need to add the accents in the font. This seems to be the hardest part because the whole font is loaded to Vram and there is no space for more letters.
- Still need to translate all the graphics.
- I want to insert the google translation step on the extraction, so the focus goes to the revision phase.