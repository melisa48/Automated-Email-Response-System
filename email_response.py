import re
from typing import Dict, Tuple
from enum import Enum
import spacy

class EmailCategory(Enum):
    SUPPORT = "support"
    SALES = "sales"
    BILLING = "billing"
    GENERAL = "general"
    TECHNICAL = "technical"

class EmailProcessor:
    def __init__(self):
        # Load English language model for NLP
        self.nlp = spacy.load("en_core_web_sm")
        
        # Keywords for classification
        self.category_keywords = {
            EmailCategory.SUPPORT: ["help", "support", "issue", "problem", "trouble", "assist"],
            EmailCategory.SALES: ["purchase", "buy", "price", "quote", "sales", "cost"],
            EmailCategory.BILLING: ["invoice", "payment", "bill", "charge", "subscription", "plan"],
            EmailCategory.TECHNICAL: ["error", "bug", "technical", "login", "password", "access"],
            EmailCategory.GENERAL: ["information", "question", "inquiry", "contact", "hello", "hi"]
        }
        
        # Template responses for each category with proper spacing
        self.response_templates = {
            EmailCategory.TECHNICAL: """Dear {name},

Thank you for reporting the technical issue regarding "{subject}".

Our technical team has been notified and will investigate the matter. You can track the status of your report using reference number: {ticket_id}

For common technical solutions, please visit: tech-support.example.com

Best regards,
Technical Support Team""",
            
            EmailCategory.SUPPORT: """Dear {name},

Thank you for contacting our support team. We have received your request regarding "{subject}".

Our team will review your issue and get back to you within 24 hours. Your ticket number is: {ticket_id}

For immediate assistance, please check our FAQ at: support.example.com

Best regards,
Support Team""",
            
            EmailCategory.SALES: """Dear {name},

Thank you for your interest in our products/services. We're excited to help you with "{subject}".

One of our sales representatives will contact you shortly with detailed information about our offerings and pricing.

In the meantime, you can browse our product catalog at: products.example.com

Best regards,
Sales Team""",
            
            EmailCategory.BILLING: """Dear {name},

We've received your billing inquiry regarding "{subject}".

Our billing department will review your request and respond within 1 business day. For immediate access to your billing information, please visit our customer portal at: billing.example.com

Your reference number is: {ticket_id}

Best regards,
Billing Team""",
            
            EmailCategory.GENERAL: """Dear {name},

Thank you for your message regarding "{subject}".

We've received your inquiry and will route it to the appropriate department. You can expect a response within 1-2 business days.

Reference number: {ticket_id}

Best regards,
Customer Service Team"""
        }

    def extract_email_info(self, email_text: str) -> Dict[str, str]:
        """Extract name and other relevant information from email text."""
        name_match = re.search(r"From:\s*([\w\s]+?)(?:\n|$)", email_text, re.IGNORECASE)
        subject_match = re.search(r"Subject:\s*(.+?)(?:\n|$)", email_text, re.IGNORECASE)
        
        name = name_match.group(1).strip() if name_match else "Valued Customer"
        subject = subject_match.group(1).strip() if subject_match else "your inquiry"
        
        return {
            "name": name,
            "subject": subject
        }

    def categorize_email(self, email_text: str) -> EmailCategory:
        """Categorize email based on content using NLP."""
        doc = self.nlp(email_text.lower())
        category_scores = {category: 0 for category in EmailCategory}
        
        for token in doc:
            for category, keywords in self.category_keywords.items():
                if token.text in keywords:
                    category_scores[category] += 1
        
        best_category = max(category_scores.items(), key=lambda x: x[1])[0]
        return best_category if category_scores[best_category] > 0 else EmailCategory.GENERAL

    def generate_response(self, email_text: str) -> Tuple[EmailCategory, str]:
        """Generate appropriate response based on email category."""
        email_info = self.extract_email_info(email_text)
        category = self.categorize_email(email_text)
        
        import random
        ticket_id = f"TKT-{random.randint(10000, 99999)}"
        
        response = self.response_templates[category].format(
            name=email_info["name"],
            subject=email_info["subject"],
            ticket_id=ticket_id
        )
        
        # Ensure consistent line breaks
        response = '\n'.join(line.strip() for line in response.split('\n'))
        return category, response

def main():
    processor = EmailProcessor()
    
    sample_email = """
    From: John Smith
    Subject: Cannot login to my account
    
    Hi,
    I'm having trouble logging into my account. I've tried resetting my password
    but I'm still getting an error message. Can you please help?
    
    Thanks,
    John
    """
    
    category, response = processor.generate_response(sample_email)
    print(f"Email Category: {category.value}\n")
    print("Generated Response:")
    print("-" * 60)
    print(response)
    print("-" * 60)

if __name__ == "__main__":
    main()