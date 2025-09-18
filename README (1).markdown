# VulnShield - Cybersecurity Assistant & Automation System

VulnShield is an AI-powered cybersecurity assistant designed to streamline vulnerability scanning, patch management, and security reporting through an intuitive Telegram interface. By combining multiple AI agents, persistent PostgreSQL memory, automated PDF reporting, and Google Calendar integration, VulnShield provides a comprehensive solution for managing system security.

## 🌟 Key Features

- **Dual AI Agent System**: Two specialized Google Gemini AI agents handle command processing and cybersecurity tasks.
- **Telegram Bot Interface**: Interactive chat-based interface for seamless security management.
- **Automated Vulnerability Scanning**: Identifies CVEs in installed software with severity assessments.
- **Intelligent Patch Management**: Recommends and applies security patches with a confirmation workflow.
- **PDF Report Generation**: Generates professional security reports via APITemplate.io.
- **Persistent Memory**: Stores conversation context in a PostgreSQL database.
- **Google Calendar Integration**: Automatically schedules security actions as calendar events.
- **Whitelist Security Model**: Strictly validates commands with safety flags to ensure secure operations.

## 🏗️ System Architecture

```
Telegram User → Telegram Trigger → AI Agent 1 (Command Validator) → Switch Node
    ↓ ↓
    └─ Safe Commands → HTTP Request → AI Agent 2 (Cybersecurity) → PDF Report → Telegram Document
    └─ Casual Chat → Telegram Message
    └─ Dangerous Commands → Blocked Response
```

## 🔧 Installation & Setup

### Prerequisites

- n8n instance with access to custom nodes
- PostgreSQL database
- Telegram Bot Token
- Google Gemini API key
- Google Calendar OAuth credentials
- APITemplate.io account

### Installation Steps

1. **Import the Workflow**  
   Import the provided JSON workflow into your n8n instance.

2. **Set up Credentials**  
   Configure the following credentials in n8n:
   - Google Gemini (PaLM) API
   - PostgreSQL database
   - Telegram Bot API
   - Google Calendar OAuth
   - APITemplate.io API

3. **Database Setup**  
   Create the `chat_memory` table in your PostgreSQL database:

   ```sql
   CREATE TABLE chat_memory (
       session_id VARCHAR(255) NOT NULL,
       memory_data JSONB,
       created_at TIMESTAMP DEFAULT NOW(),
       updated_at TIMESTAMP DEFAULT NOW()
   );
   ```

4. **Environment Configuration**  
   - Ensure all API endpoints and webhooks are properly configured.
   - Set up SSL for production environments.

## 🚀 Usage

### Starting a Conversation
Interact with the Telegram bot by sending a message:

```
/user: Hi
/bot: Hi! Would you like me to scan your system for vulnerabilities now?
```

### Available Commands
- **List Installed Software**: `Show me installed software`
- **Scan for Vulnerabilities**: `Scan my system for vulnerabilities`
- **Apply Patches**: `Update my software`

### Example Workflow
1. User sends a command via Telegram.
2. AI Agent 1 validates the command against whitelist rules.
3. Safe commands are forwarded to AI Agent 2 for security task execution.
4. Vulnerability scan is performed.
5. A PDF report is generated and sent via Telegram.
6. A Google Calendar event is scheduled for the action.

## 🔒 Security Features

- **Command Whitelisting**: Only pre-approved commands are executed.
- **Danger Detection**: Flags and blocks harmful requests.
- **Confirmation Requirements**: Requires confirmation before critical actions.
- **No Shell Access**: Prevents execution of arbitrary system commands.
- **Audit Logging**: Logs all actions for accountability.

## 📊 Report Format
Generated PDF reports include:
- Executive summary of vulnerabilities
- Prioritized vulnerability table with severity ratings
- Patch recommendations with risk scores
- Update history and applied changes
- Color-coded risk assessment:
  - 🔴 Red: 9–10
  - 🟡 Yellow: 5–8
  - 🟢 Green: 1–4

## 🛠️ Technical Components

- **AI Agents**:
  - Agent 1: Command validation and user interaction
  - Agent 2: Cybersecurity task execution
- **Integration Nodes**:
  - Telegram: Communication interface
  - PostgreSQL: Persistent chat memory
  - Google Calendar: Event scheduling
  - APITemplate.io: PDF report generation
  - HTTP Request: External API communication
- **Custom Python Server**: Flask server for web command execution (use cautiously in production).

## ⚙️ Configuration

### Environment Variables

```bash
export DATABASE_URL="postgresql://user:pass@host:port/db"
export TELEGRAM_TOKEN="your_telegram_bot_token"
export GEMINI_API_KEY="your_gemini_api_key"
```

### n8n Credentials Setup
Configure the following in n8n:
- Google Gemini API
- PostgreSQL database
- Telegram Bot API
- Google Calendar OAuth2
- APITemplate.io API

## 📈 Performance Considerations

- Add PostgreSQL indexing on `session_id` for efficient memory retrieval.
- Implement Gemini API rate limiting handling.
- Optimize Telegram message processing.
- Use caching strategies for PDF generation.

## 🔮 Future Enhancements

- Multi-language support
- Integration with additional vulnerability databases
- Advanced patch rollout strategies
- Team collaboration features
- Mobile application interface
- Advanced analytics dashboard
- SIEM integration
- Automated compliance reporting

## 🆘 Troubleshooting

### Common Issues
- **Webhook Errors**: Verify Telegram webhook configuration.
- **Database Connection**: Check PostgreSQL connection string.
- **API Limits**: Monitor Gemini API quotas.
- **Memory Issues**: Optimize PostgreSQL retention policies.

### Debug Mode

```bash
export N8N_LOG_LEVEL=debug
```

## 📝 License
This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Contributions are welcome! Please submit pull requests, open issues, or suggest new features.

## 🏆 Acknowledgments
- n8n for workflow automation
- Google Gemini for AI capabilities
- Telegram for Bot API
- APITemplate.io for PDF generation

## ⚠️ Warning
This system executes security-related actions. Always test in a controlled environment before deploying to production. The developers are not responsible for any security incidents caused by misconfiguration or misuse.