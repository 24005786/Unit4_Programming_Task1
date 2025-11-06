Student ID: 24005786

Unit 4: Programming

Written report

**Introduction & Project Overview**

The purpose of this report is to design, develop, and evaluate a program which calculates the monthly costs for athletes who train at the North Sussex Judo Club. This application was built using Python within the Visual Studio Code (VS Code) Integrated Development Environment (IDE) and bring together three core programming paradigms: procedural, object-orientated, and event-driven programming. The program allows users to input key details such as the athlete’s name, training plan, weight, competition category, as well as private training hours. Based on these inputs, the program calculates the total monthly cost by combining training competition, and private coaching fees. Input validation and error handling were implemented to ensure that invalid data does not cause the program to crash, therefore making it both reliable and user-friendly. The program’s design followed a structured algorithm development process using pseudocode and flowcharts before implementation. Consequently, these tools therefore ensured logical flow, clear decision structures, as well as efficient data handling. The final version of the program includes a Graphical User Interface (GUI) created with Tkinter, providing a professional and efficient interface for users.

This project demonstrates the complete software lifecycle: “from algorithm design and code implementation to debugging and evaluation,” (GeeksforGeeks, 2025) whilst following industry coding standards and secure programming practices.

**Algorithm Design**

Before developing the North Sussex Judo Monthly Fees Calculator, it was essential to design a clear algorithm which outlines the logical order of operations. The software design process ensures that the process of “planning and structuring a software system before actual coding begins. It involves defining the architecture, components, interfaces, and data flow to ensure the software meets user requirements while being efficient, scalable, and maintainable.” (K, 2025). The program’s main purpose is to calculate an athlete’s total monthly training cost based upon their training plan, number of private coaching hours, and competitions entered. To make it both secure as well as user-friendly, the algorithm also implements input validation, data integrity checks and error handling.

**Identifying Inputs, Processes & Outputs:**

|  |  |
| --- | --- |
| **Stage** | **Description** |
| Inputs | Athlete Name, Training Plan (Beginner, Intermediate, Elite), Weight (kg), Competition Category (Flyweight - Heavyweight), Private Training Hours (0 -20), Number of Competitions. |
| Processes | Validate all user inputs, auto-cap private hours at 20, prevent beginners from entering competitions, calculate weekly fees, private hour rate, and competition cost, then compute total monthly cost. |
| Outputs | Display a full breakdown of training, private, and competition fees, total cost, and a weight category feedback message. |

**Pseudocode Design**

Before coding, pseudocode was created to outlines the logical flow and structure of the program. As a result, this helped ensure that the logic, calculation, and validation rules were correct before implementation.

![This image shows a screenshot of Visual Studio Code with a file named `Unit4_Programming_Pseudocode.txt` open in the editor. The file contains pseudocode for a "North Sussex Judo Monthly Fees Calculator." Key elements visible in the pseudocode: - **Pricing constants** for different training plans (Beginner, Intermediate, Elite), coach rates, and entry fees. - **Weight category upper limits** for various judo categories (Flyweight, Lightweight, etc.). - **User input and validation** for training plan, weight category, number of competitions, and private coaching hours. - **Conditional logic** to restrict beginners from entering competitions. - **Loops** for input validation and repeating prompts until valid data is entered. The editor uses syntax highlighting for plain text, and the file explorer is visible on the left, showing other related files. The top bar shows multiple open tabs, including a README, a flowchart image, and another pseudocode file. The status bar at the bottom indicates the cursor position and file details.](./24005786_Task1_WrittenReport_images/image_001.png)

**Figure 1:** Pseudocode outlining the planned algorithm steps for data input, validation and monthly cost calculation

