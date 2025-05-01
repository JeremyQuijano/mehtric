# mehtric
```
                 _     _    
                | |   | |     
  _ __ ___   ___| |__ | |_ _ __ _  ___ 
 | '_ ` _ \ / _ \ '_ \| __| '__| |/ __|
 | | | | | |  __/ | | | |_| |  | | (__ 
 |_| |_| |_|\___|_| |_|\__|_|  |_|\___|
```

**Mehtric** is a custom interpreted programming language written in Python using the [SLY](https://github.com/dabeaz/sly) (Sly Lexer and Parser) library. It supports variables, arithmetic expressions, strings, comparison operators, and REPL interaction. We followed the tutrial from [GeeksForGeeks](https://www.geeksforgeeks.org/how-to-create-a-programming-language-using-python/) to implement our lexer, parser, interpreter, and main files.

## Features

- Integer and string literals
- Arithmetic operations: `+`, `-`, `*`, `/`, `%`, `**`
- String concatenation with `+`
- Variable assignment and usage
- Comparison operators: `==`, `!=`, `<`, `<=`, `>`, `>=`
- Built-in functions: `help`, `quit`, `clear`, etc.
- Reserved keywords handling
- Error types and messages
- REPL (interactive shell)

## Example Usage

```mehtric
>>> x = 10
>>> y = 5
>>> x + y
15
>>> name = "meh"
>>> "Hello, " + name
Hello, meh
>>> quit
```

## Getting Started

1. **Install dependencies**:
   ```bash
   pip install sly
   ```

2. **Run the interpreter**:
   ```bash
   python mehtric.py
   ```

## File Structure

- `mehtric_main.py` — main entry point for the language interpreter
- `mehtric_lexer.py` — defines the lexical tokens using SLY
- `mehtric_parser.py` — defines grammar and parsing rules
- `mehtric_interpreter.py` — walks the parsed AST and evaluates expressions
- `README_mehtric.md` — project documentation

## Roadmap

- [ ] Add support for user-defined functions
- [ ] Add list and dictionary types
- [ ] Implement control flow (`if`, `while`, etc.)
- [ ] Add import/module system

## License

MIT License.
