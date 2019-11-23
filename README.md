**Metaheuristic Optimization**\
**Satisfiability Checker**

In computer science, the Boolean satisfiability problem (sometimes called propositional satisfiability problem and abbreviated SATISFIABILITY or SAT) is the problem of determining if there exists an interpretation that satisfies a given Boolean formula. In other words, it asks whether the variables of a given Boolean formula can be consistently replaced by the values TRUE or FALSE in such a way that the formula evaluates to TRUE. If this is the case, the formula is called satisfiable. On the other hand, if no such assignment exists, the function expressed by the formula is FALSE for all possible variable assignments and the formula is unsatisfiable. For example, the formula "a AND NOT b" is satisfiable because one can find the values a = TRUE and b = FALSE, which make (a AND NOT b) = TRUE. In contrast, "a AND NOT a" is unsatisfiable.

SAT is the first problem that was proven to be NP-complete. This means that all problems in the complexity class NP, which includes a wide range of natural decision and optimization problems, are at most as difficult to solve as SAT. There is no known algorithm that efficiently solves each SAT problem, and it is generally believed that no such algorithm exists; yet this belief has not been proven mathematically, and resolving the question of whether SAT has a polynomial-time algorithm is equivalent to the P versus NP problem, which is a famous open problem in the theory of computing.
[source]https://en.wikipedia.org/wiki/Boolean_satisfiability_problem

**Run**\
For the run two files are considered at a time. For example, uf20-01.cnf and 1.txt
First one contains a SAT instance I (in .cnf format) and second one is a solution for I. 
This program indicates whether the provided solution is a valid solution for I or not.


**File format for Satisfiability Problems**\
The preamble. The preamble contains information about the instance. This information is contained in lines. Each line begins with a single character (followed by a space) that determines the type of line. These types are as follows:
• Comments : comment line give human-readable information about the file and are ignored by programs. Comment lines appear at the beginning of the preamble. Each line begins with a lower-case character c
c This is an example of a comment line
• Problemline:thereisoneproblemlineperinputfile.Theproblemline must appear before any node or arc descriptor lines. For cnf instances, the problem line has the following format, the problem line begins with a lower-case character p
p FORMAT VARIABLES CLAUSES
The FORMAT field allows programs to determine the format that will be expected, and should contain the word “cnf”. The VARIABLES field contains an integer value specifying n, the number of variables in the instance. The CLAUSES field contains an integer value specifying m, the number of clauses in the instance. This line must occur as the last line of the preamble.
• The CLAUSES . The clauses appear immediately after the problem line. The variables are assumed to be numbered from 1 up to n. It is not necessary that every variable appear in an instance. Each clause will be represented by a sequence of number, each separated by either a space, a tab, or a newline character. The non-negated version of a variable i is represented by i; the negated version is represented
by -i.
Each clause is terminated by “0”. Unlike many formats that represent the end of a clause by a new-line symbol, this format allows clauses to be on multiple lines.
Example: (x 1∨x 3∨-x 4)∧(x 4)∧(x 2∨-x 3)
A possible input file would be
c Example CNF format file c
p cnf 4 3
1 3 -4 0 40
2 -3 0

**Output or solution files**\
Every algorithm or heuristic creates an output or solution file. This output file should consist of one or more of the following lines, depending on the type of algorithm and problem being solved.
• Comment. Comment line give human-readable information about the file and are ignored by programs. Comment lines can appear anywhere in the file. Each comment line begins with a lower-case character c. Note that comment lines can be used to provide solution information not otherwise available (i.e., computation time, number of calculations). 
c This is an example of a comment line 
• Variable Line 

vV
The lower-case character v means that this is a variable line. The value V is either a positive value i , which means that i should be set to true or a negative value -i , implying it should be set to false. 
