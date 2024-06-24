The Student Grade Management System is a program designed to manage student course grades. 
It allows administrators to input, query, modify, and delete student information, as well as sort and search student grades.

Following actions were added for an interactive interface.
1. Input and store student information
  a. Implement a function to input student's ID, name (both English and Chinese), subject wise grades (Math grade and English grade) and calculate the total score.
  b. Save the student information to file(s) using commas as separators between the fields. This will make it a CSV file, which is also accessible in MS Excel.

2. Print all students’ information
  a. Implement a function to read student information from the file(s) and print all student information on the screen.

3. Modify student’s information
  a. Implement a function to check if a student exists in the student information file.
  b. Student searching can be done in a fuzzy way. Use Python Regex library to do fuzzy searching and matching.
  c. If the student exists, allow the administrator to modify any information of the student (name, grades, etc.).
  d. If the student does not exist, return to the main menu.

4. Delete student information:
  a. If the student exists, allow the administrator to delete the student's information.
  b. If the student does not exist, return to the main menu.

5. Sort by student grades:
  a. Implement a function to sort student information based on the total score.
  b. Display the sorted student information, including ID, name, Math grade, English grade, and total score.

6. Search for student information:
  a. Implement a function to search for a student's information based on their ID or name. Name search should support fuzzy search system
  b. If the ID exists, output the detailed information of the student.
  c. If the ID does not exist, prompt that the input ID does not exist.
