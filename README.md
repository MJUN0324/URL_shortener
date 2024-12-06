# URL_shortener

![url_shortner](https://github.com/user-attachments/assets/c66d5c78-0418-45ea-affa-9b1f2daa4928)

## Architecture

[comment]: <![URLShortner_Architecture drawio](https://github.com/user-attachments/assets/36c24a77-e178-4187-975e-6a4b541603a1)>

<p align="center"><img src="https://github.com/user-attachments/assets/36c24a77-e178-4187-975e-6a4b541603a1"</p>

---

## Website URL

URL Shortner: [https://shorturlapi-urlshortn-364405424984.s3.us-east-1.amazonaws.com/index.html](https://shorturlapi-urlshortn-364405424984.s3.us-east-1.amazonaws.com/index.html)

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
git clone https://github.com/MegazoneCloud-HKG-Hiring/assignment-jun-miyajima.git
cd assignment-jun-miyajima
```

## AWS SAM Template

### 1. Build the SAM Application

Navigate to the aws directory

```bash
cd aws
```

Build the SAM template

```bash
sam build
```

### 2. Deploy the SAM Application

To deploy the backend to AWS, run:

```bash
sam deploy --guided --capabilities CAPABILITY_NAMED_IAM
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

**AWS Console**

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

| Service     | Estimated Monthly Cost (USD) |
| ----------- | ---------------------------- |
| AWS Lambda  | $0.00                        |
| API Gateway | $1.00                        |
| Amazon S3   | $2.24                        |
| DynamoDB    | $0.82                        |
| **Total**   | **$4.06**                    |

My Estimate: [Download PDF](https://github.com/user-attachments/files/18025902/8adba10c-1ee5-4929-8b69-eb5819102970.pdf), [link](https://calculator.aws/#/estimate?id=a5a8f9c5812dfbbdf0ab2857da1627ce00674cbe)

For more accurate estimate, please use the [AWS Pricing Calculator](https://calculator.aws/#/).

## License
This project is licensed under the MIT License - see the `LICENSE` file for details.
