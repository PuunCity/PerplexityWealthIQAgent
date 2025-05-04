README ver 1.0

Hi! This is WealthIQ's repository and here is a breakdown of the contents of the repository:

## The code
The main file in which the program's execution as well as the API integration is being made is in **APIIntegration.py**

### Libraries
The project uses many libraries, modules and dependencies such as:
- matplotlib.pyplot
- openai
- time
- datetime
- Email management:
  - email.message
    - mime.multipart
    - mime.text
    - mime.image 
  - markdown
  - smtplib (email automation service)
- pickle (memory dumping for saving data)
 
### How to naviguate the code
Start at **APIIntegration.py**, this is the main file of the code, from there, you can follow the method calls refering to other files inside folders such as ConsoleManagement, EmailHandling and Caching. (EXEMPLE: the code will often call methods from ConsoleManagement.ConsoleInput.py to manage user input.)

#### Other files:
The graph.png files are simply the generated graphs being emailed to the user, you don't need to care about them.
Output.md is the message generated in a mardown format by the API request to be sent to the user via email.
