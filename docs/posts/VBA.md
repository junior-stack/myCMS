---
date:
    created: 2026-04-16
draft: true
tags:
  - Finance
---
My note about VBA
<!-- more -->

# 1. ADO connect
DB platforms ADO can connect: https://www.connectionstrings.com/
## 1.1 Connect to AccessDB
https://www.youtube.com/watch?v=U_Eahf6O59Q

https://www.youtube.com/watch?v=ND2eE3g-yDs

## 1.2 Connect to PostgreSQL/MySQL
https://www.youtube.com/watch?v=Hs6ALekQ0AM


# 2. Connect to Application(COM)

word, outlook, access, google drive

word: https://www.youtube.com/watch?v=qeEkOW7gX-M

outlook: https://www.youtube.com/watch?v=07wGZ6_5-HE

# 3. Formula

convert text to numerical:

| formula                           | desc                                                                                                                                                                                                                               |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| concat(A1, " ", B1)               | concatenate two columns entry values                                                                                                                                                                                               |
| `left(A1, [num_chars])`           | extracts a specified number of chars from the start of the text                                                                                                                                                                    |
| `value`                           | convert text-formatted strings into corresponding types,<br>`=VALUE("100")` returns `100`;<br>`=VALUE("$125.50")` returns `125.5`;<br>`=VALUE("12:00")` returns a serial number for time (0.5); `=VALUE("Text")` returns `#VALUE!` |
| `mid(A1, 9, 6)`                   | extract 6 char from the 9th position of the text                                                                                                                                                                                   |
| `substitute([string], "rpm", "")` | replace the rpm in string with empty string                                                                                                                                                                                        |
|                                   |                                                                                                                                                                                                                                    |

Join table in different sheets:

| formula                                 | desc                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `vlookup(A2, "Sheet2"!$A$2:$D$18, 2,1)` | It scans the first column of table range `"Sheet2"!$A$2:$D$18` to find the row that has A2 value. It then returns the `2` nd column from that table range of that row. The last argument `exact_match` is either 1 or 0.<br><br>If 0, the function fails if the value isn't there<br>if 1, the function finds approximate match if exact match is missing |
| Xlookup                                 |                                                                                                                                                                                                                                                                                                                                                           |
| Filter                                  |                                                                                                                                                                                                                                                                                                                                                           |

# 4. Pivot table
What is a pivot table:
It's a summary table that shows the max, min, sum, avg of a numerical field for each group of a categorical field

- create pivot table: select all of the data entries, Insert > pivot table > From table/range

# 5. Plot