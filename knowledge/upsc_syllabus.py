# knowledge/upsc_syllabus.py

UPSC_CATEGORIES = {
    "Prelims_GS1": {
        "History": [
            "Ancient History",
            "Medieval History",
            "Modern Indian History",
            "Indian National Movement",
            "Art & Culture"
        ],
        "Geography": [
            "Indian Geography (Physical, Social, Economic)",
            "World Geography (Physical, Social, Economic)",
            "Important Geophysical Phenomena (Earthquakes, Tsunami, Cyclones)",
            "Changes in Critical Geographical Features"
        ],
        "Polity_and_Governance": [
            "Indian Constitution (Evolution, Features, Amendments)",
            "Functions & Responsibilities of Union & States (Federal Structure)",
            "Local Governments (Panchayati Raj, Municipalities)",
            "Separation of Powers, Dispute Redressal Mechanisms",
            "Parliament & State Legislatures (Structure, Functioning)",
            "Executive & Judiciary (Structure, Organization, Functioning)",
            "Constitutional & Non-Constitutional Bodies",
            "Government Policies & Interventions",
            "Governance (Transparency, Accountability, E-governance, Citizen's Charters)",
            "Role of Civil Services"
        ],
        "Economy_and_Social_Development": [
            "Indian Economy (Planning, Mobilization of Resources, Growth, Development, Employment)",
            "Inclusive Growth",
            "Government Budgeting",
            "Poverty & Inclusion",
            "Demographics",
            "Social Sector Initiatives (Health, Education, Human Resources)",
            "Issues related to Poverty & Hunger"
        ],
        "Environment_and_Ecology": [
            "General issues on Environmental Ecology",
            "Biodiversity",
            "Climate Change",
            "Conservation, Environmental Pollution & Degradation",
            "Environmental Impact Assessment (EIA)"
        ],
        "Science_and_Technology": [
            "General Science",
            "Developments & Applications in Everyday Life",
            "Achievements of Indians in S&T",
            "Indigenization of Technology",
            "Awareness in IT, Space, Computers, Robotics, Nanotechnology, Biotechnology",
            "Issues related to Intellectual Property Rights (IPR)"
        ],
        "Current_Events": [
            "National Current Events",
            "International Current Events",
            "Important Schemes & Policies in News"
        ]
    },
    "Mains_GS2": {
        "Governance": [
            "Government Policies & Interventions",
            "Development Processes & Industry Role",
            "NGOs, SHGs, Groups, Associations, Donors, Charities",
            "Transparency & Accountability, E-governance, Citizen's Charters",
            "Role of Civil Services in a Democracy"
        ],
        "Constitution": [
            "Historical Underpinnings, Evolution, Features, Amendments, Basic Structure",
            "Functions & Responsibilities of Union & States (Federal Structure)",
            "Separation of Powers, Dispute Redressal Mechanisms",
            "Comparison of Indian Constitutional Scheme with other countries"
        ],
        "Polity": [
            "Parliament & State Legislatures (Structure, Functioning, Powers & Privileges)",
            "Executive & Judiciary (Structure, Organization, Functioning)",
            "Ministries & Departments",
            "Pressure Groups, Formal & Informal Associations",
            "Salient Features of Representation of People's Act",
            "Appointment to Constitutional Posts, Powers of Constitutional Bodies",
            "Statutory, Regulatory & Quasi-Judicial Bodies"
        ],
        "Social_Justice": [
            "Welfare Schemes for Vulnerable Sections (Centre & States)",
            "Performance of Welfare Schemes",
            "Mechanisms, Laws, Institutions for Protection of Vulnerable Sections",
            "Issues related to Development & Management of Social Sector (Health, Education, HR)",
            "Issues related to Poverty & Hunger"
        ],
        "International_Relations": [
            "India & its Neighborhood",
            "Bilateral, Regional & Global Groupings & Agreements (affecting India's interests)",
            "Effect of Policies & Politics of Developed & Developing Countries on India's Interests",
            "Indian Diaspora",
            "Important International Institutions, Agencies & Fora (Structure, Mandate)"
        ]
    },
    "Mains_GS3": {
        "Economy": [
            "Indian Economy (Planning, Mobilization of Resources, Growth, Development, Employment)",
            "Inclusive Growth & Issues",
            "Government Budgeting",
            "Effects of Liberalization on Economy",
            "Changes in Industrial Policy & their effects",
            "Infrastructure (Energy, Ports, Roads, Airports, Railways etc.)",
            "Investment Models (PPP etc.)"
        ],
        "Agriculture": [
            "Major Cropping Patterns, Irrigation Systems",
            "Storage, Transport & Marketing of Agricultural Produce",
            "E-technology in aid of Farmers",
            "Direct & Indirect Farm Subsidies, MSP",
            "Public Distribution System (PDS)",
            "Buffer Stocks & Food Security",
            "Technology Missions, Economics of Animal-Rearing",
            "Food Processing & Related Industries",
            "Land Reforms in India"
        ],
        "Science_and_Technology": [
            "Achievements of Indians in S&T",
            "Indigenization of Technology & Development of New Technology",
            "Awareness in IT, Space, Computers, Robotics, Nanotechnology, Biotechnology",
            "Issues related to Intellectual Property Rights (IPR)"
        ],
        "Biodiversity_and_Environment": [
            "Conservation, Environmental Pollution & Degradation",
            "Environmental Impact Assessment (EIA)",
            "Biodiversity (Basics, Conservation, Threats)",
            "Climate Change (Issues, Adaptation, Mitigation)"
        ],
        "Disaster_Management": [
            "Disasters & Disaster Management (Types, Prevention, Mitigation, Preparedness, Response, Rehabilitation)"
        ],
        "Internal_Security": [
            "Linkages between Development & Spread of Extremism",
            "Role of External State & Non-State Actors",
            "Challenges to Internal Security through Communication Networks (Media, Social Networking Sites)",
            "Basics of Cyber Security",
            "Money-Laundering & its Prevention",
            "Security Challenges & Management in Border Areas",
            "Linkages of Organized Crime with Terrorism",
            "Various Security Forces & Agencies & their Mandate"
        ]
    },
    "Mains_GS4": {
        "Ethics_and_Human_Interface": [
            "Essence, Determinants & Consequences of Ethics in Human Actions",
            "Dimensions of Ethics",
            "Ethics in Private & Public Relationships",
            "Human Values (Lessons from Leaders, Reformers, Administrators)"
        ],
        "Attitude": [
            "Content, Structure, Function of Attitude",
            "Influence of Attitude in Thought & Behavior",
            "Moral & Political Attitudes",
            "Social Influence & Persuasion"
        ],
        "Aptitude_and_Foundational_Values": [
            "Integrity, Impartiality & Non-partisanship",
            "Objectivity, Dedication to Public Service",
            "Empathy, Tolerance & Compassion towards Weaker Sections"
        ],
        "Emotional_Intelligence": [
            "Concepts of Emotional Intelligence",
            "Utility & Application in Administration & Governance"
        ],
        "Contributions_of_Thinkers_and_Philosophers": [
            "Moral Thinkers & Philosophers from India & World (to concepts of morality)"
        ],
        "Public_Civil_Service_Values_and_Ethics_in_Public_Administration": [
            "Status & Associated Problems",
            "Ethical Concerns & Dilemmas (Govt & Private Institutions)",
            "Laws, Rules, Regulations & Conscience as sources of Ethical Guidance",
            "Accountability & Ethical Governance",
            "Strengthening of Ethical & Moral Values in Governance",
            "Ethical Issues in International Relations & Funding",
            "Corporate Governance"
        ],
        "Probity_in_Governance": [
            "Concept of Public Service",
            "Philosophical Basis of Governance & Probity",
            "Information Sharing & Transparency (Right to Information)",
            "Codes of Ethics, Codes of Conduct",
            "Citizen's Charters",
            "Quality of Service Delivery",
            "Utilization of Public Funds",
            "Challenges of Corruption",
            "Work Culture"
        ],
        "Case_Studies": [
            "Application of ethical principles to real-life situations"
        ]
    }
}