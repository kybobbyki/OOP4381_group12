# OOP4381_group12
 ITSS/BUAN 4381 group 12 project. 

Write a program that helps users manage daily expenses. Functionalities of this system include:
Enable users to input the transaction information, such as name of the transaction, the amount, the date, the category of the transaction, etc. Assign each transaction a unique transaction ID. Store the information in a file.
(Note: when users run the function again, the new transaction should be stored in the file together with the transaction they entered previously. In other words, the transactions they entered previously should not be cleared.)

Enable users to view transactions filtered by both a time period (date range) and a specific type (e.g., only food transactions within a certain date range).

Enable users to modify an existing transaction. To modify a transaction, users must specify both the transaction type and the date of the transaction they want to update. The program will then display all transactions matching that type and date, allowing users to select by transaction ID and make changes.

Display the statistics for each type of expense. For example, for food transactions, the program can display the average spent per meal type (e.g., average spent on lunch). Additionally, provide general statistics for all transactions over a specified period, such as total spending and daily average.

Requirements:
When users run the program, the program asks users what they want to do (e.g., add a transaction, see the existing transactions, modify an existing transaction, or display the statistics of the transactions). The program should continuously prompt users for actions until users decide to quit (for example, users enter “quit”).

Have a class named Transaction to store attributes and write methods that enable information modification.

Create at least two child classes of Transaction for different types of expenses. Each subclass should represent a specific type of expense and include additional unique attributes. Each subclass should define methods relevant to the unique attributes it introduces. For example, a FoodTransaction can have attributes such as meal_type and location and have methods to set and display meal_type and location.

Determine by yourself the details of each functionality (such as what transaction information are included, what statistics are provided, the data types, how to store the information, etc.). Include at least three different types of information and three different statistics.

Store the information in a structured format such as txt or csv, with separate files or sections for each type of transaction. Each transaction entry should include the unique attributes of its respective subclass. When modifying or viewing transactions, the program should read from these files, instantiate the correct subclass, and retrieve the transaction details.

Use meaningful variable and method names, and add appropriate comments to make the code readable.

Deliverables:
A Jupyter Notebook file or .py files that include your code, with comments explaining the purpose of each class, method, and main sections of functionality.

A word document that explains

The class hierarchy, including details on the base class and each subclass.
Sample input and output for each functionality (e.g., adding, viewing, modifying transactions).
Screenshots demonstrating program functionality for different expense types and statistics.
Rubric:
Program Logic and User Guidance [15 points]

The program follows the logic in the requirements, ensuring each function operates correctly based on user inputs.
Clear prompts and messages are provided to inform users of the available actions and what they need to do when using a particular functionality.
Exceptions are implemented to prevent the system from crashing due to improper actions or invalid inputs.
Class Structure and Implementation [20 points]
The Transaction class is defined as required, including core attributes like transaction ID, amount, date, and category.
At least two child classes are created, each representing a different type of expense and including unique attributes.
Each subclass includes relevant methods for its unique attributes.
Adding and Storing Transactions [10 points]

Users can add new transactions, specifying the necessary details based on the transaction type.
Transactions are stored in the file in a structured format, ensuring that previously entered transactions are retained and new entries are appended correctly.
Viewing Transactions by Type and Time Period [10 points]

Users can filter and view transactions by a specified date range and transaction type.
The program retrieves and displays the relevant information from the file correctly.
Modifying Existing Transactions [10 points]

Users can modify a transaction by specifying the transaction type and date.
The program displays matching transactions and allows users to select by transaction ID to make updates. The file is updated accordingly.
Statistics Display [15 points]

For each expense type, at least three different statistics are displayed (e.g., average spent per meal type for food transactions, average spent on each day).
Code Readability [5 points]

Variable and method names are meaningful and reflect their purpose.
Comments are added to explain the purpose of each class, method, and major sections, enhancing code readability.
Documentation [15 points]

A Word document clearly describes the class hierarchy and functionality of the program.
Sample inputs and outputs are included, demonstrating how to use each function.
Screenshots are provided to illustrate program flow and show examples of the different expense types and statistics.
Use of AI:
Students are permitted to use AI as a tool for guidance and learning. However, to ensure academic integrity and a deep understanding of the project, the following guidelines must be adhered to:

Scope of AI Assistance:

Permitted Use: Students may ask AI specific, targeted questions related to concepts, methods, debugging help, or suggestions on structuring parts of their code. They may also seek clarification on requirements or explanations of programming principles related to the project.
Prohibited Use: Students are not allowed to generate the entire project code or significant portions of it directly from AI. This includes copying full code implementations for major functions or classes and assembling them into the final project without modification or understanding.
Original Work: Students should ensure that their final code reflects their own effort and understanding, with AI used only as a supporting resource, similar to asking for help from a tutor or referring to documentation.
AI Interaction Documentation:

If students used AI, they must submit a separate document detailing their AI interactions. This document should include screenshots of specific questions they asked the AI and how they applied AI responses in their project, detailing any modifications made to the AI’s suggestions.
Consequences of Violations:

Directly generating large portions of code or the entire project from AI without explanation will result in 0 for the project.
Grading break down
Program Logic and User Guidance [15 points]

The program follows the logic in the requirements, ensuring each function operates correctly based on user inputs.
Clear prompts and messages are provided to inform users of the available actions and what they need to do when using a particular functionality.
Exceptions are implemented to prevent the system from crashing due to improper actions or invalid inputs.
Class Structure and Implementation [20 points]

The Transaction class is defined as required, including core attributes like transaction ID, amount, date, and category.
At least two child classes are created, each representing a different type of expense and including unique attributes.
Each subclass includes relevant methods for its unique attributes.
Adding and Storing Transactions [10 points]

Users can add new transactions, specifying the necessary details based on the transaction type.
Transactions are stored in the file in a structured format, ensuring that previously entered transactions are retained and new entries are appended correctly.
Viewing Transactions by Type and Time Period [10 points]

Users can filter and view transactions by a specified date range and transaction type.
The program retrieves and displays the relevant information from the file correctly.
Modifying Existing Transactions [10 points]

Users can modify a transaction by specifying the transaction type and date.
The program displays matching transactions and allows users to select by transaction ID to make updates. The file is updated accordingly.
Statistics Display [15 points]

For each expense type, at least three different statistics are displayed (e.g., average spent per meal type for food transactions, average spent on each day).
Code Readability [5 points]

Variable and method names are meaningful and reflect their purpose.
Comments are added to explain the purpose of each class, method, and major sections, enhancing code readability.
Documentation [15 points]

A Word document clearly describes the class hierarchy and functionality of the program.
Sample inputs and outputs are included, demonstrating how to use each function.
Screenshots are provided to illustrate program flow and show examples of the different expense types and statistics.