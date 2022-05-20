import sys
import keyboard
import argparse
import requests
import colorama as cla
from time import sleep


def write(text):
    if args.debug:
        print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] Write text: {text}")
    keyboard.write(text)
    if keyboard.is_pressed("shift"):
        print(f"{cla.Fore.YELLOW}Interrupted. The program will exit.{cla.Style.RESET_ALL}")
        sys.exit(0)


def write_text_from_file(source_file):
    if args.debug:
        print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] Writing from file: {source_file}")
    with open(source_file, "r") as file:
        for line in file:
            write(line)
            sleep(args.delay)


def write_list(_list):
    if args.debug:
        print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] List to write: {_list}")
    for item in _list:
        write(item)
        keyboard.send("enter")
        sleep(args.delay)


def main():
    if args.debug:
        print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] args: {args}")

    # switch to previous application
    if not args.no_alt_tab:
        keyboard.send("alt+tab")
        if args.debug:
            print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] Switched to previously focused application")
        sleep(.1)

    # countdown
    if args.countdown > 0:  # if to prevent random newline when countdown = 0
        for i in range(args.countdown):
            print(f"\r> Typing in {cla.Fore.CYAN}{args.countdown - i}{cla.Style.RESET_ALL}          ", end="", flush=True)
            sleep(1)
        print()
    print(f"{cla.Back.LIGHTYELLOW_EX}{cla.Fore.BLACK}Hold shift to terminate{cla.Style.RESET_ALL}")

    # determine source type and do stuff accordingly
    if args.source_type == "text":
        for i in range(args.iterations):
            if args.debug:
                print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] Starting iteration {i}")
            write(args.source)
            keyboard.send("enter")
            sleep(args.delay)

    elif args.source_type == "file":
        for i in range(args.iterations):
            if args.debug:
                print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] Starting iteration {i}")
            write_text_from_file(args.source)
            keyboard.send("enter")

    elif args.source_type == "url":
        text = requests.get(args.source).text.splitlines()
        for i in range(args.iterations):
            if args.debug:
                print(f"[{cla.Fore.YELLOW}debug{cla.Style.RESET_ALL}] Starting iteration {i}")
            write_list(text)

    # indicate when finished
    print(f"{cla.Fore.GREEN}Finished{cla.Style.RESET_ALL}")


if __name__ == '__main__':
    cla.init()

    arg_parser = argparse.ArgumentParser(description="Program that automatically types text. Made by lolcatproductions")

    # source args
    arg_parser.add_argument("source_type", choices=["text", "file", "url"], help="Source type: what kind of source to get text from")
    arg_parser.add_argument("source", help="Where to get text from / what text to type (if source type is text)")

    # options
    arg_parser.add_argument("-i", "--iterations", type=int, default=1, help="How many times to type the input (default: 1)")
    arg_parser.add_argument("-d", "--delay", type=float, default=.05, help="Delay between iterations/lines in seconds (default: 0.05)")

    # extra args
    arg_parser.add_argument("--no-alt-tab", action="store_true", help="Don't switch to previous application before typing. "
                                                                      "It is strongly recommended to use the --countdown flag when using this flag.")
    arg_parser.add_argument("--countdown", type=int, default=0, help="From where to count down to before typing (default: 0)")
    arg_parser.add_argument("--debug", action="store_true", help="Print some debug info")

    args = arg_parser.parse_args()

    main()