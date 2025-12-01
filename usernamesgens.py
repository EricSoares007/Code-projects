#!/usr/bin/env python3
import argparse
import random
import os

def generate_usernames(words, num_usernames=50):
    usernames = set()
    symbols = ["", "_", ".", "-", ""]
    while len(usernames) < num_usernames:
        combo = random.sample(words, random.randint(2, min(4, len(words))))
        base = "".join(random.choice(symbols).join(combo).title())
        number = str(random.randint(0, 9999)) if random.random() > 0.5 else ""
        username = (base + number).lower()
        usernames.add(username)
    return list(usernames)

def get_input_list():
    print("Enter words separated by commas (e.g., John, Pizza, Loki, Gaming):")
    items = input("> ").strip().split(",")
    return [item.strip() for item in items if item.strip()]

def main():
    parser = argparse.ArgumentParser(description="Custom Username Generator Tool")
    parser.add_argument("--words", help="Comma-separated list of base words (e.g. John,Pizza,Loki)")
    parser.add_argument("--count", type=int, default=50, help="Number of usernames to generate (default: 50)")
    parser.add_argument("--output", default="usernames.txt", help="Output filename (default: usernames.txt)")
    parser.add_argument("--interactive", action="store_true", help="Run interactively to input words manually")
    args = parser.parse_args()

    if args.interactive:
        words = get_input_list()
    elif args.words:
        words = [w.strip() for w in args.words.split(",") if w.strip()]
    else:
        print("❌ No words provided. Use --words or --interactive.")
        return

    if len(words) < 2:
        print("Please provide at least two words.")
        return

    usernames = generate_usernames(words, args.count)

    with open(args.output, "w", encoding="utf-8") as f:
        for name in usernames:
            f.write(name + "\n")

    print(f"\n✅ Generated {len(usernames)} usernames.")
    print(f"📁 Saved to: {os.path.abspath(args.output)}")

if __name__ == "__main__":
    main()

