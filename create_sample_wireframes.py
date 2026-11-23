"""
Generates clean, authentic wireframe sketch sample images using PIL
for immediate 1-click testing in the Streamlit Capstone dashboard.
"""

import os
from PIL import Image, ImageDraw, ImageFont


def create_samples():
    os.makedirs("samples", exist_ok=True)

    # 1. Login Form Wireframe
    img_login = Image.new("RGB", (600, 750), color=(250, 250, 250))
    d = ImageDraw.Draw(img_login)
    
    # Outer Card
    d.rectangle([80, 80, 520, 670], outline=(60, 60, 60), width=3)
    # Avatar / Logo Circle
    d.ellipse([260, 120, 340, 200], outline=(80, 80, 80), width=3)
    # Title line
    d.text((230, 220), "USER LOGIN", fill=(40, 40, 40))
    # Subtitle line
    d.rectangle([200, 250, 400, 255], fill=(180, 180, 180))
    
    # Email label & input
    d.text((120, 295), "Email / Username", fill=(70, 70, 70))
    d.rectangle([120, 320, 480, 370], outline=(80, 80, 80), width=2)
    
    # Password label & input
    d.text((120, 400), "Password", fill=(70, 70, 70))
    d.rectangle([120, 425, 480, 475], outline=(80, 80, 80), width=2)
    
    # Checkbox
    d.rectangle([120, 500, 138, 518], outline=(80, 80, 80), width=2)
    d.text((150, 502), "Remember me", fill=(90, 90, 90))
    d.text((380, 502), "Forgot?", fill=(90, 90, 90))
    
    # Submit Button (Bold filled rectangle with rounded corners)
    d.rounded_rectangle([120, 545, 480, 605], radius=10, fill=(40, 40, 40))
    d.text((265, 565), "SIGN IN", fill=(255, 255, 255))
    
    # Footer link
    d.text((210, 630), "Don't have an account? Sign Up", fill=(100, 100, 100))
    img_login.save("samples/login_wireframe.png")

    # 2. E-Commerce Product Card Wireframe
    img_card = Image.new("RGB", (550, 700), color=(252, 252, 252))
    d = ImageDraw.Draw(img_card)
    
    # Card Border
    d.rounded_rectangle([60, 60, 490, 640], radius=12, outline=(50, 50, 50), width=3)
    # Image Placeholder Box with crossed lines
    d.rectangle([90, 90, 460, 360], outline=(80, 80, 80), width=2)
    d.line([90, 90, 460, 360], fill=(160, 160, 160), width=2)
    d.line([90, 360, 460, 90], fill=(160, 160, 160), width=2)
    d.text((220, 220), "[ Product Image ]", fill=(100, 100, 100))
    
    # Rating stars line
    d.text((95, 385), "**** (4.8 Rating)", fill=(120, 120, 120))
    # Product Title
    d.text((95, 420), "Wireless Noise-Canceling Headphones", fill=(30, 30, 30))
    # Description lines
    d.rectangle([95, 460, 450, 465], fill=(180, 180, 180))
    d.rectangle([95, 480, 380, 485], fill=(180, 180, 180))
    # Price
    d.text((95, 520), "$249.99", fill=(30, 30, 30))
    # Add to cart button
    d.rounded_rectangle([95, 560, 455, 615], radius=8, fill=(40, 40, 40))
    d.text((225, 580), "Add to Cart", fill=(255, 255, 255))
    img_card.save("samples/ecommerce_card.png")

    # 3. Analytics Dashboard Wireframe
    img_dash = Image.new("RGB", (900, 600), color=(250, 250, 250))
    d = ImageDraw.Draw(img_dash)
    
    # Sidebar
    d.rectangle([40, 40, 240, 560], outline=(60, 60, 60), width=3)
    d.text((70, 70), "LOGO / APP", fill=(30, 30, 30))
    d.rectangle([60, 110, 220, 113], fill=(150, 150, 150))
    # Nav items
    for i, item in enumerate(["[=] Dashboard", "[#] Analytics", "[o] Customers", "[*] Reports", "[@] Settings"]):
        d.text((70, 140 + i * 45), item, fill=(70, 70, 70))
        
    # Main Content Area
    d.rectangle([260, 40, 860, 560], outline=(60, 60, 60), width=3)
    # Topbar
    d.text((290, 65), "Dashboard Overview", fill=(30, 30, 30))
    d.rectangle([680, 60, 830, 95], outline=(80, 80, 80), width=2)
    d.text((700, 72), "[ Search... ]", fill=(120, 120, 120))
    
    # 3 Metric Cards
    for i, metric in enumerate(["Revenue: $45k", "Users: 12,800", "Growth: +18%"]):
        x1 = 290 + i * 185
        x2 = x1 + 170
        d.rounded_rectangle([x1, 120, x2, 210], radius=8, outline=(80, 80, 80), width=2)
        d.text((x1 + 20, 150), metric, fill=(40, 40, 40))
        
    # Big Chart Box
    d.rectangle([290, 240, 830, 530], outline=(80, 80, 80), width=2)
    d.text((310, 260), "Monthly Active Users Chart", fill=(80, 80, 80))
    # Trend wave
    d.line([320, 480, 420, 410, 520, 450, 640, 350, 750, 320, 800, 290], fill=(100, 100, 100), width=3)
    img_dash.save("samples/dashboard_wireframe.png")

    # 4. SaaS Landing Page Wireframe
    img_landing = Image.new("RGB", (900, 650), color=(252, 252, 252))
    d = ImageDraw.Draw(img_landing)
    # Header Navbar
    d.rectangle([40, 40, 860, 100], outline=(60, 60, 60), width=3)
    d.text((70, 65), "BrandName", fill=(30, 30, 30))
    d.text((380, 65), "Features   Pricing   About   Contact", fill=(80, 80, 80))
    d.rounded_rectangle([720, 55, 830, 90], radius=6, fill=(40, 40, 40))
    d.text((740, 65), "Sign Up", fill=(255, 255, 255))
    
    # Hero Title & Subtitle
    d.text((250, 150), "TRANSFORM SKETCHES TO CODE", fill=(20, 20, 20))
    d.rectangle([200, 190, 700, 195], fill=(180, 180, 180))
    d.rectangle([260, 210, 640, 215], fill=(180, 180, 180))
    # Hero CTA Buttons
    d.rounded_rectangle([320, 245, 450, 290], radius=8, fill=(40, 40, 40))
    d.text((345, 260), "Get Started", fill=(255, 255, 255))
    d.rounded_rectangle([470, 245, 590, 290], radius=8, outline=(80, 80, 80), width=2)
    d.text((495, 260), "Live Demo", fill=(50, 50, 50))
    
    # 3 Feature Grid Columns
    for i in range(3):
        x1 = 60 + i * 275
        x2 = x1 + 250
        d.rounded_rectangle([x1, 330, x2, 590], radius=10, outline=(80, 80, 80), width=2)
        # Icon circle
        d.ellipse([x1 + 95, 360, x1 + 155, 420], outline=(80, 80, 80), width=2)
        d.text((x1 + 65, 440), f"Feature {i+1} Title", fill=(30, 30, 30))
        d.rectangle([x1 + 30, 480, x2 - 30, 485], fill=(180, 180, 180))
        d.rectangle([x1 + 30, 500, x2 - 50, 505], fill=(180, 180, 180))
        d.rectangle([x1 + 30, 520, x2 - 40, 525], fill=(180, 180, 180))
    img_landing.save("samples/saas_landing_wireframe.png")

    print("Created 4 benchmark samples in samples/ successfully.")

if __name__ == "__main__":
    create_samples()
