# lambda-ansible
Setup AWS environment and deploy lambda

To run this deployment you need:

IAM user with following permissions:
  + AmazonRDSFullAccess
  + AWSLambdaFullAccess
  + IAMFullAccess
  + AmazonVPCFullAccess

Store your AWS credentials:
```shell
cat ~/.aws/credentials 
[default]
aws_access_key_id = ACCESKEY
aws_secret_access_key = SECRETKEY
```
For testing purpose you can also install awscli:
```shell
sudo pip install awscli
aws --version
aws configure
```
Add your account it to environment variables
```shell
export AWS_ACCOUNT_ID=122998
```
Virtual env
```shell
cd lambda-ansible
virtualenv lambda
source env/bin/activate 
echo $VIRTUAL_ENV
```
Install python dependencies
```shell
pip install -r /path/to/requirements.txt
```
After that you can run deployment:
```shell
ansible-playbook -i inventory/hosts aws.yml -e@secret_vars/secret.yml
```

Tips and Trics:
+ code/client.cfg store db credentials for lambda, host will be replaced after RDS setup
+ code/site-packeges contains psycopg2 with statically linked libpq.so, https://github.com/jkehler/awslambda-psycopg2 for details
+ ansible generate secret_vars/upsilon-test.yml with VPC,Subnets and RDS endpoint, which used as variables
