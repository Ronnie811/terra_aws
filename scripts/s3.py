import boto3


def remove_public_access_s3(bucket_name):
    """
    Checks if the bucket has public access and deletes it.
    :param bucket_name: Name of the S3 bucket
    """
    s3 = boto3.client("s3")
    acl = s3.get_bucket_acl(Bucket=bucket_name)

    # We check if the bucket has public access
    for grant in acl["Grants"]:
        if "URI" in grant["Grantee"] and "AllUsers" in grant["Grantee"]["URI"]:
            print(f"Public access detected on bucket {bucket_name}. Removing access...")
            s3.put_bucket_acl(Bucket=bucket_name, ACL="private")
            return f"Public access removed from bucket {bucket_name}"

    return f"The bucket {bucket_name} does not have public access."


if __name__ == "__main__":
    bucket = "public-bucket-example-unique-7"  # Change to the name of your bucket
    print(remove_public_access_s3(bucket))
