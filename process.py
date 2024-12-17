import json
import re

# Define the function to clean text
def clean_text(content, redundant_start, redundant_end):
    """
    Clean the text by removing redundant start and end patterns, and applying additional text cleaning.

    Args:
        content (str): The raw content string.
        redundant_start (str): The redundant starting pattern to remove.
        redundant_end (str): The redundant ending pattern to remove.
    
    Returns:
        str: The cleaned content.
    """
    # Step 1: Remove redundant starting pattern
    content = re.sub(re.escape(redundant_start), "", content, flags=re.IGNORECASE)
    
    # Step 2: Remove redundant ending pattern (everything after it)
    content = re.sub(f"{re.escape(redundant_end)}.*", "", content)
    
    # Step 3: Normalize whitespace (replace multiple spaces with a single space)
    content = re.sub(r'\s+', ' ', content).strip()
    
    # Step 4: Remove non-alphanumeric characters (except spaces)
    content = re.sub(r'[^\w\s]', '', content)
    
    # Step 5: Decode unicode escape sequences
    content = bytes(content, "utf-8").decode("unicode_escape")
    
    return content

# Define a function to clean the data and save it
def process_and_save(data, hrefs, redundant_start, redundant_end, output_filename):
    """
    Processes the data by cleaning the content based on redundant start and end patterns
    and saves the cleaned data into a JSON file.

    Args:
        data (dict): The original raw data.
        hrefs (list): The list of hrefs to process.
        redundant_start (str): The redundant starting pattern to remove.
        redundant_end (str): The redundant ending pattern to remove.
        output_filename (str): The name of the output file to save the cleaned data.
    """
    cleaned_data = {}
    
    for href in hrefs:
        cleaned_data[href] = clean_text(data[href], redundant_start, redundant_end)

    # Save the cleaned data into a JSON file
    with open(output_filename, "w", encoding="utf-8") as json_file:
        json.dump(cleaned_data, json_file, indent=4)

    print(f"Data cleaned and saved to {output_filename}")

