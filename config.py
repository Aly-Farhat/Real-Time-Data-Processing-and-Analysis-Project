# Configuration File Explanation:
# This configuration dictionary contains the credentials required to authenticate and interact with AWS services.
# - 'AWS_ACCESS_KEY': Represents the access key ID, which is part of the credentials needed to access AWS resources.
# - 'AWS_SECRET_KEY': Represents the secret access key, which, together with the access key ID, provides secure access.


# How to Retrieve AWS Access Key and Secret Key:
# 1. Log in to the AWS Management Console: https://aws.amazon.com/console/
# 2. Navigate to "IAM" (Identity and Access Management) under AWS Services.
# 3. Go to "Users" and select your username.
# 4. Under the "Security Credentials" tab, click "Create Access Key."
# 5. Download the credentials or copy the Access Key ID and Secret Access Key for use.

 
# Note:
# For security purposes, it is highly recommended to avoid hardcoding sensitive information like AWS credentials directly in the code.
# Instead, use environment variables or a secure credential management service to protect your keys.

# How to Load the Environment Variables (On Windows):
# Search for "Environment Variables" in the Windows search bar and select "Edit the system environment variables."
# Click on "Environment Variables" in the System Properties dialog.
# Add New Variables:
# Under "System Variables" or "User Variables" (depending on whether you want these settings available to all users or just your account), click "New."
# Add the following variables:
#   Variable Name: AWS_ACCESS_KEY
#   Variable Value: Your actual AWS access key.
# Repeat for AWS_SECRET_KEY.
# Save and Restart:
# Click "OK" to save.
# Restart your code editor or terminal to ensure the environment variables are loaded.
# ---------------------------------------------------------------------------------------------------------------------------------------

import os

configuration = {
    'AWS_ACCESS_KEY': os.getenv('AWS_ACCESS_KEY'),
    'AWS_SECRET_KEY': os.getenv('AWS_SECRET_KEY')
}
