import pytest
from scripts.rds import remove_public_access_rds
from moto import mock_rds
import boto3


@pytest.fixture
def rds_setup():
    with mock_rds():
        rds = boto3.client("rds")
        # Create a sample RDS instance
        rds.create_db_instance(
            DBInstanceIdentifier="public-rds-instance",
            DBInstanceClass="db.t2.micro",
            Engine="mysql",
            MasterUsername="admin",
            MasterUserPassword="password",
            PubliclyAccessible=True,
        )
        yield rds


def test_remove_public_access_rds(rds_setup):
    # Call script to remove public access
    result = remove_public_access_rds("public-rds-instance")
    # Verify that the result contains the deletion confirmation
    assert "Acceso público eliminado" in result
