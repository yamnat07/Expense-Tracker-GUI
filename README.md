# Expense Tracker

A simple desktop application for recording daily expenses, built with Python and tkinter. Enter an expense, and it is saved to a text file and shown immediately in a scrollable table.

This project was created as a learning exercise in Python, tkinter, input validation, and basic file handling.

## Features

- Add an expense with a **date**, **category**, **amount (in rupees)**, and a short **description**
- Choose the date from day, month, and year dropdowns
- Choose from 13 categories: Food, Travel, Shopping, Bills, Entertainment, Education, Health, Rent, Groceries, Utilities, Subscriptions, Personal Care, and Other
- Input validation with clear warning messages
- Every expense is appended to a text file (`expense_data.txt`)
- Expenses are displayed in a table with a vertical scrollbar, so any number of entries can be viewed
- Dark-themed interface that opens maximized

## Interface

The window opens maximized with a dark charcoal background, light text, and green accents. The title **Expense Tracker** appears at the top, and the screen is split into two sides.

**Left side: the entry form**

1. **Date** with three dropdowns (day, month, year)
2. **Category** dropdown
3. **Amount (Rs.)** text field
4. **Description** multi-line text box
5. A green **Add Expense** button

**Right side: the expense table**

- Columns: **Date**, **Category**, **Amount (Rs.)**, **Description**
- Green column headers and a highlighted (green) selected row
- A vertical scrollbar attached to the right edge of the table, which becomes useful once the table holds more rows than fit on screen

## What to Expect When Using It

1. Fill in every field and click **Add Expense**.
2. The expense is written to `expense_data.txt`, added as a new row in the table, and a confirmation message is shown.
3. The category, amount, and description fields are cleared, ready for the next entry.
4. The date stays selected on purpose, because several expenses are often recorded on the same day.

### Validation rules

- All fields are required.
- The date must be a real calendar date (for example, 31 February is rejected).
- The amount must be a positive whole number, with no decimals and no leading zeros.
- The description cannot be empty.

If something is wrong, a warning message explains what to fix, and nothing is saved.

## Requirements

- **Python 3.12 or newer** (the code uses an f-string syntax that older versions do not support)
- **tkinter**, which is included with the standard Python installer on Windows
- No third-party packages are needed

## How to Run

1. Download `expense-tracker-gui.py`.
2. Open a terminal in the folder containing the file.
3. Run:

```
python expense-tracker-gui.py
```

### Keyboard shortcuts

| Key | Action |
|---|---|
| `Alt + Enter` | Switch to full-screen mode |
| `Esc` | Leave full-screen mode |

## Data Storage

Expenses are appended to `expense_data.txt` in the folder you run the program from. An empty copy of this file is included in the repository, and the app adds each new expense to the end of it. If the file is missing, the app creates it automatically. Keep it in the same folder as `expense-tracker-gui.py`. Each expense is saved as one block:

```
Date=5/May/2026
Category=Food
Amount Spend=250
Desc.=Tea and snacks

```

Line breaks in a description are replaced with spaces so each entry stays readable.

## Known Limitations

- Previously saved expenses are **not** loaded back when the app starts. The table shows only the expenses added during the current session, while the text file keeps the full history.
- Expenses cannot be edited or deleted from within the app.
- Amounts are whole rupees only (no paise).
- The year dropdown covers 2026 to 2047.
- Developed and tested on Windows with Python 3.14. The maximized startup window and the Segoe UI font are Windows-oriented, so other operating systems may need small adjustments.

## Possible Future Improvements

- Load saved expenses from the file when the app starts
- Show a running total of money spent
- Delete or edit a selected expense
- Preselect today's date on startup
- Store data in CSV or JSON format

## AI Assistance Disclosure

AI tools were used during this project, and this section describes how.

- **Claude** (by Anthropic) and **ChatGPT** (by OpenAI) were used for design suggestions, ideas, and guidance.
- Claude was also used for code review, debugging help, explanations of tkinter concepts, and example snippets for parts of the interface, such as the table styling and scrollbar.
- AI tools were used to work faster and to get guidance while learning, which reflects how these tools are commonly used in software development today.
- The application was assembled, adapted, and tested by the author. Suggestions and snippets from AI tools were reviewed and adjusted before being used, and the author is responsible for the final code.

## Author

**Tanmay Grover**

GitHub: [yamnat07](https://github.com/yamnat07)
