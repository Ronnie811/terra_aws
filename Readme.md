
# AWS Resource Validation Challenge

This project consists of Python scripts to validate and manage AWS resources using `boto3`. The aim is to identify and mitigate potential misconfigurations in an AWS environment. The repository also includes Terraform configurations to provision the required AWS resources for testing and unit tests for validating the scripts.

---

## **Table of Contents**
1. [Description](#description)
2. [Project Structure](#project-structure)
3. [Terraform Implementation](#terraform-implementation)
4. [Python Scripts](#python-scripts)
5. [Unit Tests](#unit-tests)
6. [Setup and Usage](#setup-and-usage)
7. [Contributing](#contributing)

---

## **Description**

The challenge includes three main tasks:

1. **S3 Bucket Validation**: Ensure S3 buckets do not have public access; remove it if detected.
2. **RDS Public Access Validation**: Verify RDS instances are not publicly accessible; modify settings to restrict access if needed.
3. **EC2 IAM Role Validation**: Check if EC2 instances have the `AmazonSSMManagedInstanceCore` policy attached to their roles and detach it if found.

---

## **Project Structure**

```plaintext
.
├── terraform/                      # Terraform configurations
│   ├── main.tf                     # Main Terraform file
├── scripts/                        # Python scripts for resource validation
│   ├── s3.py                       # S3 bucket validation script
│   ├── rds.py                      # RDS public access validation script
│   └── ec2_ssm_policy.py           # EC2 IAM role validation script
├── tests/                          # Unit tests for Python scripts
│   ├── test_s3.py                  # Unit tests for s3.py
│   ├── test_rds.py                 # Unit tests for rds.py
│   └── test_ec2_ssm_policy.py      # Unit tests for ec2_ssm_policy.py
├── README.md                       # Project documentation
└── venv                            # Python dependencies
```

---

## **Terraform Implementation**

### **Description**

The `terraform/` directory includes configurations to provision the following AWS resources:
- **S3 Buckets**: Two buckets, one with and one without public access.
- **RDS Instance**: A MySQL database instance with configurable public access.
- **EC2 Instance**: An instance associated with an IAM instance profile containing the `AmazonSSMManagedInstanceCore` policy.

### **Setup**

1. **Prerequisites**:
   - Install Terraform.
   - Configure AWS credentials with required permissions.

2. **Steps**:
   - Navigate to the `terraform/` directory.
   - Run the following commands:
     ```bash
     terraform init
     terraform plan
     terraform apply
     ```

3. **Outputs**:
   Upon successful provisioning, Terraform provides:
   - S3 bucket names
   - RDS instance identifier
   - EC2 instance ID and profile name

---

## **Python Scripts**

### **1. s3.py**
- Identifies S3 buckets with public access and removes permissions if detected.
- **Usage**:
  ```bash
  python scripts/s3.py
  ```

### **2. rds.py**
- Verifies RDS instances for public accessibility and disables it if found.
- **Usage**:
  ```bash
  python scripts/rds.py
  ```

### **3. ec2_ssm_policy.py**
- Validates IAM roles associated with EC2 instances and detaches the `AmazonSSMManagedInstanceCore` policy if found.
- **Usage**:
  ```bash
  python scripts/ec2_ssm_policy.py --instance-id <EC2_INSTANCE_ID>
  ```

---

## **Unit Tests**

Unit tests ensure script functionality. Located in the `tests/` directory:

1. **test_s3.py**:
   - Tests the `s3.py` script.

2. **test_rds.py**:
   - Tests the `rds.py` script.

3. **test_ec2_ssm_policy.py**:
   - Tests the `ec2_ssm_policy.py` script.

### **Running Tests**

Install `pytest` and execute:
```bash
pytest tests/
```

---

## **Setup and Usage**

### **Prerequisites**
- Install Python 3.13.1 or higher.
- Install dependencies:
  ```bash
  pip install black flake8 boto3 pytest moto
  ```

### **AWS Configuration**
- Ensure AWS credentials are set up via AWS CLI or environment variables.

### **Running Scripts**
- Navigate to the `scripts/` directory and execute the desired script as needed.

---

## **Contributing**

Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b master
   ```
3. Commit changes:
   ```bash
   git commit -m "Add something"
   ```
4. Push to the branch:
   ```bash
   git push origin master
   ```
5. Open a pull request.

---

## **License**

This project is licensed under the MIT License.