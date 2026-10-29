"""All the text on the portfolio lives here. Edit this file, not app.py.

Rules: keep every claim something you can explain in an interview, and replace
the placeholder GitHub links in PROJECTS with the exact repository URLs.
"""

PROFILE = {
    "name": "Arbin Sigdel",
    "page_title": "Arbin Sigdel | Junior Developer, Kathmandu",
    "intro": (
        "I'm a junior developer in Kathmandu. I turn designs into working React "
        "interfaces and Django features, and I'm building the habits a team relies on: "
        "tests, code review and clear documentation."
    ),
    "facts": "Two internships, nine months in total. Computer Engineering graduate, July 2025.",
    "location": "Kathmandu, Nepal",
    "email": "sigdelarbin1@gmail.com",
    "phone": "+977 9863482269",
    "linkedin": "https://www.linkedin.com/in/arbin-sigdel-253320334/",
    "github": "https://github.com/arbinsigdel12",
    "featured_demo_label": "Try the live ClickCart demo",
    "featured_demo_url": "https://arbinsecommerce.netlify.app",
    "cv_file": "assets/Arbin_Sigdel_CV_Junior_Developer.pdf",
    # The same CV is served from static/ so the Download button can be a plain link.
    "cv_url": "app/static/Arbin_Sigdel_CV_Junior_Developer.pdf",
    "cv_download_name": "Arbin_Sigdel_CV.pdf",
    # Optional: put a photo at static/profile.jpg and it appears on the About page.
    "photo_file": "static/profile.jpg",
    "photo_url": "app/static/profile.jpg",
}

ABOUT = [
    "I studied Computer Engineering at Kathmandu Engineering College and graduated in "
    "July 2025. Before and after graduating I worked as an intern at two companies: "
    "Django development at Matrix Softech, then frontend development with React, Next.js "
    "and TypeScript at Codniv Innovations.",
    "At Codniv I turned designs into responsive interfaces, built reusable components, "
    "connected them to REST APIs and took part in code reviews. My experience letter "
    "describes me as punctual, hardworking and willing to learn. That is how I want to "
    "work in a team: finish what I am given, say early when I am stuck, and write down "
    "what I built.",
]

CURRENTLY = (
    "Working on right now: unit testing with Jest and Vitest, Git workflows and SQL "
    "fundamentals."
)

EXPERIENCE = [
    {
        "role": "Frontend Developer Intern",
        "org": "Codniv Innovations Pvt. Ltd., Kathmandu",
        "when": "Sep 2025 to Mar 2026",
        "points": [
            "Turned UI/UX designs and wireframes into responsive interfaces with React.js, "
            "Next.js, TypeScript and Tailwind CSS.",
            "Built reusable components and integrated RESTful APIs to power dynamic features.",
            "Took part in code reviews; tested, debugged and optimised pages for "
            "performance and user experience.",
            "Worked daily with developers and designers on a scalable, maintainable codebase.",
        ],
    },
    {
        "role": "Django Developer Intern",
        "org": "Matrix Softech Pvt. Ltd., Lalitpur",
        "when": "Oct 2023 to Jan 2024",
        "points": [
            "Developed and improved features of a Project Management System in Django "
            "under senior-developer supervision.",
            "Tested changes to the existing project against requirements and ran "
            "quality-assurance checks.",
            "Designed UI screens with Figma and ReactJS; completed Python and Django training.",
            "Sent daily progress updates to mentors and helped write documents for new "
            "applications, including Terms of Reference and a Privacy Policy.",
        ],
    },
]

# "code" should be the exact repository URL. Set "live" or "code" to "" to hide a link.
PROJECTS = [
    {
        "name": "ClickCart",
        "stack": "React, TypeScript, Redux",
        "summary": "An e-commerce storefront with product browsing, a cart and checkout.",
        "points": [
            "Redux keeps cart and product state consistent across components.",
            "API-like logic sits inside Redux slices, which cuts repeated fetch calls and "
            "keeps the code easier to maintain.",
        ],
        "live": "https://arbinsecommerce.netlify.app",
        "code": "https://github.com/arbinsigdel12",
    },
    {
        "name": "Fake News Detection",
        "stack": "Python, Scikit-Learn, Pandas",
        "summary": "A text classifier that labels news articles as real or fake.",
        "points": [
            "An ensemble of Logistic Regression, Decision Tree, Gradient Boosting and "
            "Random Forest, trained on more than 40,000 articles from a Kaggle dataset; "
            "95% accuracy on my test split.",
            "Includes a small text-based tool for real-time prediction.",
        ],
        "live": "",
        "code": "https://github.com/arbinsigdel12",
    },
    {
        "name": "Animal Welfare App",
        "stack": "Flutter, Firebase",
        "summary": "A mobile app built as my college minor project.",
        "points": [
            "Gallery image upload and real-time database integration with Firebase.",
        ],
        "live": "",
        "code": "https://github.com/arbinsigdel12",
    },
    {
        "name": "RAG Chatbot for Legal and Compliance Questions",
        "stack": "Python, LangChain, HuggingFace, FAISS",
        "summary": "A question-answering pipeline over regulatory documents.",
        "points": [
            "Documents are indexed in a vector database and retrieved to answer questions.",
            "Custom prompts reduce made-up answers.",
        ],
        "live": "",
        "code": "https://github.com/arbinsigdel12",
    },
]

SKILLS = [
    ("Languages", "JavaScript, TypeScript, Python, Dart"),
    ("Frontend", "React.js, Next.js, Redux, Tailwind CSS, Bootstrap, HTML, CSS"),
    ("Backend and data", "Django, REST API integration, Firebase, Pandas, NumPy, Scikit-Learn"),
    ("Working practices", "Git and GitHub, debugging, manual QA testing, code review, "
                          "technical documentation, Figma"),
    ("Learning now", "Unit testing with Jest and Vitest, SQL"),
]

EDUCATION = {
    "degree": "Bachelor in Computer Engineering",
    "school": "Kathmandu Engineering College, Kalimati, Kathmandu",
    "when": "Graduated July 2025",
}


# ---- Added for the redesign ------------------------------------------------

# Words that roll in the home-page headline: "I build ___".
ROLES = ["React interfaces", "Django features", "REST integrations", "tested, readable code"]

# Numbers shown on the home page. Each one comes from the text above.
STATS = [
    (2, "", "Internships"),
    (9, "", "Months of experience"),
    (4, "", "Projects built"),
    (95, "%", "Accuracy, fake-news model"),
]

# What I do: three cards on the home page.
FOCUS = [
    ("Frontend", "Responsive interfaces from design files, with reusable components.",
     "React, Next.js, TypeScript, Tailwind"),
    ("Backend", "Django features, REST API integration and Firebase.",
     "Django, REST, Firebase"),
    ("Data and AI", "Classifiers and retrieval pipelines in Python.",
     "Scikit-Learn, LangChain, FAISS"),
]

# Which projects get a big card on the home page (by name).
FEATURED = ["ClickCart", "Fake News Detection"]
