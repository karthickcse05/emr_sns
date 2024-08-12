import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('emr')
    response = client.list_instances(
        ClusterId='',
        InstanceGroupTypes=['MASTER'],
        InstanceStates=['RUNNING']
    )
    print(response)
    ec2_instance_id = []
    if len(response['Instances']) > 0 :
        for instance in response['instances']:
            print(instance['Ec2InstanceId'])
            ec2_instance_id.append(instance['Ec2InstanceId'])
        
        mail_message = (
                        f"The following EC2 instances {ec2_instance_id} has been active in EMR\n"
                        )
        print(mail_message)
        mail_subject= 'EC2 instance in EMR !!!'
        topicARN = ''
        client_sns = boto3.client('sns')
        client_sns.publish(Message=mail_message,
                    Subject=mail_subject,
                    TopicArn=topicARN)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
