import glob
import re

brands_data = {
    "audi": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and VAG-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Audi vehicles utilize highly advanced immobilisers, from the early Megamos crypto systems to the latest MQB and MLB platforms. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's ECU or dashboard cluster must be accessed to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for the Volkswagen Audi Group (VAG). This allows us to securely bypass active immobilisers, extract the necessary Component Security (CS) codes, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Audi Key Problems</div>
      <h2>Common Audi Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Audi key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Key Stuck in Ignition</h3>
        <p>Older Audi models (like the early A3 or A4) occasionally suffer from steering lock housing or ignition barrel failure, trapping the key inside. We can safely extract the key, repair the barrel, and replace the housing if necessary on-site.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Smart Key De-synchronisation</h3>
        <p>Proximity "Advanced Keys" for the Q5, Q7, and modern A-series can lose sync with the vehicle due to battery depletion or interference. We provide mobile re-synchronisation to restore your keyless entry and push-to-start functions.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Flip Key Shells</h3>
        <p>Audi flip keys are prone to the hinge snapping or the remote buttons degrading over time. Instead of replacing the entire key, we can transfer your existing circuit board and transponder into a reinforced aftermarket shell and cut a fresh blade.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "bmw": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and BMW-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern BMW vehicles utilize some of the most sophisticated immobiliser networks in the industry, including EWS, CAS, and the latest FEM/BDC systems. If you lose your only key, a standard high-street key cutter cannot help because these advanced modules require direct communication or bench-programming to authorize a new key. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for BMW and MINI vehicles. This allows us to safely read ISN (Individual Serial Numbers), bypass active immobilisers, and program a new transponder or smart fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">BMW Key Problems</div>
      <h2>Common BMW Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of BMW key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>CAS / FEM Module Synchronisation</h3>
        <p>If your BMW cranks but won't start, or refuses to recognize the key entirely, the CAS or FEM/BDC module may have lost synchronization. We can perform on-site module testing, realignment, and key re-syncing to get the engine running.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Rechargeable Battery Failure (Diamond Keys)</h3>
        <p>Older E-Series BMWs use "diamond" shape keys with an internal rechargeable battery that degrades over time. If your remote stops locking/unlocking, we can cut open the sealed unit, replace the battery, and reseal it, or supply a brand new modern-style key.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Keyless Go Range Issues</h3>
        <p>Modern F and G-Series smart keys can suffer from reduced range or complete failure due to drops and water damage. We provide rapid diagnostic testing and replacement smart keys programmed directly to your vehicle's profile.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "ford": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and Ford-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Ford vehicles utilize highly secure PATS (Passive Anti-Theft System) immobilisers. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's ECU or BCM must be accessed directly through timed security access to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for European Ford models (including Transit vans). This allows us to securely bypass active immobilisers, clear lost keys from the system, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Ford Key Problems</div>
      <h2>Common Ford Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Ford key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Tibbe Lock &amp; Key Wear</h3>
        <p>Older Ford Transits, Fiestas, and Focuses use cylindrical "Tibbe" keys that wear down severely over time, eventually failing to turn the ignition or door locks. We can decode the original cuts from your lock and cut a fresh, factory-spec key blade to restore smooth operation.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Bonnet Lock Failure (Focus &amp; Mondeo)</h3>
        <p>Certain Ford models feature a unique key-operated bonnet release mechanism behind the front badge. These frequently jam or snap due to dirt and lack of lubrication. We can gain non-destructive entry to the engine bay and replace the mechanism.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Keyless Entry (KeyFree) Issues</h3>
        <p>Modern Fords equipped with KeyFree proximity systems can suffer from antenna faults or de-synchronized fobs. We provide full diagnostic testing and replacement smart keys to restore keyless functionality.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "kia": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Kia vehicles, much like their sister company Hyundai, utilize highly advanced rolling-code immobilisers and smart proximity systems. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's ECU must be accessed directly to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for Korean domestic and European-market Kia models. This allows us to securely bypass active immobilisers, extract the necessary PIN codes, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Kia Key Problems</div>
      <h2>Common Kia Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Kia key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Ignition Barrel Sticking</h3>
        <p>Many Kia models, particularly the older Picanto and Rio, suffer from worn ignition barrels where the key becomes difficult to insert or turn. We can safely remove the barrel, replace the worn wafers, and cut a fresh key on-site.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Flip Key Mechanisms</h3>
        <p>Kia flip keys are prone to the internal spring mechanism snapping, leaving the key blade dangling or stuck inside the shell. We can transfer your existing transponder chip and remote board into a brand-new aftermarket shell to save you the cost of a full replacement.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Smart Key De-synchronisation</h3>
        <p>Proximity keys for the Sportage, Sorento, and EV6 ranges can occasionally lose sync due to battery depletion. We provide mobile re-synchronisation and diagnostic testing to ensure your push-to-start functions work flawlessly.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "land-rover": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and JLR-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Land Rover and Range Rover vehicles utilize some of the most complex KVM (Keyless Vehicle Module) and ultra-wideband (UWB) security systems on the market to combat relay theft. If you lose your keys, standard programming tools often fail or permanently lock the modules. Our mobile auto locksmiths carry advanced, dealership-level diagnostic equipment tailored specifically for Jaguar Land Rover (JLR) vehicles. This allows us to safely communicate with the vehicle's DoIP (Diagnostics over Internet Protocol) network, replace or reset locked KVM modules if necessary, and program a new smart fob on the roadside—saving you the massive expense of main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Land Rover Key Problems</div>
      <h2>Common Land Rover Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Land Rover key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Locked KVM Modules (All Keys Lost)</h3>
        <p>On newer models (2015+), losing all your keys means the Keyless Vehicle Module locks itself for security. We have the specialist tools required to either safely virginise the existing module via EEPROM or program a replacement module on-site to accept new keys.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Smart Key Battery Drain</h3>
        <p>Certain Range Rover smart keys are known for draining their internal CR2032 batteries exceptionally fast due to constant RF polling. We can diagnose key faults, supply genuine replacements, and ensure the vehicle's receiver module is functioning correctly.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Emergency Blade Access</h3>
        <p>If your vehicle battery goes flat, the electronic door handles on models like the Velar won't present themselves. We can safely deploy the emergency physical key blade hidden inside your fob and decode the door lock to gain non-destructive entry.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "mercedes": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and Mercedes-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Mercedes vehicles utilize the highly secure DAS (Drive Authorization System) and FBS (Fahrberechtigungssystem) infrared immobilisers. If you lose your only key, a standard auto locksmith often cannot help because the Electronic Ignition Switch (EIS/EZS) requires complex cryptographic calculation to generate a new key track. Our mobile vans are equipped with specialist Mercedes bench-programming and IR tools. This allows us to safely extract the password from the EIS, calculate the key data, and program a new infrared fob on the roadside—saving you the expense and weeks of waiting associated with main dealer ordering from Germany.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Mercedes Key Problems</div>
      <h2>Common Mercedes Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Mercedes key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>EIS (Electronic Ignition Switch) Failure</h3>
        <p>If your key turns in the ignition but the dash lights don't come on and the car won't start, the EIS may be failing. We can diagnose whether the fault lies in the key or the ignition switch itself, and perform necessary repairs or replacements.</p>
      </div>
      <div class="reveal feature-item">
        <h3>ESL (Electronic Steering Lock) Motor Failure</h3>
        <p>A very common issue on the C-Class (W204) and E-Class (W212) is the steering lock motor burning out. You'll hear no "whirring" sound when inserting the key, and the car won't start. We can replace the motor or install a robust ESL emulator on-site to permanently fix the issue.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Infrared Key Damage</h3>
        <p>Mercedes keys rely on an infrared emitter at the tip of the key to communicate with the ignition. Dropping the key can easily shatter the internal coil or IR diode. We can supply and program brand-new, modern chrome-style replacement keys.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "nissan": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Nissan vehicles utilize advanced NATS (Nissan Anti-Theft System) immobilisers and Intelligent Key proximity modules. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's BCM (Body Control Module) requires a 20-digit rolling pin code to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for Nissan vehicles. This allows us to securely bypass active immobilisers, calculate the necessary PIN codes, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Nissan Key Problems</div>
      <h2>Common Nissan Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Nissan key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Twist-to-Start Ignition Wear</h3>
        <p>Many older Nissan Micras and Qashqais feature a plastic twist-knob ignition that allows you to start the car while the proximity key remains in your pocket. These knobs and the internal mechanical bypass locks frequently jam. We can repair or replace the barrel assembly on-site.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Intelligent Key De-synchronisation</h3>
        <p>Proximity keys for the Qashqai, Juke, and LEAF ranges can occasionally lose sync with the vehicle due to flat batteries or interference. We provide mobile re-synchronisation and diagnostic testing to ensure your keyless entry functions flawlessly.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Micro-Switches</h3>
        <p>The rubber buttons on standard Nissan remote keys often wear through, causing the delicate micro-switches underneath to snap off the circuit board. We can solder new switches onto the board and provide a brand-new casing to restore full functionality.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "peugeot": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and PSA-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Peugeot vehicles utilize complex BSI (Boîtier de Servitude Intelligent) multiplex modules for their immobiliser systems. If you lose your only key, a standard high-street key cutter cannot generate a new one because the BSI must be accessed directly to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for the PSA Group (Peugeot/Citroën). This allows us to securely extract the 4-digit security PIN directly from the ECU or BSI, bypass active immobilisers, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Peugeot Key Problems</div>
      <h2>Common Peugeot Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Peugeot key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>BSI Corruption / Economy Mode</h3>
        <p>If the vehicle battery dies or is disconnected improperly, the Peugeot BSI unit can corrupt its key data, throwing the car into "Economy Mode" and refusing to start. We can safely re-configure the BSI, extract the PIN, and re-learn the keys on-site.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Flip Key Mechanisms</h3>
        <p>Peugeot flip keys (commonly used on the 208, 308, and Boxer vans) are notorious for the internal spring mechanism snapping. We can transfer your existing circuit board into a brand-new, reinforced aftermarket shell and cut a fresh blade.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Worn Door Locks &amp; Keys</h3>
        <p>Physical key blades on older Peugeots (like the 206 and 207) often wear down until they can no longer turn the ignition. We can decode the lock and cut a fresh factory-spec blade to restore smooth operation.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "renault": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and Renault-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Renault vehicles utilize unique UCH (Unité Centrale de l'Habitacle) multiplex modules and highly secure key card systems rather than traditional bladed keys. If you lose your only key card, a standard high-street key cutter cannot generate a new one because the vehicle's immobiliser requires rolling-code synchronization. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for Renault vehicles. This allows us to securely extract the ISK (Incode/Outcode) data, bypass active immobilisers, and program a new key card on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Renault Key Problems</div>
      <h2>Common Renault Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Renault key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>"Card Not Detected" Error</h3>
        <p>The most common issue with Renault Megane, Scenic, and Clio key cards is internal circuit board cracking caused by sitting on or bending the card. This results in a "Card Not Detected" message on the dash. We can supply and program brand-new, robust replacement key cards on-site.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Card Reader Failure</h3>
        <p>If your key card is functioning perfectly but the car still won't start, the slot reader itself may have internal broken micro-switches. We can diagnose whether the fault lies in the card or the reader, and perform necessary repairs.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Keyless Entry (Hands-Free) Issues</h3>
        <p>Modern Renaults equipped with Hands-Free proximity systems can suffer from antenna faults or de-synchronized cards. We provide full diagnostic testing and replacement smart cards to restore keyless functionality.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "skoda": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and VAG-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Skoda vehicles utilize highly advanced immobilisers, sharing the MQB and MLB platforms with the rest of the Volkswagen Audi Group. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's dashboard cluster or ECU must be accessed to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for VAG vehicles. This allows us to securely bypass active immobilisers, extract the necessary Component Security (CS) codes, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Skoda Key Problems</div>
      <h2>Common Skoda Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Skoda key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Ignition Barrel Sticking (Octavia &amp; Fabia)</h3>
        <p>Many Skoda models suffer from steering lock housing or ignition barrel failure, where the key becomes difficult to turn or gets trapped inside. We can safely extract the key, repair the barrel, and replace the housing if necessary on-site.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Flip Key Shells</h3>
        <p>Skoda flip keys are prone to the hinge snapping or the rubber buttons degrading and falling out over time. Instead of replacing the entire key, we can transfer your existing circuit board and transponder into a reinforced aftermarket shell and cut a fresh blade.</p>
      </div>
      <div class="reveal feature-item">
        <h3>KESSY (Keyless Entry) Range Issues</h3>
        <p>Modern Skodas equipped with the KESSY smart key system can suffer from reduced range or failure due to drops and water damage. We provide rapid diagnostic testing and replacement smart keys programmed directly to your vehicle's profile.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "toyota": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Toyota vehicles utilize highly reliable but highly secure immobiliser systems. On many models, if you lose your only \"Master\" key, a standard auto locksmith cannot simply plug in and program a new one because the immobiliser ECU will refuse access without an existing master key present. Our mobile vans are equipped with specialist EEPROM and chip-reading tools. This allows us to safely remove the immobiliser unit, read the data directly from the microchip, and write a new master key directly to the board—saving you the massive expense of replacing the entire ECU at a main dealer.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Toyota Key Problems</div>
      <h2>Common Toyota Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Toyota key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>"All Keys Lost" (Immobiliser Reset)</h3>
        <p>As mentioned, losing all keys on models like the Aygo, Yaris, or older Prius often requires a complete immobiliser reset. We perform this complex procedure on-site, allowing us to program new keys without replacing expensive computer modules.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Key Blades</h3>
        <p>Toyota keys with the remote buttons built into the hard plastic head are notorious for snapping at the point where the metal blade meets the plastic, especially when turning worn ignitions. We can supply a stronger aftermarket shell and cut a fresh blade from your broken pieces.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Smart Key De-synchronisation</h3>
        <p>Proximity keys for the modern Prius, RAV4, and C-HR ranges can occasionally lose sync with the vehicle due to flat batteries. We provide mobile re-synchronisation and diagnostic testing to ensure your push-to-start functions work flawlessly.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "vauxhall": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and Vauxhall-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Vauxhall vehicles utilize advanced immobilisers integrated into their CIM (Column Integration Module) or BCM units. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle requires a 4-digit CarPass security code to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for Vauxhall (Opel) vehicles. This allows us to securely extract the CarPass PIN directly from the vehicle's modules, bypass active immobilisers, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Vauxhall Key Problems</div>
      <h2>Common Vauxhall Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Vauxhall key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Worn 2-Track Keys (Corsa &amp; Astra)</h3>
        <p>Older Vauxhall models utilize a 2-track laser key that wears down heavily over time, eventually failing to turn the ignition or door locks. We can decode the original factory cuts from your lock and cut a fresh, crisp key blade to restore smooth operation.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Flip Key Mechanisms</h3>
        <p>Vauxhall flip keys (commonly used on the Insignia, Astra J, and Corsa E) are notorious for the internal spring mechanism snapping or the rubber buttons perishing. We can transfer your existing circuit board into a brand-new, reinforced aftermarket shell and cut a fresh blade.</p>
      </div>
      <div class="reveal feature-item">
        <h3>CIM Module Faults</h3>
        <p>If your key turns but the car won't crank, or the immobiliser light flashes rapidly, the CIM module on the steering column may be failing to read the key. We can diagnose the fault, repair the transponder coil, or program replacement modules.</p>
      </div>
    </div>
  </div>
</section>

"""
    },
    "volkswagen": {
        "hero": " Whether you're stranded at home, at work, or on the roadside anywhere in Greater London, our fully equipped mobile vans arrive with the blank keys, transponder chips, and VAG-specific programming software required to get you back on the road the very same day. We pride ourselves on rapid response times and non-destructive entry methods.",
        "specialist": "Modern Volkswagen vehicles utilize highly advanced immobilisers, from the early Megamos crypto systems to the latest MQB platforms. If you lose your only key, a standard high-street key cutter cannot generate a new one because the vehicle's dashboard cluster or ECU must be accessed to authorize a new transponder. Our mobile auto locksmiths carry dealership-level diagnostic equipment tailored specifically for the Volkswagen Audi Group (VAG). This allows us to securely bypass active immobilisers, extract the necessary Component Security (CS) codes and MAC data, and program a new key fob on the roadside—saving you the expense and weeks of waiting associated with main dealer recovery.",
        "issues": """<!-- ==================== COMMON ISSUES ==================== -->
<section class="section">
  <div class="container">
    <div class="reveal section-head center">
      <div class="eyebrow">Volkswagen Key Problems</div>
      <h2>Common Volkswagen Key &amp; Lock Issues We Resolve</h2>
      <p>We see a wide variety of Volkswagen key faults across London. Here are the most common issues our mobile locksmiths fix on a daily basis:</p>
    </div>
    
    <div class="feature-grid">
      <div class="reveal feature-item">
        <h3>Ignition Barrel Sticking (Golf &amp; Polo)</h3>
        <p>Many VW models suffer from steering lock housing or ignition barrel failure, where the key becomes difficult to turn or gets trapped inside. We can safely extract the key, repair the barrel, and replace the housing if necessary on-site without needing to order expensive dealer parts.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Broken Flip Key Shells</h3>
        <p>Volkswagen flip keys are highly prone to the hinge snapping or the rubber buttons tearing and falling out over time. Instead of replacing the entire key, we can transfer your existing circuit board and glass transponder chip into a reinforced aftermarket shell and cut a fresh blade.</p>
      </div>
      <div class="reveal feature-item">
        <h3>Keyless Entry Range Issues</h3>
        <p>Modern VWs equipped with the KESSY smart key system can suffer from reduced range or complete failure due to drops, water damage, or dying internal batteries. We provide rapid diagnostic testing and replacement smart keys programmed directly to your vehicle's profile.</p>
      </div>
    </div>
  </div>
</section>

"""
    }
}

import os

base_path = r"C:\Users\97ars\.gemini\antigravity-ide\scratch\quick-turn-auto-keys\brands"

success_count = 0
error_files = []

for brand, data in brands_data.items():
    filepath = os.path.join(base_path, f"{brand}.html")
    if not os.path.exists(filepath):
        print(f"Skipping {brand}, file not found")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Hero Addition
    # Find the first paragraph inside <div class="reveal hero-copy">
    # We can match: <div class="reveal hero-copy">.*?</p>
    match_hero = re.search(r'(<div class="reveal hero-copy">.*?)(</p>)', content, re.DOTALL)
    if match_hero:
        content = content[:match_hero.start(2)] + data['hero'] + content[match_hero.start(2):]
    else:
        print(f"Failed to find hero for {brand}")
        error_files.append(brand)
        continue
        
    # 2. Why a Specialist Addition
    # Find <div class="reveal split-copy">...</div>
    # The structure has <p>...then <p style="margin-top:16px;">
    # We want to insert a NEW paragraph BEFORE the final <p style="margin-top:16px;">...
    match_split = re.search(r'(<div class="reveal split-copy">.*?)(<p[^>]*>.*?</p>)\s*(</div>)', content, re.DOTALL)
    if match_split:
        # Actually, the last <p> inside split-copy is the one we want to prepend our new paragraph to.
        # Let's just find the last <p[^>]*> before </div> in split-copy.
        split_content = match_split.group(1) + f'<p style="margin-top:16px;">{data["specialist"]}</p>\n        ' + match_split.group(2) + match_split.group(3)
        content = content[:match_split.start()] + split_content + content[match_split.end():]
    else:
        print(f"Failed to find split-copy for {brand}")
        error_files.append(brand)
        continue
        
    # 3. New Section
    # Find <!-- ==================== MOBILE
    match_mobile = re.search(r'<!-- ==================== MOBILE', content)
    if match_mobile:
        content = content[:match_mobile.start()] + data['issues'] + content[match_mobile.start():]
    else:
        print(f"Failed to find MOBILE section comment for {brand}")
        error_files.append(brand)
        continue
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    success_count += 1

print(f"Successfully injected content into {success_count} files.")
if error_files:
    print(f"Errors occurred on: {error_files}")
