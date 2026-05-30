# Compiler Sessional Lab Assignments

![Language](https://img.shields.io/badge/Language-Python%20%7C%20Flex%20%7C%20Bison-blue)
![Course](https://img.shields.io/badge/Course-Compiler%20Sessional-green)

## Repository Structure

| Lab No | Lab Name                           |
| ------ | ---------------------------------- |
| 01     | Regular Expression Matching        |
| 02     | SLR Parser                         |
| 03     | Predictive Parser                  |
| 04     | LALR Parser                        |
| 05     | LEX Program Conversion (Substring) |

---

## Lab 01: Regular Expression Matching

### Objective

Implement pattern matching using Regular Expressions.

### Technologies

* Python
* Regex (`re` module)

### Input Example

```text
ab*c*d
acccd
```

### Output Example

```text
YES, 1
```

---

## Lab 02: SLR Parser

### Objective

Design and implement an SLR Parser.

### Grammar

```text
E → E + T | T
T → id
```

### Sample Input

```text
id + id
```

### Sample Output

```text
ACCEPTED
```

---

## Lab 03: Predictive Parser

### Objective

Implement Recursive Descent / Predictive Parsing.

### Grammar

```text
E  → T E'
E' → + T E' | ε
T  → F T'
T' → * F T' | ε
F  → ID | (E)
```

### Sample Input

```text
ID*ID
```

### Sample Output

```text
valid string
```

---

## Lab 04: LALR Parser

### Objective

Implement arithmetic expression parsing using Flex and Bison.

### Supported Operations

| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| *        | Multiplication |
| ()       | Parentheses    |

### Sample Input

```text
2+3*4
```

### Sample Output

```text
14
```

---

## Lab 05: LEX Program Conversion (Substring)

### Objective

Replace occurrences of `abc` with `ABC`.

### Sample Input

```text
abc xyz abcdef
```

### Sample Output

```text
ABC xyz ABCdef
```

---

## Technologies Used

| Tool         | Purpose                              |
| ------------ | ------------------------------------ |
| Python       | Regex, SLR Parser, Predictive Parser |
| Flex (LEX)   | Lexical Analysis                     |
| Bison (YACC) | Syntax Analysis                      |
| Git          | Version Control                      |
| GitHub       | Repository Hosting                   |

---

## Course Topics Covered

* Lexical Analysis
* Regular Expressions
* Predictive Parsing
* SLR Parsing
* LALR Parsing
* Flex & Bison
* Compiler Design Fundamentals

---

## Author

**Compiler Sessional Lab Report**

Department of Computer Science & Engineering (CSE)
