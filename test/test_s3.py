import pytest
from scripts.s3 import remove_public_access_s3
from moto import mock_s3
import boto3


@pytest.fixture
def s3_setup():
    with mock_s3():
        s3 = boto3.client("s3")
        # Create a sample bucket
        s3.create_bucket(Bucket="public-bucket-example")
        # Assign a public ACL to the bucket
        s3.put_bucket_acl(Bucket="public-bucket-example", ACL="public-read")
        yield s3


def test_remove_public_access_s3(s3_setup):
    # Call script to remove public access
    result = remove_public_access_s3("public-bucket-example")
    # Verify that the result contains the deletion confirmation
    assert "Public access removed" in result