![This image shows a screenshot of Visual Studio Code with a file named **Unit4_Programming_Pseudocode.txt** open in the editor. The file contains structured pseudocode for a program related to a sports or training scenario, likely for managing competition categories, training plans, and costs. Key elements visible in the pseudocode: - **Inputs**: User is prompted to enter their weight, select a competition weight category, and input the number of competitions and private coaching hours per week. - **Validation**: The code checks if the competition category is valid and restricts beginners from entering competitions. - **Calculations**: It calculates weekly fees, training costs, private coaching costs, competition costs, and total costs. - **Weight Check**: The code compares the user's weight to the category limit and generates a message indicating if the user is over, under, or exactly at the limit. - **Output**: The section for output is indicated but not shown in the visible portion. The Visual Studio Code interface shows tabs for other files at the top, including a README, a flowchart image, and the main program file. The editor uses syntax highlighting for plain text, and the sidebar shows the file explorer.](./24005786_Task1_WrittenReport_images/image_002.png)

![This image shows a screenshot of Visual Studio Code with a pseudocode file open, named `Unit4_Programming_Pseudocode.txt`. The file appears to be part of a programming assignment or project related to calculating monthly fees for athletes. Key points visible in the image: - The pseudocode is structured with clear sections for output, data storage, and loop control. - Output statements display information such as the athlete's name, selected plan, itemized monthly costs (training, private coaching, competitions), total monthly cost, and a weight message. - There is a section to optionally store a summary record for reporting, appending various variables (athlete name, training plan, costs, and weight message) to an `ATHLETES` collection. - A loop allows the user to add another athlete, with input validation for "Yes" or "No" responses. - The program ends with a thank you message. - The editor is in dark mode, and there are multiple tabs open, including a README file and a flowchart image. - The file uses indentation and comments for clarity, and the pseudocode is written in plain text. Overall, the image shows a well-organized pseudocode implementation for a monthly fees calculator, likely for a sports club or similar context.](./24005786_Task1_WrittenReport_images/image_003.png)

**Flowchart Representation**

The algorithm was represented visually through a flowchart created in Draw.io (diagrams.net). It shows decision structure, loops, and data flow from user input through to the final output.

**Figure 2:** Flowchart showing the decision-making process and cost calculation logic for the North Sussex Judo Monthly Fees Calculator.

![This image is a **flowchart** for a program that manages athlete training and competition costs. Here’s a summary of its process: 1. **Start**: The program begins by initializing constants such as weekly fees, coaching rate, competition fee, weeks per month, and category limits. 2. **Add Athlete Loop**: The user is asked if they want to add another athlete. If yes, the following steps are repeated for each athlete: - **Input Athlete Name** - **Input Training Plan**: Must be one of Beginner, Intermediate, or Elite. If invalid, the user is prompted to re-enter. - **Input Current Weight**: Must be greater than 0. If invalid, re-enter. - **Input Competition Category**: Must be Flyweight, Lightweight, or Heavyweight. If invalid, re-enter. - **Beginner Plan Check**: If the athlete is a beginner, they cannot enter competitions (number of competitions set to 0). - **Input Number of Competitions**: For non-beginners, must be greater than 0. If invalid, re-enter. - **Input Private Hours per Week**: Must be between 0 and 5. If invalid, re-enter. - **Calculate Monthly Hours**: Private hours per week × 4. - **Calculate Total Costs**: - Training cost = weekly fee × 4 - Private cost = private hours per month × 4.50 - Competition cost = number of competitions × 22.00 - Total cost = training cost + private cost + competition cost - **Weight Category Check**: - If Heavyweight, display "No upper limit (over 100kg)". - Otherwise, check if the athlete's weight is within the category limit and display the difference or how much they are over. - **Display Results**: Athlete name, training plan, monthly cost, total cost, and weight message. 3. **End**: The process ends after all athletes are entered. **Purpose:** The flowchart helps organize athlete data, validate inputs, calculate costs, and check weight categories for a training and competition management system.](./24005786_Task1_WrittenReport_images/image_004.png)

**Choice of Programming Paradigms**

This program integrates three programming paradigms to meet functional and performance requirements:

* Procedural Programming is a “programming paradigm that organises code into step-by-step instructions called procedures, routines, or functions.” (*Ada Computer Science*, no date). This ensures the program is executed in a logical, step-by-step program, therefore making it easy to test and maintain.
* Object-Orientated Programming (OOP) is a “programming paradigm based on the concept of ‘objects,’ which are self-contained units that combine data and the code (functions) that operate on that data.” (BBC Bitesize, no date). This approach increases reusability, readability, and minimising redundancy.
* Event-Driven Programming is a “paradigm where the program's flow is determined by external occurrences called "events," such as user actions, sensor inputs, or messages from other systems,” (Convex, 2024). For instance, the GUI, which was built using Tkinter responds to user interactions, therefore making the program interactive and responsive.

These paradigms complement each other. For example, procedural logic ensures control flow, OOP structures the data and logic neatly, and event-driven programming connects it all through the GUI.

**Design Rational and Optimisation**

The design process followed a structured approach to ensure both accuracy as well as efficiency:

* Input validation presents invalid data (e.g. negative hours, invalid categories).
* Constants are used for key values (fees, limits) to improve maintainability.
* The flowchart and pseudocode acted as roadmaps during implementation.
* OOP principle ensure scalability for future updates.
* GUI design ensures accessibility and user-friendliness, improving interaction quality.

This optimisation demonstrates careful planning and high level understanding of the algorithm design and program flow.

**Evaluation of Algorithm Design**

The final algorithm successfully meets the functional, technical, and user requirements set out in the problem statement.

* All inputs are validated correctly, preventing errors and crashes.
* Outputs are formatted clearly, improving user understanding.
* The logic is efficient, avoiding redundant calculations as well as nested conditions.
* The design could efficiently integrate future enhancements, such as data storage or login systems.

**Steps from Algorithm to Code**

After completing the design phase through pseudocode and flowchart development, the nest step was to translate these algorithmic representations into functional Python code. This process required careful consideration of programming paradigms, secure coding practices, and modular structure to ensure accuracy, maintainability, and performance.

**Translating Pseudocode into Python**

The pseudocode created earlier defined the step-by-step logical structure of the program - including user input, data validation, decision-making, and cost calculation. Each part of the pseudocode was converted into Python syntax while maintain readability and efficiency. For example, the pseudocode’s “IF training\_plan = Beginner THEN competitions = 0” was implemented in Python as:

![This image shows a snippet of Python code in Visual Studio Code. The code checks if a user's plan is "Beginner" using an `if` statement: ```python if self.plan == "Beginner": self.competitions = 0 ``` - There are comments explaining that beginners cannot enter competitions. - If the plan is "Beginner", the `competitions` attribute is set to 0. - Additional comments clarify that for beginners, any competitions entered should result in a competition cost of £0.00.](./24005786_Task1_WrittenReport_images/image_005.png)

Similarly, the pseudocode’s repetition structure “REPEAT UNTIL choice = N” was adapted into an event-driven loop through the Tkinter GUI, where the user interacts repeatedly via the “Calculate” button. This ensured that the program remains active and user-controlled rather than sequentially looping in the terminal.

**Implementing Flowchart Logic in Code**

The flowchart, created using Draw.io, visually represented the program’s decision-making process - particularly around validation, cost calculation, and category checks. Each flowchart condition was translated into Python IF-ELIF-ELSE statements and summarised within functions or class methods for modularity. For example, “IF category limit = ‘Unlimited’ THEN display ‘No upper limit’ ELSE compare weight to limit.”

This is translated into Python as:

![This image shows a snippet of Python code inside Visual Studio Code. The code is part of a function or method that compares a weight value (`self.weight`) to a `limit`. Here’s what it does: - If `limit` is `"Unlimited"`, it returns a message saying there is no upper limit for the Heavyweight category. - If `self.weight` is greater than `limit`, it returns a message indicating the weight is "OVER" by the difference, formatted to one decimal place. - If `self.weight` is less than `limit`, it returns a message indicating the weight is "UNDER" by the difference, also formatted to one decimal place. - If neither condition is met, it returns "Exactly on the limit." There is also a comment `#TEST Heavyweight` next to the first return statement. The code uses f-strings for formatting output.](./24005786_Task1_WrittenReport_images/image_006.png)

This ensured that the control flow mirrored the original flowchart and that all decision branches produced accurate and predictable results.

**Justification of Python as the Chosen Programming Language**

Python was used as the implementation language for this project because it supports multi-paradigm development, therefore allowing the integration of procedural, object-orientated, and event-driven programming within one application. This choice was also supported by Python’s “simplicity and readability as the language’s syntax is clean and intuitive, making it an excellent choice for beginners. Python’s code is often described as almost English-like, which allows developers to focus on solving problems rather than deciphering complex syntax.” (Singh, 2024).

Key reasons for choosing Python:

* Python’s syntax closely resembles pseudocode making it ideal for clear, step-by-step logic conversion.
* Support for OOP, by allowing “the creation of classes and objects, which group data (attributes) and behaviour (methods) together.” (*Is Python Object-Oriented?* 2024). This promotes encapsulation and modularity, therefore promoting maintainability.
* Python’s built-in GUI framework (Tkinter) can “abstract away low-level details of GUI programming, making it easier for developers to focus on the logic behind the application.” (Hernandez, 2024). This enhances the ability to write clean and maintainable code as well as reducing the chance of errors.
* In Python, using “try-except blocks is crucial for maintaining security by preventing unexpected crashes and managing errors effectively.” (Discover how to handle errors in Python effectively while maintaining security. Learn the best practices for robust and secure coding., 2024).
* Visual Studio’s Python is simple and comes with built features that enhance a developer’s experience. For instance, “features like syntax autocomplete, linting, debugging, unit testing, GitOps, virtual environments, notebooks, editing tools, and the ability to customize the editor.” (Awan, 2023).

**Linking Algorithms to Code Structure**

The following connections were made between design documentation and implementation:

|  |  |  |
| --- | --- | --- |
| **Design Component** | **Implementation in Code** | **Explanation** |
| Input Handling (pseudocode input lines0 | Tkinter Enter and OptionMenu widgets | GUI-based data entry replacing console input. |
| Validation | validate\_inputs() function in Athlete class | Ensures data integrity (hours < 20, valid category, etc) |
| Decision Making | If-elif-else structures | Implements logical branching identical to the flowchart |
| Calculations | calculate\_fees() method | Executes training, private, and competition cost formulas. |
| Output Display | result\_text.set() | Updates GUI dynamically to show results. |

**Implementation Reflection and Professional Quality**

Throughout development, both the pseudocode and flowchart were actively referenced to guide program structure as well as ensure logical consistency. Python’s indentation and naming conventions made the translation from design to code more readable. To maintain coding standards, the program used:

* Uppercase constant variables, (PRIVATE\_HOUR\_RATE, MAX\_PRIVATE\_HOURS).
* Consistent indentation and commenting for clarity.
* Docstrings (“”” …”””) to explain class as well as method functionality.

The close alignment between the algorithm and the final code ensured minimal errors during testing, any issues (such as invalid user input or missing validation) were quickly identified and resolved using IDE feedback tools like the Run and Debug feature in VS Code.

**Development Process**

**Setting Up the Environment**

Development began by configuring the VS Code IDE, installing Python and linking environment to a GitHub repository. This setup enabled real-time syntax checking version control and integrated debugging, all of which contributed to producing a clean, professional code.

A new file, main.py was created to implement the program, and support files such as (Unit4\_Programming\_Pseudocode.text and Unit4\_Programming\_Task1\_Flowhcart\_drawio.png) were added for documentation.

**Figure 3:** VS Code workspace showing main.py and other project files

![This image shows the **Explorer** pane in Visual Studio Code. The currently open folder is named `UNIT4_PROGRAMMING_TASK1`. Inside this folder, there are four files: 1. `README.md` (a Markdown file, currently selected) 2. `Unit4_Programming_Main.py` (a Python file) 3. `Unit4_Programming_Psuedocode.txt` (a text file, likely containing pseudocode) 4. `Unit4_Programming_Task1_Flowchart.drawio` (a Draw.io diagram file, likely a flowchart) The Explorer pane also displays icons for common actions like creating a new file or folder, refreshing, and collapsing the folder view.](./24005786_Task1_WrittenReport_images/image_007.png)

**Building the Core Logic**

The initial development phase involved writing the procedural structure of the program. Constants were declared at the top to define training fees, competition costs, and private training rates, ensuring readability, and easy modification. Each logical block from the pseudocode was implemented step by step, such as:

* Input validation.
* Cost calculation.
* Output formatting.

![This image shows a Python method called `calculate_fees(self)` defined inside a class. The method calculates various monthly costs related to a plan, likely for a training or coaching program. Here’s a breakdown: - **Docstring:** Describes the method as "Procedural control: Control total monthly cost". - **weekly_fee:** Looks up a weekly fee from a dictionary `WEEKLY_FEES` using `self.plan`. - **training_cost:** Multiplies the weekly fee by 4 (weeks in a month). - **private_cost:** Multiplies `self.private_hours` by `PRIVATE_HOUR_RATE`. - **competition_cost:** Multiplies `self.competitions` by `COMPETITION_COST`. - **total_cost:** Sums up training, private, and competition costs. - **Return:** Returns a tuple with all four costs: `training_cost`, `private_cost`, `competition_cost`, and `total_cost`. The code uses constants and instance variables, and is formatted with syntax highlighting in Visual Studio Code’s dark theme.](./24005786_Task1_WrittenReport_images/image_008.png)

**Object-Oriented Programming (OOP) Implementation**

To make the system flexible and maintainable, the core logic was absorbed in a single class named Athlete. This class structure promoted data encapsulation and reusability, allowing future extensions such as saving athlete data or exporting reports. The class contained:

* Attributed: name, plan, weight, category, private hours, competitions.
* Methods: validate\_inputs(), calculate\_fees(), and weight\_message().

For example, the validation logical was written to ensure robust, secure data entry:

![This image shows a Python method called `validate_inputs` defined within a class (indicated by the use of `self`). The method validates athlete data by checking two conditions: 1. If `self.plan` is not in the `WEEKLY_FEES` collection, it raises a `ValueError` with the message "Invalid training plan selected." 2. If `self.category` is not in the `CATEGORY_LIMITS` collection, it raises a `ValueError` with the message "Invalid category." The method includes a docstring: `"""Validate athlete data securely"""`. The code uses indentation and color highlighting typical of Visual Studio Code.](./24005786_Task1_WrittenReport_images/image_009.png)

This flexible approach directly demonstrated OOP principles. Which are, “encapsulation, abstraction, inheritance, and polymorphism. These principles help organise and structure code by creating objects that contain both data and functions, making programs more modular, reusable, and easier to maintain.” (REVUTSKA, 2023).

**Event-Driven Programming**

The algorithm’s user input section was transformed into an interactive interface using Tkinter. Each input field from the pseudocode was represented by an Entry or OptionMenu widget. The GUI listens for user events, specifically the “Calculate Monthly Fees” button, which therefore triggers the calculate\_button\_clicked() event function:

![This image shows a line of Python code in Visual Studio Code. The code creates a Tkinter button widget: ```python calculate_button = tk.Button(root, text="Calculate Monthly Fees", command=calculate_button_clicked).pack(pady=10) ``` - The button is placed in the `root` window. - The button displays the text "Calculate Monthly Fees". - When clicked, it calls the `calculate_button_clicked` function. - The button is packed into the window with a vertical padding (`pady`) of 10 pixels. **Note:** Assigning the result of `.pack()` to `calculate_button` will set it to `None`, since `.pack()` returns `None`. To keep a reference to the button, call `.pack()` on a separate line.](./24005786_Task1_WrittenReport_images/image_010.png)

This event-driven structure replaced the original REPEAT-UNTIL pseudocode loop, ensuring the program responds dynamically to user interactions instead of running in a static sequence

**Figure 4:** Tkinter GUI layout allowing user interaction and event-driven control.

![This image shows a graphical user interface (GUI) for a program called **North Sussex Judo Monthly Fees Calculator**. The interface includes the following labeled input fields and controls: - **Athlete Name:** A text box for entering the athlete's name. - **Training Plan:** A dropdown menu with options (currently set to "Beginner"). - **Weight (kg):** A text box for entering the athlete's weight in kilograms. - **Competition Category:** A dropdown menu (currently set to "Flyweight"). - **Private Training Hours (0-20):** A text box for entering the number of private training hours. - **Number of Competitions:** A text box for entering the number of competitions. Below these fields are two buttons: - **Calculate Monthly Fees** (to perform the calculation) - **Reset** (to clear the form) The layout is simple and vertically aligned, designed for easy data entry.](./24005786_Task1_WrittenReport_images/image_011.png)

**Implementing Validation and Error Handling**

During testing, several validation and logic issues were identified and resolved:

|  |  |
| --- | --- |
| Challenge | Solution |
| Program crashed when invalid inputs were entered. | Added try/except blocks to catch exceptions and show user-friendly error messages via messagebox.showerror(). |
| Private training hours above 20 caused unrealistic values. | Added an auto-cap condition: if hours > 20, set to 20. |
| “Beginner athletes incorrectly included competition costs. | Introduced conditional logic to reset competitions to 0 for beginners. |
| Tkinter widgets sometimes failed to update output. | Implemented StringVar() binding to dynamically refresh GUI results. |

**Testing & Refinement**

|  |  |  |
| --- | --- | --- |
| **Test Case** | **Expected Result** | **Outcome** |
| Beginner + any competition | Competition cost = £0.00 | Correct |
| Private hours = 21 | Auto-capped to 20 | Correct |
| Heavyweight category | “No upper limit…” message | Correct |
| Middleweight (81kg) with weight 82kg | “OVER by 1.0kg) | Correct |

**Figure 5:** Program successfully calculating monthly fees and displaying output in GUI

![This image shows a user interface for calculating monthly fees for an athlete's training and competition costs. The form includes the following fields and controls: - **Athlete Name:** A text box with "John Smith" entered. - **Training Plan:** A dropdown menu set to "Intermediate." - **Weight (kg):** A text box with "73" entered. - **Competition Category:** A dropdown menu set to "Light-Middleweight." - **Private Training Hours (0-20):** A text box with "10" entered. - **Number of Competitions:** A text box with "3" entered. Below the input fields, a summary is displayed: - Athlete: John Smith - Plan: Intermediate - Training Cost: £120.00 - Private Coaching: £95.00 - Competition Cost: £66.00 - TOTAL: £281.00 - Weight Message: Exactly on the limit. At the bottom, there are two buttons: **Calculate Monthly Fees** and **Reset**.](./24005786_Task1_WrittenReport_images/image_012.png)

**Challenges Faces and Solutions Implemented**

|  |  |  |
| --- | --- | --- |
| **Challenge** | **Description** | **Solution Implemented** |
| GUI not displaying correctly. | Initial layout overlapped labels. | Adjusted. Pack() order and added spacing with pady. |
| “String literal is unterminated” syntax error | Missing closing quote in Tkinter label. | Fixed by reviewing suggestion in VS code. |
| Event order causing calculation error. | calculate\_button\_clicked() executed before user input validated. | Added try block with sequential validation checks. |
| Data reusability, | Difficult to manage repeated input. | Encapsulated logic in OOP class structure. |

**Version Control and Iterative Development**

GitHub was used to track each development stage. Each iteration stage was committed and uploaded, allowing changes to be reviewed and rolled back if necessary. This reflects professional software engineering practice as well as supports maintainability.

![This image shows a GitHub repository page in a web browser. The repository is named **Unit4_Programming_Task1** and belongs to the user **24005786**. The **Code** tab is selected, displaying the contents of the **main** branch. The file list includes: - `README.md` - `Unit4_Programming_Main.py` - `Unit4_Programming_Psuedocode.txt` - `Unit4_Programming_Task1_Flowchart.drawio.png` There are also navigation options at the top for **Issues**, **Pull requests**, **Actions**, and **Projects**.](./24005786_Task1_WrittenReport_images/image_013.png)

**Figure 6:** GitHub repository showing all projects.

**Reflection and Quality Evaluation**

The development process successfully met the requirements of the original algorithm while improving maintainability as well as user experience. The integration of procedural, object-orientated, as well as event-driven techniques produced a well-structured, reusable and professional application. The pseudocode and flowchart effectively guided the build and reduced errors, ensuring a seamless transition from theory to practice.

**Debugging Process & IDE Features Used**

Debugging was an essential part of the program’s development process as it ensured that the final Python code operated reliably, securely, and aligned with the original algorithm and flowchart logic.

**Debugging Approach**

This was carried out continuously using both manual testing (running and reviewing program output) and automated support from VS Code. Common debugging techniques used included:

* Reading terminal error messages after each test run.
* Using try/except blocks for runtime error handling.
* Testing one component at a time (procedural - OOP - GUI).

**Common Errors Identified & Resolved**

|  |  |  |
| --- | --- | --- |
| **Issue** | **Cause** | **Resolution** |
| “String literal is unterminated” | Missing quotation mark in a Tkinter label. | Fixed by reviewing error suggestions and correcting string syntax. |
| name\_entry not defined | Widget referenced before name-entry creation | Moved declaration above event-driven function |
| Program crashed with invalid user input | Non-numeric entry for weight or hours. | Added try/except block in calculate\_button\_clicked() and displayed error with messagebox.showerror(). |
| GUI not updating dynamically | Output label not bound to variable | Replaces with StringVar() and linked to result\_text.set() |
| Incorrect validation for beginners. | Logic allowed competition fees for Beginner plan | Added conditional to set competitions = 0 when plan = “Beginner” |

**IDE Tools and Debugging Features**

The VS Code IDE provided several integrated debugging features that improved program reliability:

* Pylance highlighted missing colons, quotation marks, or indentation errors before runtime.
* Run and Debug console allowed step-by-step monitoring of variables and logic flow.
* Terminal output lops helped trace logic errors and identify where incorrect values were written.
* Code commenting simplified the testing of specific sections without affecting the entire program.

**Figure 7:** Using the VS Code Debug Console to test logic and trace errors.

![This image shows the "Run and Debug" panel in Visual Studio Code. The panel provides options to run and debug code. There is a prominent blue "Run and Debug" button. Below it, there are instructions to customize the run and debug process by creating a `launch.json` file (with a clickable link). It also mentions that you can debug using a terminal command or in an interactive chat (both are clickable links). At the bottom, there is another blue button labeled "Show automatic Python configurations." The left sidebar shows icons for Explorer, Search, Source Control, Run and Debug, and Extensions.](./24005786_Task1_WrittenReport_images/image_014.png)

**Error Handling & Secure Programming**

To prevent crashes and improve user experience, structured handling was added across the program. For example, the event-driven GUI used a try/except block to catch errors when users entered invalid data.

![This image shows a Python function definition in Visual Studio Code. The function is named `calculate_button_clicked` and is likely part of a GUI application. It is triggered when a user clicks a "Calculate" button, as described in the docstring. Key points: - The function uses a `try` block to handle potential errors. - It retrieves and processes user input from various GUI entry fields and variables: - `name` is fetched, converted to title case, and stripped of whitespace. - `plan` and `category` are retrieved from variables. - `weight` and `private_hours` are converted to floats. - `competitions` is converted to an integer. The code uses typical Tkinter-style `.get()` methods to access entry values. Syntax highlighting is visible, with different colors for keywords, strings, and variables.](./24005786_Task1_WrittenReport_images/image_015.png)

This ensured that the program remains stable, protecting it from invalid input, and aligns with secure programming standards outlined in coding guidelines.

**Reflection on Debugging Effectiveness**

The debugging process was both systematic and repeated. Each text cycle revealed minor syntax, logical, or event-driven issues, which were resolved efficiently using IDE feedback and gradual testing. Consequently, the final program operated reliably, validates user input correctly, and matches the design expectations outlined in the pseudocode and flowchart.

**Coding Standards**

Throughout the development of the North Sussex Judo Monthly Fees Calculator, strict coding standards were applied to ensure that the final program was readable, maintainable, secure and consistent with professional software practices. These standards contributed directly towards the program’s reliability, alignment, with design documentation and overall quality.

**Consistent Naming Conventions**

* Constants were written in uppercase (e.g. PRIVATE\_HOUR\_RATE, COMPETITON\_COST) to differentiate them from regular variables.
* Variables used snake\_case (e.g. weight\_entry, total\_cost) to, “improve readability, it enhances the readability of variable and function names, making them more accessible to other programmers and even your future self.” (Tuple, 2023).

![This image shows a Python source code file open in Visual Studio Code. The file is named `Unit4_Programming_Main.py` and appears to be part of a project for calculating monthly fees for the "North Sussex Judo" club. Key points in the code: - The script uses the `tkinter` library for GUI elements, importing both `tkinter` as `tk` and `messagebox` from `tkinter`. - Several constants are defined: - `WEEKLY_FEES`: A dictionary mapping membership levels ("Beginner", "Intermediate", "Elite") to their weekly fees. - `COMPETITION_COST`: The cost for competitions, set to 22.00. - `PRIVATE_HOUR_RATE`: The hourly rate for private lessons, set to 9.50. - `MAX_PRIVATE_HOURS`: The maximum number of private hours allowed, set to 20. - `CATEGORY_LIMITS`: A dictionary mapping weight categories to their upper weight limits, with "Heavyweight" set to "Unlimited". The code is well-organized, with comments and clear variable names.](./24005786_Task1_WrittenReport_images/image_016.png)

**Figure 8:** Consistent use of naming conventions and constants for readability and variable naming in main.py

**Commenting and Documentation**

Each function and class contain docstrings (“””…”””) to explain its purpose and return values. Inline comments were also added to clarify validation steps, calculation logic, and event-driven occurrences. This ensures that the purpose of every block of code was clearly documented for both the developer and moderators.

![This image shows a code snippet in Python, viewed in Visual Studio Code. It defines the start of a class named `Athlete`. The class includes a docstring: ```python """Represents an athlete with attributes and calculation methods.""" ``` This docstring briefly describes the purpose of the class. No methods or attributes are defined yet.](./24005786_Task1_WrittenReport_images/image_017.png)

Proper documentation is crucial as “it supports various aspects of the software development lifecycle, primarily by enhancing clarity, maintainability, collaboration, and knowledge transfer.” (Fisher, 2024).

**Indentation, Spacing & Readability**

Python’s enforced indentation was used consistently across all structures, improving logical clarity and reducing the likelihood of syntax errors. Blank lines were added between sections to separate constants, classes and functions, and GUI code, enhancing overall code readability. This structure mirrors professional standards found in the PEP 8 (Python Enhancement Proposal). PEP 8’s primary goal is to “make code easier for humans to read and understand, since code is read far more often than it is written.” (Python, 2023).

**Secure and Ethical Programming Practices**

Secure coding practices were integrated through input validation exception handling, as well as restricted user interaction:

* Validation checks prevented invalid input.
* Exception handling with try/except ensure the program did not crash unexpectedly.
* Sensitive inputs were not stored or logged therefore protecting user privacy.

These practices align with professional expectations for ethical and responsible software design.

**Enhancements & Optimisation of the Algorithm**

Once the program was fully implemented and tested, several opportunities for enhancement and optimisation were identified. These improvements focused on increasing efficiency, maintainability, and user experience, while ensuring that the final program met professional and ethical software standards.

**Performance and Logical Optimisation**

During testing, certain processes were refined to improve the program’s efficiency and accuracy:

* The validation methos was enhanced to auto-cap private hours at 20 instead of displaying an error, reducing unnecessary user disappointment and making the program more efficient.
* IF-ELIF-ELSE structures reduced redundancy in weight categories.
* Constants were defined once and reused throughout the program, optimising performance and preventing errors.

These enhancements ensured smoother performance and better scalability for future updates.

**Figure 9:** Example of optimised validation logic to improve user experience

**![This image shows a Python method called `weight_message(self)` inside a class. The method returns a message about a weight category based on the object's `category` and `weight` attributes. **Key points:** - It retrieves a weight limit from a dictionary called `CATEGORY_LIMITS` using `self.category`. - If the limit is `"Unlimited"`, it returns a message indicating no upper limit for the Heavyweight category. - If the object's weight is greater than the limit, it returns an "OVER by" message with the difference. - If the weight is less than the limit, it returns an "UNDER by" message with the difference. - If the weight is exactly on the limit, it returns "Exactly on the limit." - The code uses f-strings for formatting and includes a comment for testing the Heavyweight category.](./24005786_Task1_WrittenReport_images/image_018.png)**

**Code Readability & Maintainability**

Refactoring was carried out to make the code more readable and maintainable:

* Repetitive calculations were encapsulated within the calculate\_fees() method, therefore reducing duplication.
* Comments and docstrings were added to explain the logic behind each function and class.
* The program layout followed a consistent visual structure; constants, class definition, GUI setup, and event-driven functions were clearly separated with headings.

**User Experience and Interface Enhancements**

To make the program more user-friendly, a couple of interface improvements were introduced:

* A Reset button was added to allow users to clear results quickly and perform new calculations without restarting the program.
* The program now displays dynamic feedback messages (e.g. “No upper limit for Heavyweight category”) to improve user understanding of the results.

These updates improved usability and accessibility, aligning the system with professional software design principles.

**Figure 10:** User interface enhancements improving interaction and readability.

![This image shows a graphical user interface (GUI) for a program called **North Sussex Judo Monthly Fees Calculator**. The interface includes the following labeled input fields and controls: - **Athlete Name:** A text box for entering the athlete's name. - **Training Plan:** A dropdown menu with options (currently set to "Beginner"). - **Weight (kg):** A text box for entering the athlete's weight in kilograms. - **Competition Category:** A dropdown menu (currently set to "Flyweight"). - **Private Training Hours (0-20):** A text box for entering the number of private training hours (between 0 and 20). - **Number of Competitions:** A text box for entering the number of competitions. At the bottom, there are two buttons: - **Calculate Monthly Fees** - **Reset** The layout is simple and organized, designed to collect information needed to calculate monthly judo training fees.](./24005786_Task1_WrittenReport_images/image_019.png)

**Future Improvement Opportunities**

Although the current version meets all functional and technical requirements, further enhancements could be added to increase capability and efficiency:

* Exporting monthly cost reports into a PDF format.
* Adding basic authentication for coaches or admins to protect athlete data.
* Adapting the program for cloud deployment, allowing remote access and updates.

**Evaluation**

After completing the implementation and optimisation of the North Sussex Judo Monthly Fees Calculator, it was essential to evaluate the extent to which the final program matches the original and design documentation. This evaluation also reflects on the role of the IDE and coding standards in supporting the programs accuracy, usability and professional quality.

**Comparison of Algorithm & Final Program**

The final implementation remained consistent with the logic, structure, and decisions outlined in the pseudocode and flowchart. Key elements from the algorithm were successfully adapted in Python code.

|  |  |  |
| --- | --- | --- |
| **Algorithm Feature** | **Implementation in Code** | **Evaluation** |
| Input Validation. | Implemented via validate\_input() and try/except error handling. | Prevents crashes and invalid entries. |
| Decision Structures. | Used IF-ELIF-ELSE to control training, weight, and competition logic. | Matches the flowchart’s decision nodes. |
| Loop | Replaced the REPEAT-UNTIL pseudocode loop with event-driven GUI buttons. | More efficient and user-friendly. |
| Output Display | Displayed dynamically via StringVar() in Tkinter. | Produces clear, formatted results. |

This shows that the program’s logical flow mirrors the original design, demonstrating a successful transition from algorithm to implementation.

**Figure 11:** Comparison between pseudocode and final Python implementation showing structural alignment

![This image shows a Visual Studio Code window with a text file named `Unit4_Programming_Pseudocode.txt` open. The file contains pseudocode for a "North Sussex Judo Monthly Fees Calculator." Key sections in the pseudocode include: - **Pricing Constants**: Defines fees for different training plans (Beginner, Intermediate, Elite), private coaching, competition entry, and the number of weeks per month. - **Weight Category Upper Limits**: Sets upper weight limits for various judo competition categories (Flyweight, Lightweight, etc.). - **Inputs with Validation**: Prompts for athlete name, training plan, current weight, and competition category, with validation for each input. - **Competition Entry Logic**: Restricts beginners from entering competitions and validates the number of competitions for other plans. - **Private Coaching Sessions**: Placeholder for logic about private coaching sessions. The pseudocode uses clear comments and structured logic, making it easy to follow the intended program flow.](./24005786_Task1_WrittenReport_images/image_020.png)![This image shows a text file named **Unit4_Programming_Pseudocode.txt** open in Visual Studio Code. The file contains pseudocode for a program related to athlete training plans, private coaching sessions, and competition participation. Key sections in the pseudocode include: - **Inputs with Validation:** - Checks if the training plan is "Beginner" and restricts competition entry. - Prompts for the number of competitions and validates the input. - Prompts for private coaching hours per week and validates the input. - **Calculations:** - Calculates weekly and monthly training costs, private coaching costs, and competition costs. - Sums up the total cost. - **Weight Comparison:** - Compares the athlete's weight to a category limit. - Sets a status and message based on whether the athlete is over, under, or exactly at the weight limit. - **Output:** - Displays the athlete's name and the selected training plan. The pseudocode uses clear comments and logical structure to outline the program's flow.](./24005786_Task1_WrittenReport_images/image_021.png)

![This image shows a Python source code file open in Visual Studio Code. The file appears to be part of a project for calculating monthly fees for a judo club, as indicated by the comment at the top: **#North Sussex Judo Monthly Fees Calculator**. Key elements in the code: - **Imports:** The code imports `tkinter` and `messagebox` for GUI functionality. - **Constants:** Several constants are defined: - `WEEKLY_FEES`: A dictionary mapping training plans ("Beginner", "Intermediate", "Elite") to their weekly fees. - `COMPETITION_COST`: Set to 22.00. - `PRIVATE_HOUR_RATE`: Set to 9.50. - `MAX_PRIVATE_HOURS`: Set to 20. - `CATEGORY_LIMITS`: A dictionary mapping weight categories to their limits. - **Class Definition:** The `Athlete` class is defined, representing an athlete with attributes and calculation methods. - The `__init__` method initializes attributes like name, plan, weight, category, private hours, and competitions. - The `validate_inputs` method checks if the plan and category are valid, raising a `ValueError` if not. The code is well-commented and uses clear variable names, making it easy to understand its purpose and structure.](./24005786_Task1_WrittenReport_images/image_022.png) ![This image shows a Python source code file (`Unit4_Programming_Main.py`) open in Visual Studio Code. The code defines part of a class called `Athlete` with several methods: - `validate_inputs(self)`: Validates the athlete's category, private hours, and competitions. It raises errors for invalid values and caps private hours at a maximum. - `calculate_fees(self)`: Calculates various costs (weekly fee, training cost, private cost, competition cost, total cost) for the athlete. - `weight_message(self)`: Returns a message about the athlete's weight category, indicating if they are under, over, or exactly at the category limit. There are comments explaining the logic, and some constants like `CATEGORY_LIMITS`, `MAX_PRIVATE_HOURS`, and others are referenced but not shown in the image. The bottom of the image shows the start of a GUI setup with `root = tk.Tk()`. The code uses indentation and syntax highlighting typical for Python in Visual Studio Code.](./24005786_Task1_WrittenReport_images/image_023.png)![This image shows a screenshot of Python code in Visual Studio Code. The code is part of a GUI application, likely for managing judo athlete information. Here are some key points: - The `Athlete` class has a method `weight_message(self)` that returns a message based on the athlete's weight compared to a limit. - The GUI is built using the `tkinter` library (`tk`), as seen from the use of `tk.Tk()`, `tk.Label`, `tk.Entry`, and `tk.OptionMenu`. - The window is titled "North Sussex Judo Monthly Fees Calculator" and sized to 500x600 pixels. - Input fields are created for: - Athlete Name - Training Plan (with options) - Weight (kg) - Competition Category (with options) - Private Training Hours (0–20) - Number of Competitions - An output label is set up to display results. - There is a placeholder for an event-driven function `calculate_button_clicked()` at the bottom. The code is well-organized with comments separating sections for GUI setup, input fields, and output.](./24005786_Task1_WrittenReport_images/image_024.png) ![This image shows a Python source code file open in Visual Studio Code. The code is part of a Tkinter-based GUI application for managing athlete training plans and costs. Key elements in the code: - Several Tkinter widgets are created for user input, including `Entry` fields for name, weight, private training hours, and number of competitions. - `OptionMenu` widgets are used for selecting a training plan and competition category. - A label is set up to display output results. - The function `calculate_button_clicked()` is defined to handle the event when the user clicks a "Calculate" button. It retrieves and processes input values, creates an `Athlete` object, validates inputs, and calculates costs. The code is well-commented, with sections for GUI setup and event-driven functions.](./24005786_Task1_WrittenReport_images/image_025.png) ![This image shows a screenshot of Python code in Visual Studio Code. The code defines a function called `calculate_button_clicked()`, which appears to be part of a Tkinter-based GUI application for calculating monthly fees for athletes. Key points in the code: - The function retrieves user input from GUI entry fields (`weight_entry`, `category_var`, `private_hours_entry`, `competitions_entry`). - It creates an `Athlete` object with the input data and validates the inputs. - It calculates various costs (`training_cost`, `private_cost`, `competition_cost`, `total_cost`) using the `athlete.calculate_fees()` method. - It gets a weight message from `athlete.weight_message()`. - The results are displayed in a text widget (`result_text.set(...)`). - There is error handling for `ValueError` (shows an "Input Error" message) and a generic exception handler for unexpected errors. - Below the function, two Tkinter buttons are created: one to calculate fees and one to reset the result text. - The GUI main loop is started with `root.mainloop()`. The code is well-structured and uses f-strings for formatting output.](./24005786_Task1_WrittenReport_images/image_026.png)

**Evaluation of IDE Effectiveness**

Using VS Code as the main development tool significantly improved the quality and maintainability of the program. The IDE’s features supported a professional iterative development process:

* Pylance provides real-time syntax and error detection, preventing runtime issues before running the program.
* Run and Debug Tools enable line-by-line testing and monitoring of different structures.

These tools directly contributed towards a more reliable program by reducing syntax errors improving testing accuracy and ensuring consistent version management.

**Evaluation of Coding Standards**

Coding standards are a “set of rules and guidelines for writing software code to ensure consistency, readability, and maintainability across a project. They include aspects like naming conventions, formatting, commenting, and error handling, and are followed by development teams to improve code quality, reduce bugs, and make collaboration easier.” (What coding standards in software engineering should we follow?, no date). For example, the program followed PEP 8 standards as:

* Constants were defined once and reused throughout the program to prevent redundancy.
* Function and class methods were well-commanded for clarity.
* Secure validation prevented unexpected vulnerabilities within the program.

These practices ensured the code was readable. reusable, and adaptable for future updates, aligning with professional expectations for secure, ethical programming.

**Figure 12:** Example of adhering to PEP 8 and professional coding standards.

![This image shows a section of Python code in Visual Studio Code. It defines several constants related to fees and categories, likely for a sports or training program: - `WEEKLY_FEES`: A dictionary mapping skill levels ("Beginner", "Intermediate", "Elite") to their weekly fees. - `COMPETITION_COST`: The cost to enter a competition. - `PRIVATE_HOUR_RATE`: The hourly rate for private lessons. - `MAX_PRIVATE_HOURS`: The maximum number of private hours allowed. - `CATEGORY_LIMITS`: A dictionary mapping weight categories (like "Flyweight", "Lightweight", etc.) to their upper weight limits, with "Heavyweight" set to "Unlimited". The code uses uppercase variable names for constants and is commented with `#Constants` at the top.](./24005786_Task1_WrittenReport_images/image_027.png)

**Evaluation of Programming Efficiency & User Experience**

User experience was optimised through interactive design, fast calculations, and real-time error messages, all of which contribute towards a high-level solution:

* All calculations produced accurate and validated outputs.
* The interface was intuitive, allowing non-technical users to operate the calculator without difficulty.
* Error handling prevented any crashes, therefore enhancing reliability and efficiency.

**Reflection & Scalability**

The project demonstrates a theoretical design to an implemented, professional solution. Future scalability was considered throughout the process, ensuring that additional features could be easily added. This may include athlete database storage, reporting or authentication. The balance between functionality, validation and user experience shows strong adherence to professional standards.

Reference List:

*Ada Computer Science* (no date) *Ada Computer Science*. Available at: https://adacomputerscience.org/concepts/procprog\_paradigm.

Awan, A.A. (2023) *Setting Up VSCode For Python: A Complete Guide*, *Datacamp.com*. DataCamp. Available at: https://www.datacamp.com/tutorial/setting-up-vscode-python.

BBC Bitesize (no date) *Object Oriented Programming (OOP) - Contemporary trends in software development - CCEA - GCSE Digital Technology (CCEA) Revision*, *BBC Bitesize*. Available at: https://www.bbc.co.uk/bitesize/guides/zc8pjty/revision/3.

Convex (2024) *Event Driven Programming: A Definitive Guide*, *Convex.dev*. Available at: https://stack.convex.dev/event-driven-programming.

*Discover how to handle errors in Python effectively while maintaining security. Learn the best practices for robust and secure coding.* (2024) *Linkedin.com*. Available at: https://www.linkedin.com/advice/3/what-best-practices-error-handling-python-qcvic (Accessed: January 2025).

Fisher, L. (2024) *The Importance of Robust Documentation in Software Development*, *Acm.org*. Communications of the ACM. Available at: https://cacm.acm.org/blogcacm/the-importance-of-robust-documentation-in-software-development/.

GeeksforGeeks (2025) *Software Development Life Cycle (SDLC)*, *GeeksforGeeks*. Available at: https://www.geeksforgeeks.org/software-engineering/software-development-life-cycle-sdlc/.

Hernandez, M. (2024) *What Are the Benefits of Using Python GUI Development?*, *ParallelStaff | Nearshore Software Development Company*. Parallel Staff, Inc. Available at: https://parallelstaff.com/benefits-of-using-python-for-gui-development/.

*Is Python Object-Oriented?* (2024) *Coursera*. Available at: https://www.coursera.org/in/articles/is-python-object-oriented.

K, S. (2025) *Software Design Process Explained: Everything You Should Know*, *EitBiz Blog - Updates on Technology and Innovative Digital Solutions*. Available at: https://www.eitbiz.com/blog/software-design-process-everything-you-should-know/ (Accessed: 2025).

Python, R. (2023) *How to Write Beautiful Python Code With PEP 8 – Real Python*, *realpython.com*. Available at: https://realpython.com/python-pep8/.

REVUTSKA, N. (2023) *What is Object-Oriented Programming (oop)? Explaining four major principles*, *Softserveinc.com*. Available at: https://career.softserveinc.com/en-us/stories/what-is-object-oriented-programming-oop-explaining-four-major-principles.

Singh, P. (2024) *10 Advantages of Python Over Other Programming Languages*, *Analytics Vidhya*. Available at: https://www.analyticsvidhya.com/blog/2024/01/advantages-of-python-over-other-programming-languages/.

Tuple (2023) *Snake Case*, *Tuple.nl*. Available at: https://www.tuple.nl/en/knowledge-base/snake-case (Accessed: 2025).

*What coding standards in software engineering should we follow?* (no date) *SearchSoftwareQuality*. Available at: https://www.techtarget.com/searchsoftwarequality/answer/What-coding-standards-in-software-engineering-should-we-follow.