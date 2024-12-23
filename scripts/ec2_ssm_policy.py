import boto3
import argparse


def remove_ssm_policy_from_ec2(instance_id):
    """
    Checks if an EC2 instance has the SSM policy and removes it.
    :param instance_id: ID of the EC2 instance
    """
    ec2 = boto3.client("ec2")
    iam = boto3.client("iam")

    # Get the IAM profile of the instance
    response = ec2.describe_instances(InstanceIds=[instance_id])
    instance = response["Reservations"][0]["Instances"][0]

    # Check if the instance has an IAM profile
    if "IamInstanceProfile" not in instance:
        return (
            f"No IAM instance profile associated with instance {instance_id}"
        )

# Extract the role name from the instance profile ARN

    role_name = "SSMRole"

    # Disassociate SSM policy
    try:
        iam.detach_role_policy(
            RoleName=role_name,
            PolicyArn="arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore",
        )
        return f"Política SSM eliminada del rol {role_name}."
    except iam.exceptions.NoSuchEntityException:
        return (
            f"The role {role_name} cannot be found. "
            "Make sure the IAM role exists."
        )

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Remove SSM policy from an EC2 instance"
    )
    parser.add_argument(
        "--instance-id",
        required=True,
        help=("ID of the EC2 instance from which"
              " the SSM policy will be removed"),
    )
    args = parser.parse_args()
    instance_id = args.instance_id

    print(remove_ssm_policy_from_ec2(instance_id))
