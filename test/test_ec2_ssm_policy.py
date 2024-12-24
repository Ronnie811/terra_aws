import pytest
from scripts.ec2_ssm_policy import remove_ssm_policy_from_ec2
from moto import mock_aws
import boto3


@pytest.fixture
def ec2_setup():
    with mock_aws():
        ec2 = boto3.client("ec2")
        iam = boto3.client("iam")

        # Create a sample EC2 instance
        instance = ec2.run_instances(
            ImageId="ami-0abcdef1234567890",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
        )

        # Create an IAM role and associate it with the EC2 instance
        # role = iam.create_role(RoleName="EC2Role",
        # AssumeRolePolicyDocument="{}")

        ec2_instance_id = instance["Instances"][0]["InstanceId"]
        ec2.associate_iam_instance_profile(
            IamInstanceProfile={"Name": "EC2Role"}, InstanceId=ec2_instance_id
        )

        # Attach SSM policy to role
        iam.attach_role_policy(
            RoleName="EC2Role",
            PolicyArn="arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
        )

        yield ec2, iam, ec2_instance_id


def test_remove_ssm_policy_from_ec2(ec2_setup):
    ec2, iam, instance_id = ec2_setup
    result = remove_ssm_policy_from_ec2(instance_id)

    # Verify that the SSM policy has been unlinked
    policies = iam.list_attached_role_policies(RoleName="EC2Role")
    ssm_policy_attached = any(
        policy["PolicyArn"] == (
            "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
        )
        for policy in policies["AttachedPolicies"]
    )

    assert not ssm_policy_attached
    assert "SSM policy removed" in result
