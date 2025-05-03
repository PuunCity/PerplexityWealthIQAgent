## What is the plan?
The plan is to create an AI agent (using Perplexity API) which will weekly send an email to it's users containing data of their asset of choice.

> [!important] Remember, don't depend on AI to "learn" or vibe code this project!

### Todo (things to learn):
- [x] How to integrate Perplexity's API
- [x] How to extract Mathplotlib code from Perplexity
- [x] Execute the graph code in a different environment
- [ ] Integrate the app as an email bot responding to email inputs
	- [ ] Receive emails
	- [ ] extract input
	- [ ] generate input
	- [ ] execute code as input
	- [x] output a .md file as the embedded email sent to the user
- [ ] Adjust the project to be respecting the teacher's guidelines
- [ ] Add more info ...
- [ ] Make the code more readable and apply logic for robust code
- [ ] Adjust the recommendations according to the budget of the user: (less than 1k... Over than 1k...)

## Refined project (Dictionary feature):
- The program starts with some console UI or maybe GUI welcoming the user (implement some art)
- The user logs in
- The user is prompted to either start a new query like usual to get an email
- or;
	- He can fetch data from his username and the program fetches the cache and outputs all of his previous queries summarized along with the dates when they were called (Use of dictionary)
## Issues and bugs:
- [x] cannot if user isn't satisfied with extracted input, the code just redisplays the same output

## How can users access the service?
Ideally, a website where users can connect and set their input in without having to actually send an email would be ideal.

But that means a website with a landing page should be made.


## How can agents filter out flukes and non-valid content?
To do...


## So far:
The bot can send emails with .md files attached to it. It can't yet receive emails with input and it can't yet attach .png files it generated, still a challenge.