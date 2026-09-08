import os
import re

meta = {
    "index.html": {
        "title": "Mobile Auto Locksmith London | Quick Turn Auto Keys", 
        "description": "Need a mobile auto locksmith in London? Quick Turn Auto Keys provides 24/7 car key replacement, programming, and emergency lockout services. We come to you."
    },
    "quote.html": {
        "title": "Get A Quote | 24/7 Mobile Auto Locksmith London UK", 
        "description": "Contact Quick Turn Auto Keys for 24/7 mobile car locksmith services in London. Call 07446 980720 for emergency car key replacement, lockouts, and more."
    },
    "services/car-key-cutting.html": {
        "title": "Car Key Cutting London | Mobile Spare Car Key Service", 
        "description": "Need a spare car key in London? Our mobile auto locksmiths provide precision car key cutting at your home or workplace. Get a reliable spare key today."
    },
    "services/car-key-programming.html": {
        "title": "Car Key Programming London | Transponder & Remote Fobs", 
        "description": "Expert mobile car key programming in London. We program transponder keys, remote fobs, and smart keys for a wide range of vehicles. Same-day service."
    },
    "services/car-key-replacement.html": {
        "title": "Car Key Replacement London | Mobile Auto Locksmith", 
        "description": "Fast and affordable mobile car key replacement in London. If you've broken or lost your key, our expert auto locksmiths cut and program replacements on site."
    },
    "services/eeprom-programming.html": {
        "title": "EEPROM Programming London | Advanced Car Key Programming", 
        "description": "Advanced EEPROM programming in London for lost keys and immobilized vehicles. We expertly recover data directly from your vehicle's ECU or immobiliser unit."
    },
    "services/emergency-car-lockout.html": {
        "title": "Emergency Car Lockout Service London | 24/7 Locksmith", 
        "description": "Locked your keys in the car in London? Our 24/7 emergency auto locksmiths use non-destructive entry methods to unlock your vehicle safely and quickly."
    },
    "services/ignition-repair.html": {
        "title": "Car Ignition Repair & Replacement London | Auto Locksmith", 
        "description": "Key stuck in the ignition or won't turn? Our mobile technicians provide professional car ignition repair and barrel replacement in London at your location."
    },
    "services/key-fob-repair.html": {
        "title": "Car Key Fob Repair & Replacement London | Mobile Locksmith", 
        "description": "Is your car key fob broken or unresponsive? We offer professional key fob repair, battery replacement, and reprogramming in London for all major vehicle makes."
    },
    "services/lost-car-keys.html": {
        "title": "Lost Car Keys Replacement London | No Spare Key Needed", 
        "description": "Lost your only car key in London? We can help. Our mobile auto locksmiths provide complete lost car key replacement and programming on-site to get you back."
    },
    "services/van-key-replacement.html": {
        "title": "Van Key Replacement London | Commercial Auto Locksmith", 
        "description": "Specialist van key replacement and commercial fleet locksmith services in London. We minimise downtime by coming directly to your business or breakdown location."
    },
    "brands/audi.html": {
        "title": "Audi Car Key Replacement London | 24/7 Auto Locksmith", 
        "description": "Lost your Audi key or locked out in London? Our mobile auto locksmiths provide 24/7 Audi car key replacement, cutting, and programming at your location."
    },
    "brands/bmw.html": {
        "title": "BMW Car Key Replacement London | 24/7 Auto Locksmith", 
        "description": "Lost your BMW key or locked out in London? Our mobile auto locksmiths provide 24/7 BMW car key replacement, cutting, and programming at your location."
    },
    "brands/ford.html": {
        "title": "Ford Car Key Replacement London | 24/7 Auto Locksmith", 
        "description": "Lost your Ford key or locked out in London? Our mobile auto locksmiths provide 24/7 Ford car key replacement, cutting, and programming at your location."
    },
    "brands/hyundai.html": {
        "title": "Hyundai Car Key Replacement London | Mobile Locksmith", 
        "description": "Lost your Hyundai key or locked out in London? Our mobile auto locksmiths provide 24/7 Hyundai car key replacement, cutting, and programming at your location."
    },
    "brands/kia.html": {
        "title": "Kia Car Key Replacement London | 24/7 Auto Locksmith", 
        "description": "Lost your Kia key or locked out in London? Our mobile auto locksmiths provide 24/7 Kia car key replacement, cutting, and programming at your location."
    },
    "brands/land-rover.html": {
        "title": "Land Rover Car Key Replacement London | Mobile Locksmith", 
        "description": "Lost your Land Rover key or locked out in London? Our mobile auto locksmiths provide 24/7 Land Rover car key replacement, cutting, and programming services."
    },
    "brands/mercedes.html": {
        "title": "Mercedes Car Key Replacement London | Mobile Locksmith", 
        "description": "Lost your Mercedes key or locked out in London? Our mobile auto locksmiths provide 24/7 Mercedes car key replacement, cutting, and programming at your location."
    },
    "brands/nissan.html": {
        "title": "Nissan Car Key Replacement London | Auto Locksmith", 
        "description": "Lost your Nissan key or locked out in London? Our mobile auto locksmiths provide 24/7 Nissan car key replacement, cutting, and programming at your location."
    },
    "brands/peugeot.html": {
        "title": "Peugeot Car Key Replacement London | Mobile Locksmith", 
        "description": "Lost your Peugeot key or locked out in London? Our mobile auto locksmiths provide 24/7 Peugeot car key replacement, cutting, and programming at your location."
    },
    "brands/renault.html": {
        "title": "Renault Car Key Replacement London | Mobile Locksmith", 
        "description": "Lost your Renault key or locked out in London? Our mobile auto locksmiths provide 24/7 Renault car key replacement, cutting, and programming at your location."
    },
    "brands/skoda.html": {
        "title": "Skoda Car Key Replacement London | 24/7 Auto Locksmith", 
        "description": "Lost your Skoda key or locked out in London? Our mobile auto locksmiths provide 24/7 Skoda car key replacement, cutting, and programming at your location."
    },
    "brands/toyota.html": {
        "title": "Toyota Car Key Replacement London | Auto Locksmith", 
        "description": "Lost your Toyota key or locked out in London? Our mobile auto locksmiths provide 24/7 Toyota car key replacement, cutting, and programming at your location."
    },
    "brands/vauxhall.html": {
        "title": "Vauxhall Car Key Replacement London | Mobile Locksmith", 
        "description": "Lost your Vauxhall key or locked out in London? Our mobile auto locksmiths provide 24/7 Vauxhall car key replacement, cutting, and programming at your location."
    },
    "brands/volkswagen.html": {
        "title": "Volkswagen Car Key Replacement London | Mobile Locksmith", 
        "description": "Lost your Volkswagen key or locked out in London? Our mobile auto locksmiths provide 24/7 Volkswagen car key replacement, cutting, and programming services."
    }
}

success_count = 0
for filepath, data in meta.items():
    if not os.path.exists(filepath):
        print(f"Error: File not found {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace Title
    content = re.sub(r'<title>(.*?)</title>', f'<title>{data["title"]}</title>', content, flags=re.IGNORECASE | re.DOTALL)
    # Replace Description
    content = re.sub(r'<meta\s+name="description"\s+content="([^"]+)">', f'<meta name="description"\n    content="{data["description"]}">', content, flags=re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    # Verification read
    with open(filepath, 'r', encoding='utf-8') as f:
        verify = f.read()
    
    t_match = re.search(r'<title>(.*?)</title>', verify, re.IGNORECASE | re.DOTALL)
    d_match = re.search(r'<meta\s+name="description"\s+content="([^"]+)">', verify, re.IGNORECASE)
    
    if t_match and d_match and t_match.group(1).strip() == data['title'] and d_match.group(1).strip().replace('\n', ' ') == data['description'].replace('\n', ' '):
        success_count += 1
    else:
        print(f"Failed verification for {filepath}")

print(f"Successfully injected and verified {success_count} files out of {len(meta)}.")
