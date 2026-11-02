from django.core.management.base import BaseCommand
from core.models import SiteSetting, Service, Project, Property, Testimonial

class Command(BaseCommand):
    help = "Add rich BuildCraft demo content; all entries can be edited in Django Admin."
    def handle(self, *args, **options):
        SiteSetting.objects.update_or_create(pk=1, defaults={"company_name":"BuildCraft","tagline":"Building dreams. Creating legacies.","phone":"+91 98765 43210","email":"hello@buildcraft.example","address":"Trivandrum, Kerala, India","about_text":"BuildCraft brings architecture, engineering and craftsmanship together to create lasting homes and business spaces. From the first consultation to final handover, our approach is built around clarity, quality and thoughtful planning."})
        services = [
          ("Residential Construction","🏡","Thoughtfully planned independent homes, villas and multi-family residences. We coordinate site assessment, architectural planning, structural work, quality checks and finishing so every stage has a clear purpose."),
          ("Commercial Construction","🏢","Functional offices, retail spaces, clinics and business buildings designed around people, workflow and long-term performance. Our process brings planning, engineering and site execution together."),
          ("Maintenance & Repairs","🛠️","Practical property care including waterproofing, structural repairs, electrical and plumbing upgrades, painting and periodic maintenance to help protect your investment."),
          ("Interior Planning & Design","🛋️","Comfortable, beautiful interiors with considered layouts, lighting, storage, materials and finishes. We shape each room around the way you live or work."),
          ("Renovation & Remodeling","🧱","Give existing spaces a new life with extensions, modern layouts, facade upgrades, kitchen and bathroom remodelling and carefully managed renovation work."),
          ("Architecture & Planning","📐","Concept development, space planning, drawings, material guidance and coordinated design support to help turn an early idea into a buildable plan."),
        ]
        for i,(title,icon,desc) in enumerate(services,1): Service.objects.update_or_create(title=title,defaults={"description":desc,"icon":icon,"order":i,"is_active":True})
        project_data = [
          ("The Courtyard Villa","Residential","Trivandrum, Kerala","A contemporary family home shaped around a planted courtyard, generous daylight and a calm indoor-outdoor connection.",2026),
          ("Palm Grove Residence","Residential","Kollam, Kerala","A warm modern residence with shaded balconies, practical family spaces and a carefully layered exterior palette.",2025),
          ("Hillview Family Home","Residential","Nedumangad, Kerala","A compact hillside home planned to make the most of its views, natural ventilation and sloping site.",2025),
          ("The Garden House","Residential","Kochi, Kerala","A modern home with a garden-facing living space, clean lines and durable low-maintenance finishes.",2024),
          ("Lake Edge Residence","Residential","Alappuzha, Kerala","A spacious family residence with a welcoming entry, open-plan gathering areas and restful private rooms.",2024),
          ("Crescent Business Centre","Commercial","Kochi, Kerala","A contemporary commercial building with clear circulation, flexible office floors and a strong street presence.",2026),
          ("Harbour View Offices","Commercial","Kollam, Kerala","A professional office environment planned for daylight, collaborative work and efficient daily operations.",2025),
          ("Greenline Retail Hub","Commercial","Trivandrum, Kerala","A retail destination with adaptable shopfronts, accessible customer routes and practical service areas.",2025),
          ("Summit Medical Suites","Commercial","Kottayam, Kerala","A clean, accessible healthcare facility with patient-friendly circulation and carefully planned rooms.",2024),
          ("The Works Studio","Commercial","Thrissur, Kerala","A flexible workspace with meeting areas, open work zones and a durable contemporary material palette.",2024),
          ("Serene Living Room","Interior Design","Trivandrum, Kerala","A light-filled living room with layered textures, comfortable seating and integrated ambient lighting.",2026),
          ("Warm Minimal Kitchen","Interior Design","Kochi, Kerala","A functional kitchen with efficient storage, easy-care surfaces and a balanced mix of warm finishes.",2025),
          ("Calm Bedroom Suite","Interior Design","Kollam, Kerala","A restful bedroom concept with soft tones, custom storage and thoughtful lighting details.",2025),
          ("Modern Reception Lounge","Interior Design","Kottayam, Kerala","A welcoming reception interior with a clear visitor journey and refined brand-led details.",2024),
          ("Compact Apartment Fitout","Interior Design","Thrissur, Kerala","A space-conscious apartment interior that combines flexible furniture, storage and natural light.",2024),
          ("Heritage Home Renewal","Renovation","Fort Kochi, Kerala","A sensitive upgrade that refreshes essential services while retaining the character of an older home.",2026),
          ("Family Home Extension","Renovation","Trivandrum, Kerala","An additional family wing designed to connect naturally with the existing home and garden.",2025),
          ("Facade Refresh Project","Renovation","Kollam, Kerala","A dated exterior renewed with a contemporary finish, improved weather protection and a welcoming entrance.",2025),
          ("Kitchen & Bath Upgrade","Renovation","Alappuzha, Kerala","A coordinated renovation that improves everyday function, ventilation, storage and finish quality.",2024),
          ("Apartment Modernisation","Renovation","Kochi, Kerala","A complete interior refresh with improved lighting, updated finishes and more useful room layouts.",2024),
          ("Coastal Home Blueprint","Architecture","Alappuzha, Kerala","A climate-aware concept plan with shaded openings, cross ventilation and practical outdoor transitions.",2026),
          ("Urban Duplex Plan","Architecture","Kochi, Kerala","A compact duplex layout that separates shared and private zones while keeping the home connected.",2025),
          ("Courtyard Residence Concept","Architecture","Thrissur, Kerala","A concept built around a central courtyard to bring daylight and greenery into the heart of the home.",2025),
          ("Community Hall Design","Architecture","Kottayam, Kerala","A welcoming public building concept with flexible gathering space and accessible circulation.",2024),
          ("Mixed-use Building Study","Architecture","Trivandrum, Kerala","A mixed-use concept that balances street-level commercial activity with comfortable upper-level spaces.",2024),
        ]
        project_images = ['projects/01-design-mar-2-2026-02-01-01-pm.png','projects/06-design-mar-3-2026-12-17-50-pm.png','projects/08-design-mar-3-2026-12-39-14-pm.png','projects/10-design-mar-3-2026-12-49-18-pm.png','projects/17-pr1.png','projects/18-pr2.png','projects/19-pr3.png','projects/20-pr4.png','projects/21-pr5.png','projects/22-pr6.png']
        project_images = [project_images[i % len(project_images)] for i in range(len(project_data))]
        for i,(title,cat,loc,desc,year) in enumerate(project_data):
          Project.objects.update_or_create(title=title,defaults={"category":cat,"location":loc,"description":desc,"completion_year":year,"featured":True,"image":project_images[i]})
        property_data = [
          ("Emerald Garden Villa","Villa","Sale","Trivandrum, Kerala",12800000,4,4,2850,"A spacious villa with a landscaped garden, generous family lounge and private outdoor seating."),
          ("Skyline Premium Apartment","Apartment","Sale","Kochi, Kerala",7850000,3,3,1680,"A bright city apartment with practical storage, balcony views and convenient access to daily essentials."),
          ("Palm Court Independent Home","House","Sale","Kollam, Kerala",8900000,3,3,2100,"An independent family home with a functional kitchen, comfortable bedrooms and covered parking."),
          ("Central Business Suite","Commercial","Rent","Trivandrum, Kerala",65000,0,1,1450,"A flexible commercial unit suitable for a studio, professional office or customer-facing business."),
          ("Lakeview Duplex Villa","Villa","Sale","Alappuzha, Kerala",15400000,4,4,3200,"A two-level home with spacious living areas, a family terrace and a calm residential setting."),
          ("Urban Nest 2 BHK","Apartment","Rent","Kochi, Kerala",28000,2,2,1120,"A well-planned apartment with a bright living room and easy access to public transport."),
          ("Hilltop Family House","House","Sale","Nedumangad, Kerala",6750000,3,2,1760,"A practical family home with a shaded sit-out and well-proportioned rooms."),
          ("Retail Corner Space","Commercial","Rent","Kollam, Kerala",42000,0,1,980,"A street-facing retail space with a flexible open plan and visible frontage."),
          ("Orchid Residency 3 BHK","Apartment","Sale","Thrissur, Kerala",9200000,3,3,1540,"A comfortable apartment with good natural light, a balcony and family-friendly shared amenities."),
          ("Meadow View Villa","Villa","Sale","Kottayam, Kerala",11900000,4,3,2600,"A contemporary villa with an open living-dining layout and green views."),
          ("Compact City Home","House","Rent","Trivandrum, Kerala",18000,2,2,960,"A neat, easy-to-maintain home suited to a small family or working professionals."),
          ("Office Floor - Tech Park Road","Commercial","Rent","Kochi, Kerala",110000,0,2,2400,"An adaptable office floor with space for workstations, meeting rooms and reception."),
          ("Sunrise Apartment 1 BHK","Apartment","Rent","Kollam, Kerala",14500,1,1,720,"A compact apartment with an efficient layout and a bright kitchen-living area."),
          ("Grand Entrance Residence","Villa","Sale","Kochi, Kerala",18600000,5,5,3650,"A larger family villa with a generous entrance, multiple living zones and landscaped outdoor space."),
          ("Corner Plot House","House","Sale","Alappuzha, Kerala",7350000,3,2,1820,"An independent home on a corner site with good daylight and a practical family layout."),
          ("Studio Commercial Unit","Commercial","Sale","Thrissur, Kerala",5600000,0,1,860,"A compact commercial unit suitable for a boutique, consulting room or small office."),
          ("Garden View Apartment","Apartment","Sale","Kottayam, Kerala",6450000,2,2,1180,"A calm apartment overlooking landscaped common areas with comfortable everyday spaces."),
          ("Westside Family Villa","Villa","Rent","Trivandrum, Kerala",48000,3,3,2300,"A well-maintained villa with a private sit-out, family dining area and covered parking."),
          ("Warehouse & Office Unit","Commercial","Rent","Kollam, Kerala",85000,0,2,3100,"A versatile business property combining open storage space with a small office area."),
          ("Modern Compact Residence","House","Sale","Nedumangad, Kerala",5900000,2,2,1320,"A thoughtfully planned compact house with low-maintenance finishes and a useful outdoor area."),
        ]
        property_images = ['projects/01-design-mar-2-2026-02-01-01-pm.png','projects/06-design-mar-3-2026-12-17-50-pm.png','projects/08-design-mar-3-2026-12-39-14-pm.png','projects/10-design-mar-3-2026-12-49-18-pm.png','projects/17-pr1.png','projects/18-pr2.png','projects/19-pr3.png','projects/20-pr4.png','projects/21-pr5.png','projects/22-pr6.png']
        property_images = [property_images[i % len(property_images)] for i in range(len(property_data))]
        for i,(title,typ,status,loc,price,beds,baths,area,desc) in enumerate(property_data):
          Property.objects.update_or_create(title=title,defaults={"property_type":typ,"status":status,"location":loc,"price":price,"bedrooms":beds,"bathrooms":baths,"area_sqft":area,"description":desc,"featured":True,"available":True,"image":property_images[i]})
        reviews=[("Anand Kumar","Villa homeowner","The planning conversations were clear and the team helped us make sensible decisions at every stage. The finished home feels welcoming and thoughtfully detailed."),("Meera Nair","Apartment client","Communication was consistent and the design team listened carefully to how we use our space. The final result is practical and beautiful."),("Rahul Menon","Business owner","Our office fitout was coordinated professionally. The work areas are comfortable and the handover process was well organised."),("Divya Raj","Renovation client","The renovation team respected our existing home, explained the work clearly and kept the site organised."),("Arun Suresh","Homeowner","From the first layout discussion to the finishing details, the team was approachable and attentive.")]
        for name,role,msg in reviews: Testimonial.objects.update_or_create(customer_name=name,defaults={"role":role,"message":msg,"rating":5,"is_active":True})
        self.stdout.write(self.style.SUCCESS("Construction-focused demo content refreshed: 6 services, 25 projects and 5 reviews."))
