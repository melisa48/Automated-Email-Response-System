# Automated Email Response System
This Python-based system automatically categorizes incoming emails and generates appropriate responses based on the content. It uses Natural Language Processing (NLP) to analyze email content and classify it into different categories, then generates customized responses using pre-defined templates.

## Features
- Email categorization using NLP (spaCy)
- Automatic response generation with customized templates
- Support for multiple categories:
  - Technical Support
  - Customer Support
  - Sales
  - Billing
  - General Inquiries
- Automatic ticket number generation
- Professional email formatting
- Name and subject extraction from email headers

## Requirements
- Python 3.6 or higher
- spaCy library and English language model
- Regular expression support (built into Python)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/automated-email-response.git
cd automated-email-response
```

2. Install required packages:
```bash
pip install spacy
python -m spacy download en_core_web_sm
```

## Usage: 
### Email Format Requirements
The system expects emails to contain:
- From: [sender's name]
- Subject: [email subject]
- Body of the email

## Customization

### Adding New Categories
To add a new category:
1. Add it to the EmailCategory enum
2. Add relevant keywords to category_keywords in EmailProcessor
3. Create a response template in response_templates

### Modifying Templates
Response templates can be modified in the `EmailProcessor` class:
```python
self.response_templates = {
    EmailCategory.TECHNICAL: """
    Dear {name},

    Thank you for reporting the technical issue regarding "{subject}"...
    """
    # Add more templates here
}
```

## Response Categories

1. **Technical Support**
   - Handles: Login issues, technical errors, password problems
   - Generates: Technical support ticket

2. **Customer Support**
   - Handles: General help requests, product assistance
   - Generates: Support ticket with FAQ reference

3. **Sales**
   - Handles: Product inquiries, pricing questions
   - Generates: Sales team referral

4. **Billing**
   - Handles: Payment issues, invoice requests
   - Generates: Billing reference number

5. **General**
   - Handles: Miscellaneous inquiries
   - Generates: General acknowledgment with tracking number

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Author
- Melisa Sever

## Acknowledgments
- spaCy for Natural Language Processing
- Python Email Processing Libraries

## Contributing
Contributions to improve the Automated Email Response System is welcome. Please feel free to submit pull requests or open issues to discuss potential enhancements.
