path_to_file = "books/frankenstein.txt"

def print_text(text):
  print(text)

def count_words(text):
  words = text.split()
  return len(words)

def count_characters(text):
  text = text.lower()
  allowed_chars = set("abcdefghijklmnopqrstuvwxyz")
  char_count = {}
  for char in text:
    if char in allowed_chars:
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1
  return char_count

def sort_dict_by_value(d):
  return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

def main():
  # Read the file
  with open(path_to_file, "r") as file:
    text = file.read()
  
  # Generate the report
  report_lines = []
  report_lines.append(f"--- Begin report of {path_to_file} ---")
  report_lines.append(f"{count_words(text)} words found in the document\n")
  
  char_count = sort_dict_by_value(count_characters(text))
  
  for char, count in char_count.items():
    report_lines.append(f"The '{char}' character was found {count} times")
  
  report_lines.append("--- End report ---")
  
  # Print the report
  for line in report_lines:
    print(line)

main()