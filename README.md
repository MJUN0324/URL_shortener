# URL_shortener

## Architecture
![URLShortner_Architecture drawio](https://github.com/user-attachments/assets/36c24a77-e178-4187-975e-6a4b541603a1)

---

## Website URL 
[URL Shortner]()

---
## Prerequisites

Ensure you have the following tools installed:

- **AWS CLI** ([Installation Guide](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html))
- **AWS SAM CLI** ([Installation Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html))
- **Node.js** (v16 or higher) ([Download](https://nodejs.org/))
- **npm** (comes with Node.js)
- **Git** ([Download](https://git-scm.com/))

---

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/your-repo-name/project.git
cd project
```

## AWS SAM Template

### 1. Build the SAM Application

Navigate to the aws directory

```bash
cd backend
```

Build the SAM template

```bash
sam build
```

### 2. Deploy the SAM Application

To deploy the backend to AWS, run:

```bash
sam deploy --guided
```

## Frontend: Build and Deploy

### 1. Navigate to the Frontend Directory

```bash
cd frontend
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Build the Frontend Code

```bash
npm run build
```
This will create a build folder containing the production-ready files to copy to S3 bucket

### 4. Deploy the Frontend

**Option 1: Command Line**

1. Configure an S3 bucket
```bash
aws s3 mb s3://your-bucket-name
```

2. Deploy the frontend build:
```bash
aws s3 mb s3://your-bucket-name
```

3. Enable static website hosting:
```bash
aws s3 website s3://your-bucket-name --index-document index.html --error-document error.html
```
**Option 2: AWS Console**
1. Navigate to your S3 bucket created in backend section
2. Upload the build folders' files to the S3 bucket
3. Click Actions button
4. Click Make public using ACL

## Environment Variables
Ensure the following environment variables are set for local development and deployment:
| Variable Name | Description |
| ------------- | ----------- |
| `VITE_API_GATEWAY_URL` | Backend API endpoint URL. |

Set them in a `.env` file (for local use)

## Cost Estimate
| Service       | Estimated Monthly Cost (USD) |
| ------------- | ---------------------------- |
| AWS Lambda    | $2.00                        |
| API Gateway   | $3.50                        |
| Amazon S3     | $5.60                        |
| DynamoDB      | $15.00                       |
| **Total**     | **$26.10**                   |

For more accurate estimate, please use the [AWS Pricing Calculator](https://calculator.aws/#/).