# Load the data from JSON file
with open("assignment_test.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Categorize the hrefs
hrefs_fly = [h for h in data.keys() if "https://www.changiairport.com/in/en/fly" in h]
hrefs_at_changi = [h for h in data.keys() if "https://www.changiairport.com/in/en/at-changi" in h]
hrefs_dine_and_shop = [h for h in data.keys() if "https://www.changiairport.com/in/en/dine-and-shop" in h]
hrefs_experience = [h for h in data.keys() if "https://www.changiairport.com/in/en/experience" in h]
hrefs_happenings = [h for h in data.keys() if "https://www.changiairport.com/in/en/happenings" in h]
hrefs_rewards = [h for h in data.keys() if "https://www.changiairport.com/in/en/rewards" in h]
hrefs_help = [h for h in data.keys() if "https://www.changiairport.com/in/en/help" in h]

# Define the redundant start and end patterns for each category
redundant_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Cafés Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
redundant_end = "Fly Flight Information Airline Information"

# Now apply the `process_and_save` function to each category
process_and_save(data, hrefs_fly, redundant_start, redundant_end, "fly.json")
process_and_save(data, hrefs_at_changi, redundant_start, redundant_end, "at_changi.json")
process_and_save(data, hrefs_dine_and_shop, redundant_start, redundant_end, "dine_and_shop.json")
process_and_save(data, hrefs_experience, redundant_start, redundant_end, "experience.json")
process_and_save(data, hrefs_happenings, redundant_start, redundant_end, "happenings.json")
process_and_save(data, hrefs_rewards, redundant_start, redundant_end, "rewards.json")
process_and_save(data, hrefs_help , redundant_start, redundant_end, "help .json")




























# import json
# import re


# with open("assignment_test.json", "r", encoding="utf-8") as file:
#     data = json.load(file)
# hrefs = list(data.keys())

# hrefs_fly = [h for h in hrefs if "https://www.changiairport.com/in/en/fly"in h]
# hrefs_at_changi = [h for h in hrefs if "https://www.changiairport.com/in/en/at-changi"in h]
# hrefs_dine_and_shop = [h for h in hrefs if "https://www.changiairport.com/in/en/dine-and-shop"in h]
# hrefs_experience = [h for h in hrefs if "https://www.changiairport.com/in/en/experience" in h]
# hrefs_happenings = [h for h in hrefs if "https://www.changiairport.com/in/en/happenings" in h]
# hrefs_rewards = [h for h in hrefs if "https://www.changiairport.com/in/en/rewards" in h]
# hrefs_help = [h for h in hrefs if "https://www.changiairport.com/in/en/help" in h]


# def clean_text(text,start,end):
#     text = re.sub(re.escape(start), "", text, flags=re.IGNORECASE)
#     text = re.sub(f"{re.escape(end)}.*", "", text)
#     text = re.sub(r'\s+', ' ', text).strip()
#     text = re.sub(r'[^\w\s]', '', text)
#     text = bytes(text, "utf-8").decode("unicode_escape")
#     return text


# redundant_fly_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Caf\u00e9s Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
# redundant_fly_end = "Fly Flight Information Airline Information"
# fly_test = {}
# for href in hrefs_fly:
#     fly_test[href] = clean_text(data[href],redundant_fly_start,redundant_fly_end)
# with open("fly.json", "w", encoding="utf-8") as json_file:
#     json.dump(fly_test, json_file, indent=4)

# redundant_at_changi_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Caf\u00e9s Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
# redundant_at_changi_end = "Fly Flight Information Airline Information"
# at_changi_test = {}
# for href in hrefs_at_changi:
#     at_changi_test[href] = clean_text(data[href],redundant_at_changi_start,redundant_at_changi_end)
# with open("at_changi.json", "w", encoding="utf-8") as json_file:
#     json.dump(at_changi_test, json_file, indent=4)

# redundant_dine_and_shop_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Caf\u00e9s Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
# redundant_dine_and_shop_end = "Fly Flight Information Airline Information"
# dine_and_shop_test = {}
# for href in hrefs_dine_and_shop:
#     dine_and_shop_test[href] = clean_text(data[href],redundant_dine_and_shop_start,redundant_dine_and_shop_end)
# with open("dine_and_shop.json", "w", encoding="utf-8") as json_file:
#     json.dump(dine_and_shop_test, json_file, indent=4)

# redundant_experience_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Caf\u00e9s Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
# redundant_experience_end = "Fly Flight Information Airline Information"
# experience_test = {}
# for href in hrefs_experience:
#     experience_test[href] = clean_text(data[href],redundant_experience_start,redundant_experience_end)
# with open("experience.json", "w", encoding="utf-8") as json_file:
#     json.dump(experience_test, json_file, indent=4)


# redundant_happenings_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Caf\u00e9s Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
# redundant_happenings_end = "Fly Flight Information Airline Information"
# happenings_test = {}
# for href in hrefs_happenings:
#     happenings_test[href] = clean_text(data[href],redundant_happenings_start,redundant_happenings_end)
# with open("happenings.json", "w", encoding="utf-8") as json_file:
#     json.dump(happenings_test, json_file, indent=4)

# redundant_rewards_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Caf\u00e9s Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
# redundant_rewards_end = "Fly Flight Information Airline Information"
# rewards_test = {}
# for href in hrefs_rewards:
#     rewards_test[href] = clean_text(data[href],redundant_rewards_start,redundant_rewards_end)
# with open("rewards.json", "w", encoding="utf-8") as json_file:
#     json.dump(rewards_test, json_file, indent=4)


# redundant_help_start = "Airport Changi Sites Airport Corporate Careers CAI Jewel Now Boarding Fly Fly Flight Information Arrival Flight Listing Departure Flight Listing Freighter Flight Listing Arrival Guide Entry Requirements (ICA) Immigration Clearance Customs Declaration Baggage Services Lost Baggage Passenger Meeting Services Leaving Changi Airport Getting Started in Singapore Departure Guide Travel Advisories Pre-flight Check Getting to Changi Airport Early Check-in Fast Check-in Immigration Clearance Tax Refund Security Screening and Baggage Restrictions Transiting Guide Free Singapore Tours Visa-free Transit Facility Transit Hotels Lounges Airline Lounges Pay-per-use Lounges Free-to-use Rest Areas Shower and Spa Services Airline Information Passenger Airline Information Freighter Airline Information At Changi At Changi Map Terminal Guides Terminal 1 Terminal 2 Terminal 3 Terminal 4 Transport and Directions Transfer Between Changi Terminals and Jewel Getting to Changi Airport Leaving Changi Airport Coach to Johor Bahru Parking Special Assistance Travelling with Children Persons with Reduced Mobility Persons with Invisible Disability Medical Care Facilities & Services Amenities Assistance Baggage Digital Travel Services Facilities Health & Wellness Hotels Lounges Other Services Transportation Hotels Crowne Plaza Changi Airport Transit Hotels YOTEL AIR Singapore Changi Airport Jewel Changi Airport Plan Your Visit Attractions Shop Dine Stay Plan Your Events Corporate Weddings Birthdays Dine & Shop Dine & Shop Dining Caf\u00e9s Fast Food Fine Dining Food Court Homegrown Brands Pubs & Bars Quick Bites Restaurants Shopping Beauty Children & Maternity Deli & Confectionary Electronics Entertainment Fashion & Accessories Health & Wellness Home & Living Homegrown Brands Lifestyle Luxury Optical Souvenirs, Gifts & Books Sports Supermarket & Convenience Travel Watches & Jewellery Wine & Spirits Changi Pay Changi Rewards Shopping Concierge Shop Online Experience Experience Attractions Art Gardens Play Experiences for Kids Attractions ChangiVerse Activity Videos Things to Do Learning Journeys (For Students) Free Tours Free Singapore Tour Changi Airport Tours Jewel Changi Airport Tours Happenings Happenings Events Changi Festive Village Pop-up Stores Promotions Changi Rewards Member's Specials Changi Rewards Changi Rewards Benefits & Privileges Membership Benefits Parking Privileges Changi Rewards Catalogue Specials Events Monarch About Monarch Benefits & Privileges Monarch Concierge Monarch Parking Monarch FAQs Help FAQs Terms and Conditions Feedback Form Chat App & Help App & Help Assistance Lost & Found Special Assistance FAQs Changi App Travel Tips Baggage Tracker Book, Redeem & Play Dine with Changi App Changi Pay Changi App Help Centre The Great Changi Appscapade Space APPxplorer Download Changi App Contact Information Login/Sign Up Dashboard My Rewards Logout en zh All Changi Sites: Language Select: Logout"
# redundant_help_end = "Fly Flight Information Airline Information"
# help_test = {}
# for href in hrefs_help:
#     help_test[href] = clean_text(data[href],redundant_help_start,redundant_help_end)
# with open("help.json", "w", encoding="utf-8") as json_file:
#     json.dump(help_test, json_file, indent=4)