# Project Overview

First I went digging for info on LangServe, honestly, I wasn't really familiar with it. After searching through the docs and finding a pretty fresh forum post with a getting-started guide, I kicked things off.

I started by testing the basic RAG chain just to see if it worked. Once I saw it's doing well, I began organizing the project, applying some design patterns and cleaning up the code structure.
Then I Dockerized the app (because, well, easier to run and test) and spun it up to do some local checks. Once I confirmed it was running smoothly, I moved to deploy it on AWS. I ran into a few problems at first with AWS Copilot, so I switched gears and set up a VPC with EC2, that worked out. 

After everything was up and running, I put together the documentation. I figured a sequence diagram would be the best way to clearly show the message flow (from the user sending a question to the bot spitting back an answer), plus an architecture diagram to explain the setup.

## Main Challenges

* **Web Scraping**: Ensuring the scrape each url inside of https://www.promtior.ai/
* **Cloud Deployment**: Making the deployment stable on AWS using EC2.

## You can test this project here: 
```bash
http://ec2-3-14-71-186.us-east-2.compute.amazonaws.com:8080/promtior/playground/
```

## Technologies Used

* LangChain, LangServe
* OpenAI API
* Docker, AWS (EC2, VPC)