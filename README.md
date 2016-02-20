# pd2jira-python
Generate JIRA tickets from Pager Duty alerts using Amazon Web Services (AWS) Lambda!

## What is pd2jira-python?
pd2jira-python is an open source project that creates JIRA tickets from Pager Duty webhooks
No need to host the code on your personal server (unless you want to).

pd2jira-python uses the following technologies:
* Python2.7
* AWS Lambda
* AWS API Gateway
* PagerDuty Webhooks

## Let's Get Started!
pd2jira-python will be up and running within minutes. Just follow this guide!

1. Clone this project into desired local directory
``` bash 
git clone git@github.com:sbraverman/pd2jira-python.git
```

2. Replace the comments in the Configs file with your credentials
_pd2jira-python/pd2jira-python/Configs.yml_
Explanations:
* jira_url -- the site which your JIRA application is hosted from
* jira_username -- Username for which the JIRA tickets will be "created by." User must be registered with your JIRA account. 
* jira_password -- Password for the above user. 
* jira_project -- the project for which the ticket will be generated for. If DEVOPS was your project, ticket URL would be: https://<your_jira_site>.jira.com/browse/DEVOPS-6756 
Examples (from explanations above):
``` yaml
jira_url: https://<your_jira_site>.jira.com 
jira_username: Team_Account
jira_password: topsecretpassword
jira_project: DEVOPS
```

3. Download dependencies and package project together into zip file: lambda.zip
_inside project root directory_
``` bash
bash setup.sh
```  

4. Upload lambda file to AWS
  1. Log into your AWS account and navigate to Lambda
  2. Click on "Create a Lambda Function"
  3. Select Python 2.7 as language and "microsoft-http-endpoint." Click next.
  4. Configure your Lambda function. Give it a name and description.
  5. For Lambda function code, select zip file. Upload the lambda.zip file from Step 3.
  6. Set Lambda function handler and code
    * Handler: alertToTicket.lambda_handler
    * Role should be: "lambda_basic_execution"
  7. Advanced settings. 128mb and 5 seconds should be plenty. 
  8. No VPC necessary
  9. Configure Endpoints -- The only defaults that need to be changed:
    * Method: Post
    * Security: Open 
  10. Review and submit. Lambda is set up!
  11. Navigate to "API Endpoints" and copy the API endpoint URL (you will need this in the next step). 

5. Set up Pager Duty webhook.
  1. Select a service you would like to create ticket or create a new one
  2. Click on "Add Webhook"
  3. Give your webhook a name and paste the URL from step 11 in. If you forgot to copy the API endpoint URL, go to AWS, navigate to Lambda, select your newly created Lambda function, and click on "API Endpoints."
  4. You are done! Let's test it out

## Test your Lambda function
  1. In Pager Duty, navigate to the alert you set the webhook up with.
  2. Trigger an alert. NOTE: Make sure the person you are about to alert is aware that you are testing. You may want to create a new service or temporarily set yourself up as the on-call scheduled person. 
  4. Go to JIRA and ensure your ticket was generated correctly. If you see your ticket, SUCCESS! If your new ticket was not created within 5 seconds, continue to the next step. 
  3. Log in to AWS. Navigate to your Lambda function. Click on "Monitoring." Click on "View Logs in CloudWatch"
  4. View the log stream that was generated. This will give you an idea of why your ticket was not generated. Most likely, there are some custom fields you need to set to create tickets or your Configs were not set up properly. When you update the code, you will have to run the setup.sh again and reupload the zip file.  
  5. The next step you can do is make sure your custom_fields are properly set

