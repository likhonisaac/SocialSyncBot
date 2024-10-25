# 🚀 SocialSyncBot

Automated social media management tool that synchronizes posts across multiple platforms.

## Features
- 🔄 Cross-platform posting (Twitter, Telegram)
- 🔒 Secure API authentication
- 📊 Analytics tracking
- 💎 Crypto donation integration

## Quick Start

1. Clone the repository:
```bash
git clone https://github.com/likhonisaac/SocialSyncBot.git
cd SocialSyncBot
```

2. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
flask run
```

## API Usage

Post to multiple platforms:
```bash
curl -X POST http://localhost:5000/api/sync \
  -H "X-API-Key: your-api-key" \
  -H "Content-Type: application/json" \
  -d '{"content": "Hello World!", "platforms": ["twitter", "telegram"]}'
```

## Deployment

The app automatically deploys to Heroku when pushing to the main branch.

## Support
ETH: `0x00fC876d03172279E04CC30E5edCE103c3d23C1A`

## Author
Created by Likhon Sheikh
