# pd2jira_python [![Build Status](https://travis-ci.org/sbraverman/pd2jira_python.svg)](https://travis-ci.org/sbraverman/pd2jira_python)
Generate JIRA tickets from Pager Duty alerts using Amazon Web Services (AWS) Lambda!

## What is pd2jira\_python?
pd2jira\_python is an open source project that creates JIRA tickets from Pager Duty webhooks using AWS Lambda. This is a new option for making JIRA tickets from Pager Duty alerts.
No need to host the code on your personal server (unless you want to). 

pd2jira\_python uses the following technologies:
* Python2.7
* AWS Lambda
* AWS API Gateway
* PagerDuty Webhooks

## Let's get started!
pd2jira-python will be up and running within minutes. Just follow this guide!

1. Fork this project into your account and clone into local directory
  ``` bash 
  git clone git@github.com:<your_github_handle>/pd2jira-python.git
  ```
_note: replace <your_github_handle> with your Github handle_

2. Replace the comments in the Configs file with your credentials
_pd2jira-python/pd2jira-python/configs.yml_
Explanations:
  * jira_url -- the site which your JIRA application is hosted from
  * jira_username -- Username for which the JIRA tickets will be "created by." User must be registered with your JIRA account. 
  * jira_password -- Password for the above user. 
  * jira_project -- the project for which the ticket will be generated for. If DEVOPS was your project, ticket URL would be: https://<your_jira_site>.jira.com/browse/DEVOPS-6756 
  * Examples (from explanations above):
  ``` yaml
  jira_url: https://<your_jira_site>.jira.com 
  jira_username: Team_Account
  jira_password: topsecretpassword
  jira_project: DEVOPS
  ```
  Add custom configurations! (Look at configs.yml for example. 

3. Download dependencies and package project together into zip file: lambda.zip
  _inside project root directory:_
  ``` bash
  bash setup.sh
  ```  

4. Upload lambda file to AWS
  1. Log into your AWS account and navigate to Lambda
  2. Click on "Create a Lambda Function"
  3. Select Python 2.7 as language and "microsoft-http-endpoint" blueprint. Click next.
  4. Configure your Lambda function. Give it a name and description.
  5. For Lambda function code, select zip file. Upload the lambda.zip file from Step 3.
  6. Set Lambda function handler and code
    * Handler: alertToTicket.lambda_handler
    * Role: "lambda_basic_execution"
  7. Advanced settings. 128mb and 5 seconds should be plenty. 
  8. No VPC necessary
  9. Configure Endpoints -- The only defaults that need to be changed:
    * Method: Post
    * Security: Open 
  10. Review and submit. Lambda is set up!
  11. Navigate to "API Endpoints" and copy the API endpoint URL (you will need this for the next step). 

5. Set up Pager Duty webhook.
  1. Navigate to your Pager Duty account
  1. Select a service you would like to create JIRA tickets from or create a new service
  2. Click on "Add Webhook"
  3. Give your webhook a name and paste the URL from the previous step. If you forgot to copy the API endpoint URL, go to AWS, navigate to Lambda, select your newly created Lambda function, and click on "API Endpoints."
  4. You are done! Let's test it out

## Test your Lambda function
1. In Pager Duty, navigate to the service you added the webhook to.
2. Trigger an alert. NOTE: Make sure the person you are about to alert is aware that you are testing. You may want to create a new service or temporarily set yourself up as the on-call scheduled person. 
4. Go to JIRA and ensure your ticket was generated correctly. If you see your ticket, SUCCESS! If your new ticket was not created within 5 seconds, continue to the next step. 
3. Log in to AWS. Navigate to your Lambda function. Click on "Monitoring." Click on "View Logs in CloudWatch"
4. View the log stream that was generated. This will give you some ideas as to why your ticket failed to be generated. Most likely, there are some custom fields you need to set to create tickets or your Configs were not properly configured. When you update the code, you will have to run the setup.sh again and reupload the zip file.  


## Running tests
1. To run the unit tests you must be in the project root directory and have nose installed

  ```
  nosetests tests/ 
  ``` 

## Contributing
1. Fork the repository.
2. Make your changes.
3. Add unit tests.
4. Ensure unit tests pass.
5. Submit pull-request. Please make sure your commit message contains a helpful comment. Please ensure you add a comment alongside your pull-request showing proof that your code works.

