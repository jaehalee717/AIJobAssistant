"""
modules/prompt/career_library.py

AIJobAssistant
Version : v1.0.0
"""


class CareerLibrary:

    @staticmethod
    def build() -> str:

        return """
==================================================
VERIFIED CAREER LIBRARY
==================================================

TAI
--------------------------------------------------
Industry
- Higher Education
- Creative Arts Education

Strengths
- IT Operations
- Infrastructure
- Microsoft 365 Administration
- Google Workspace
- IAM
- MFA
- SSO
- JAMF
- Endpoint Management
- Information Security
- Vendor Management
- Service Delivery
- User Support

Leadership
- IT Manager
- Cross-functional Collaboration
- Stakeholder Communication

--------------------------------------------------

LG Electronics Brazil

Industry
- Manufacturing

Strengths
- Regional IT Management
- Information Security
- Azure
- Power BI
- RPA
- LGPD
- Infrastructure
- Network
- ERP
- Vendor Management
- Service Delivery
- Digital Transformation

Leadership
- Senior Manager
- Regional Leadership
- Budget Management
- Team Leadership

--------------------------------------------------

LG Electronics Spain

Industry
- Manufacturing

Strengths
- Oracle ERP
- Infrastructure
- GDPR
- Network
- Service Delivery
- IT Operations
- Information Security
- Vendor Management

Leadership
- Senior Manager
- European Operations
- Project Leadership

--------------------------------------------------

BANKePOST

Industry
- Financial Services

Strengths
- Banking Systems
- Financial IT

--------------------------------------------------

LG Internet

Industry
- Internet Services

Strengths
- eCommerce
- Internet Services
- Web Operations

--------------------------------------------------

LG Electronics Korea

Industry
- Electronics

Strengths
- Software
- Multimedia
- Engineering

==================================================
Always use this library when matching Job Description requirements.
Never assign experience to the wrong company.
Never invent evidence.
==================================================
""".strip()