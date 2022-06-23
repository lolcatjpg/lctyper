# lctyper
a simple command-line tool for writing a chunk of text multiple times, automatically 

## More detailed explanation
You can use this script to automatically write a single or multiple lines of text in rapid succession.
The amount of times the program writes the text is configurable.
You can choose to pass the text to write as a command line argument, to write text from a file or from a URL.  
  
The program has currently only been tested on Windows, but it might work on Linux and macOS.  

Windows will probably tell you the file might be harmful, since it does not have a certificate and I do not have any understanding on how this certificate stuff works. If you want, you can package the file yourself (with pyinstaller or a similar tool).

## Usage
First, focus the program you want to write text in, then, immediately after, focus the terminal. 
(The script presses alt+tab right before typing your text, to focus back on the application you want to type in. This behavior is configurable.)

#### To type text fom a command line argument:
```shell
lctyper text "your text"
```

#### To type text from a file:
```shell
lctyper file "path/to/file"
```
This wil type every line of text from the file as a separate file.

#### To type text from a URL:
```shell
lctyper url https://url
```
This wil send a request to the URL and type out the raw response body, line per line.
It is best to use this with pure text pages (like pastebin.com/raw/...).  
You have to enter the full url (with `http://` or `https://`).

### Other arguments
`-i, --iterations [iterations]`: Controls the amount of times the text will be typed. (default: 1)  
`-d, --delay [delay in seconds]`: Controls the amount of time between lines and between iterations in seconds. (default: 0.05)  
`--no-alt-tab`: Stops the script from pressing alt+tab to switch application focus before starting to type. 
It is recommended to use this in conjunction with the `--countdown` flag.  
`--countdown [countdown in seconds]`: Makes the script count down before starting to type. This cannot be a decimal number.  
`--debug`: Prints debug info to the terminal.

## Disclaimer
This program is provided without any warranty of any kind. I cannot be held responsible for any consequences you might encounter by the use of this program.
