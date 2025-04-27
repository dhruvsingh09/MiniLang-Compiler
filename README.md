MiniLang Compiler
A simple compiler pipeline built in Python that demonstrates the stages of Lexing, Parsing, Code Generation, and Interpretation for a minimal programming language (MiniLang).
It also includes a Tkinter-based GUI for easier interaction and visualization.

✨ Features
Lexer: Tokenizes the input source code.

Parser: Converts tokens into an Abstract Syntax Tree (AST).

Code Generator: Produces simple stack-based instructions.

Interpreter: Executes the generated instructions.

GUI: Built with Tkinter — view the output of each phase separately.

📁 Project Structure
bash
Copy
Edit
.
├── lexer.py          # Lexer: Breaks source code into tokens
├── parser.py         # Parser: Builds AST from tokens
├── codegen.py        # Code Generator: Converts AST to instructions
├── main.py           # GUI Application: Compiler pipeline + Tkinter interface
└── README.md         # Project description (you are here)



🛠️ How to Run
Clone the repository (or download the files).

Install requirements:
(Only tkinter, which comes pre-installed with Python in most cases.)
  If needed:
  pip install tk
Run the compiler:
  python main.py

🧠 MiniLang Language Syntax
Supports:

Variable Assignment:

plaintext
Copy
Edit
x = 5 + 3;
y = x * 2;
Printing:

plaintext
Copy
Edit
print(x);
print(y);
Operators:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Comments:

Single-line comments using // (ignored by lexer).

Parentheses for Grouping:

plaintext
Copy
Edit
x = (5 + 3) * 2;
📋 Example
Input code:

plaintext
Copy
Edit
x = 5 + 2 * 3;
y = x - 4;
print(y);
Lexer Output: List of tokens

Parser Output: Abstract Syntax Tree (AST)

CodeGen Output: Stack-based instructions

Interpreter Output: Result printed (7)

🖥️ GUI Overview
The application has four main tabs:


Tab	Description
Lexer	Shows tokens generated from source code.
Parser	Displays the AST.
Code Gen	Lists generated instructions.
Interpreter	Executes instructions and displays results.
You can easily compile or clear the workspace with buttons.

🚀 Future Improvements (Ideas)
Add support for if statements and loops.

Support floating-point numbers.

Add error recovery for parsing mistakes.

Improve interpreter with a real environment stack.

Syntax highlighting in the editor.

📚 Requirements
Python 3.x

Tkinter (comes with Python)

🤝 Credits
This project was built for educational purposes — to understand and demonstrate the basics of compilers:
Lexer ➔ Parser ➔ Code Generator ➔ Interpreter

