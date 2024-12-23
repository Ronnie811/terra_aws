import boto3


def remove_public_access_rds(db_instance_identifier):
    """
    Checks if the RDS instance has public access and deletes it.
    :param db_instance_identifier: RDS instance ID
    """
    rds = boto3.client("rds")
    response = rds.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)
    instance = response["DBInstances"][0]

    if instance["PubliclyAccessible"]:
        print(
            f"Public access detected in RDS {db_instance_identifier}. Eliminando acceso..."
        )
        rds.modify_db_instance(
            DBInstanceIdentifier=db_instance_identifier,
            PubliclyAccessible=False,
            ApplyImmediately=True,
        )
        return f"Public access removed from RDS instance {db_instance_identifier}"

    return f"The RDS instance {db_instance_identifier} does not have public access."


if __name__ == "__main__":
    db_instance = (
        "terraform-20241223103804760700000001"  # Change to your RDS instance ID
    )
    print(remove_public_access_rds(db_instance))
