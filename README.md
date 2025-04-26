# ✏️ Simple Text Editor

A lightweight command-line text editor tool for creating, viewing, and editing text files.

## ✨ Features

- 📝 Create new text files with optional templates
- ✏️ Edit files using your preferred system editor
- 👀 View file contents right in the terminal
- ℹ️ Get information about text files (size, dates, line count)
- 📄 Support for line numbers when viewing files
- 🧩 Multiple templates for different purposes (notes, to-do lists, memos)

## 🚀 Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/simple-text-editor.git
cd simple-text-editor
```

2. Make the script executable (Unix/Linux/macOS):
```bash
chmod +x main.py
```

## ⚙️ Commands

- `create`: Create a new text file
- `edit`: Edit a text file
- `view`: View a text file
- `info`: Get information about a text file

## 📋 Command Options

### Create a file:
```bash
python main.py create <file_path> [options]
```

#### Options:

- `-t, --template`: Template to use (blank, note, todo, memo)

### Edit a file:
```bash
python main.py edit <file_path>
```

### View a file:
```bash
python main.py view <file_path> [options]
```

#### Options:

- `-n, --line-numbers`: Show line numbers

### Get file information:
```bash
python main.py info <file_path>
```

## 📝 Examples

### Create files with different templates:

```bash
# Create a blank file
python main.py create document.txt
```

```bash
# Create a note with timestamp
python main.py create notes/meeting.txt -t note
```

```bash
# Create a to-do list
python main.py create todo.txt -t todo
```

```bash
# Create a memo
python main.py create memo.txt -t memo
```




