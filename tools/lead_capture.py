"""
tools/lead_capture.py
Mock lead capture tool for AutoStream agent.
"""

import json
import re
from datetime import datetime


def mock_lead_capture(name: str, email: str, platform: str) -> dict:
    """
    Mock API function to capture a qualified lead.

    Args:
        name:     Full name of the lead
        email:    Email address of the lead
        platform: Creator platform (YouTube, Instagram, TikTok, etc.)

    Returns:
        dict with status and confirmation details
    """
    # Basic validation
    if not name or not email or not platform:
        return {
            "status": "error",
            "message": "All fields (name, email, platform) are required."
        }

    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if not re.match(email_pattern, email):
        return {
            "status": "error",
            "message": f"Invalid email address: {email}"
        }

    # Simulate successful lead capture
    lead_id = f"LEAD-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    print(f"\n{'='*50}")
    print(f"✅  Lead captured successfully: {name}, {email}, {platform}")
    print(f"    Lead ID : {lead_id}")
    print(f"    Time    : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*50}\n")

    return {
        "status": "success",
        "lead_id": lead_id,
        "name": name,
        "email": email,
        "platform": platform,
        "timestamp": datetime.now().isoformat(),
        "next_step": "A Sales representative will reach out within 24 hours."
    }
