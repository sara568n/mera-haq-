
import streamlit as st

# ==================================================
# MERA HAQ
# Government Scheme Discovery Platform
# Class 12 Artificial Intelligence Project
# ==================================================

st.set_page_config(
    page_title="Mera Haq",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# LANGUAGE AND TRANSLATIONS
# ==================================================

TEXT = {
    "English": {
        "brand": "🇮🇳 MERA HAQ",
        "caption": "Government Scheme Discovery Platform",
        "language": "Language / भाषा",
        "home": "Home",
        "explore": "Explore Schemes",
        "eligibility": "Eligibility Guide",
        "ask": "Ask Mera Haq",
        "about": "About Project",
        "welcome": "KNOW YOUR RIGHTS. DISCOVER YOUR BENEFITS.",
        "notice": "Government schemes and benefits, made easier to discover.",
        "access": "Making Government Schemes Accessible",
        "access_text": "Mera Haq helps citizens discover government schemes through a simple and accessible platform.",
        "entries": "Scheme Entries",
        "languages": "Available Languages",
        "free": "Free Access",
        "what": "What is Mera Haq?",
        "what_text": "Mera Haq is an educational prototype designed to make information about government welfare schemes easier to understand and explore.",
        "explore_title": "Explore Government Schemes",
        "search": "Search for a scheme",
        "category": "Select Category",
        "all": "All Categories",
        "details": "Scheme Details",
        "benefits": "Benefits",
        "audience": "Target Audience",
        "eligibility_title": "Eligibility Guide",
        "eligibility_text": "Explore schemes based on the intended beneficiary group.",
        "select_audience": "Choose a beneficiary group",
        "all_audiences": "Everyone",
        "ask_title": "Ask Mera Haq",
        "ask_text": "Enter a question or keyword to discover a relevant scheme.",
        "question": "Type your question here",
        "find": "Find Schemes",
        "no_results": "No matching schemes found. Try another keyword.",
        "about_title": "About the Project",
        "about_text": "Mera Haq is a student-developed project that aims to improve awareness and accessibility of Indian government schemes.",
        "mission": "Our Mission",
        "mission_text": "To make information about public welfare schemes easier to find and understand.",
        "vision": "Our Vision",
        "vision_text": "A future where every citizen can access information about schemes and opportunities.",
        "technology": "Technology Used",
        "limitations": "Project Limitations",
        "limitations_text": "This prototype uses a sample scheme database. Eligibility information is indicative and should be checked on official government websites.",
        "official": "Visit Official Website",
        "footer": "Mera Haq | A Class 12 AI Project",
        "found": "schemes found",
        "no_data": "No schemes available."
    },

    "Hindi": {
        "brand": "🇮🇳 मेरा हक",
        "caption": "सरकारी योजनाओं की जानकारी का मंच",
        "language": "भाषा / Language",
        "home": "होम",
        "explore": "योजनाएँ देखें",
        "eligibility": "पात्रता मार्गदर्शिका",
        "ask": "मेरा हक से पूछें",
        "about": "परियोजना के बारे में",
        "welcome": "अपने अधिकार जानें। अपने लाभ पहचानें।",
        "notice": "सरकारी योजनाओं और लाभों की जानकारी अब आसान।",
        "access": "सरकारी योजनाओं को सभी के लिए सुलभ बनाना",
        "access_text": "मेरा हक नागरिकों को सरकारी योजनाओं की जानकारी सरल तरीके से खोजने में मदद करता है।",
        "entries": "योजनाओं की संख्या",
        "languages": "उपलब्ध भाषाएँ",
        "free": "निःशुल्क उपयोग",
        "what": "मेरा हक क्या है?",
        "what_text": "मेरा हक एक शैक्षिक प्रोटोटाइप है, जिसका उद्देश्य सरकारी कल्याणकारी योजनाओं की जानकारी को सरल बनाना है।",
        "explore_title": "सरकारी योजनाएँ देखें",
        "search": "योजना खोजें",
        "category": "श्रेणी चुनें",
        "all": "सभी श्रेणियाँ",
        "details": "योजना का विवरण",
        "benefits": "लाभ",
        "audience": "लक्षित लाभार्थी",
        "eligibility_title": "पात्रता मार्गदर्शिका",
        "eligibility_text": "लाभार्थी समूह के आधार पर योजनाएँ खोजें।",
        "select_audience": "लाभार्थी समूह चुनें",
        "all_audiences": "सभी",
        "ask_title": "मेरा हक से पूछें",
        "ask_text": "संबंधित योजना खोजने के लिए अपना प्रश्न या शब्द लिखें।",
        "question": "अपना प्रश्न यहाँ लिखें",
        "find": "योजनाएँ खोजें",
        "no_results": "कोई संबंधित योजना नहीं मिली। दूसरा शब्द लिखकर देखें।",
        "about_title": "परियोजना के बारे में",
        "about_text": "मेरा हक एक छात्र परियोजना है, जिसका उद्देश्य भारतीय सरकारी योजनाओं के प्रति जागरूकता और पहुँच बढ़ाना है।",
        "mission": "हमारा मिशन",
        "mission_text": "सरकारी कल्याणकारी योजनाओं की जानकारी को खोजना और समझना आसान बनाना।",
        "vision": "हमारा दृष्टिकोण",
        "vision_text": "ऐसा भविष्य जहाँ प्रत्येक नागरिक योजनाओं की जानकारी प्राप्त कर सके।",
        "technology": "प्रयुक्त तकनीक",
        "limitations": "परियोजना की सीमाएँ",
        "limitations_text": "यह प्रोटोटाइप नमूना योजनाओं के डेटाबेस का उपयोग करता है। पात्रता की जानकारी केवल संकेतात्मक है। आधिकारिक वेबसाइट पर जानकारी की पुष्टि करें।",
        "official": "आधिकारिक वेबसाइट देखें",
        "footer": "मेरा हक | कक्षा 12 की AI परियोजना",
        "found": "योजनाएँ मिलीं",
        "no_data": "कोई योजना उपलब्ध नहीं है।"
    }
}

# ==================================================
# GOVERNMENT SCHEME DATABASE
# ==================================================

SCHEMES = [
    {
        "name": "PM-KISAN Samman Nidhi",
        "category": "Agriculture",
        "audience": "Farmers",
        "description": "An income support scheme for eligible farmer families.",
        "benefits": "Eligible farmers receive financial assistance of ₹6,000 per year in three instalments.",
        "eligibility": "Eligible landholding farmer families, subject to scheme exclusions.",
        "url": "https://pmkisan.gov.in/"
    },
    {
        "name": "Ayushman Bharat PM-JAY",
        "category": "Health",
        "audience": "Families",
        "description": "A health assurance scheme providing eligible families access to hospital care.",
        "benefits": "Health cover of up to ₹5 lakh per eligible family per year for covered hospitalisation.",
        "eligibility": "Eligibility is based on the applicable government beneficiary database and rules.",
        "url": "https://pmjay.gov.in/"
    },
    {
        "name": "Pradhan Mantri Ujjwala Yojana",
        "category": "Women",
        "audience": "Women",
        "description": "A scheme supporting eligible women in accessing LPG connections.",
        "benefits": "Deposit-free LPG connection support and applicable benefits under scheme rules.",
        "eligibility": "Adult women from eligible households meeting scheme criteria.",
        "url": "https://www.pmuy.gov.in/"
    },
    {
        "name": "Beti Bachao Beti Padhao",
        "category": "Education",
        "audience": "Girls",
        "description": "A campaign focused on the protection, education and empowerment of girls.",
        "benefits": "Promotes awareness, education and opportunities for girls.",
        "eligibility": "A public awareness initiative; benefits depend on local programmes.",
        "url": "https://wcd.gov.in/"
    },
    {
        "name": "Sukanya Samriddhi Yojana",
        "category": "Savings",
        "audience": "Girls",
        "description": "A small savings scheme designed for the future of a girl child.",
        "benefits": "Provides a government-backed savings account with notified interest.",
        "eligibility": "A guardian can open an account for an eligible girl child.",
        "url": "https://www.indiapost.gov.in/"
    },
    {
        "name": "PM Awas Yojana - Urban",
        "category": "Housing",
        "audience": "Families",
        "description": "A programme supporting eligible urban households in accessing housing.",
        "benefits": "Housing assistance according to applicable programme guidelines.",
        "eligibility": "Eligible urban households meeting current scheme criteria.",
        "url": "https://pmay-urban.gov.in/"
    },
    {
        "name": "PM Awas Yojana - Gramin",
        "category": "Housing",
        "audience": "Rural People",
        "description": "A rural housing programme for eligible households.",
        "benefits": "Financial assistance for construction of a pucca house as per guidelines.",
        "eligibility": "Eligible rural households identified under the selection process.",
        "url": "https://pmayg.nic.in/"
    },
    {
        "name": "Mahatma Gandhi NREGA",
        "category": "Employment",
        "audience": "Rural People",
        "description": "A rural employment guarantee programme.",
        "benefits": "A legal guarantee of up to 100 days of wage employment per rural household in a financial year, subject to the Act.",
        "eligibility": "Adult members of rural households willing to undertake unskilled manual work.",
        "url": "https://nrega.nic.in/"
    },
    {
        "name": "National Social Assistance Programme",
        "category": "Social Welfare",
        "audience": "Senior Citizens",
        "description": "A social assistance programme for eligible vulnerable groups.",
        "benefits": "Assistance through applicable pension components.",
        "eligibility": "People meeting the relevant age, income and other criteria.",
        "url": "https://nsap.nic.in/"
    },
    {
        "name": "PM Vishwakarma",
        "category": "Employment",
        "audience": "Workers",
        "description": "A programme supporting traditional artisans and craftspeople.",
        "benefits": "May include skill training, toolkit support and credit support.",
        "eligibility": "Traditional artisans in notified trades who meet scheme conditions.",
        "url": "https://pmvishwakarma.gov.in/"
    },
    {
        "name": "PM Mudra Yojana",
        "category": "Business",
        "audience": "Entrepreneurs",
        "description": "A scheme supporting micro and small businesses with loans.",
        "benefits": "Loans through participating lending institutions.",
        "eligibility": "Eligible small business and income-generating activity applicants.",
        "url": "https://www.mudra.org.in/"
    },
    {
        "name": "PM Fasal Bima Yojana",
        "category": "Agriculture",
        "audience": "Farmers",
        "description": "A crop insurance scheme intended to protect farmers against notified crop losses.",
        "benefits": "Insurance protection for eligible notified crops and risks.",
        "eligibility": "Farmers growing notified crops in notified areas.",
        "url": "https://pmfby.gov.in/"
    },
    {
        "name": "National Means-cum-Merit Scholarship",
        "category": "Education",
        "audience": "Students",
        "description": "A scholarship programme for eligible students.",
        "benefits": "Scholarship support for selected students under programme rules.",
        "eligibility": "Students meeting notified examination, income and school criteria.",
        "url": "https://scholarships.gov.in/"
    },
    {
        "name": "Post Matric Scholarship",
        "category": "Education",
        "audience": "Students",
        "description": "Scholarship support for eligible students pursuing post-matric education.",
        "benefits": "Assistance may include maintenance allowance and eligible compulsory fees.",
        "eligibility": "Criteria depend on the scholarship, category, income and state rules.",
        "url": "https://scholarships.gov.in/"
    },
    {
        "name": "PM POSHAN",
        "category": "Food",
        "audience": "Children",
        "description": "A school meal programme for eligible children in covered schools.",
        "benefits": "Provides cooked meals on school days according to programme guidelines.",
        "eligibility": "Children enrolled in covered schools and classes.",
        "url": "https://pmposhan.education.gov.in/"
    },
    {
        "name": "Jal Jeevan Mission",
        "category": "Rural Development",
        "audience": "Rural People",
        "description": "A mission to improve rural household access to safe drinking water.",
        "benefits": "Supports household tap water connections and water services.",
        "eligibility": "Rural households covered by mission implementation in their area.",
        "url": "https://jaljeevanmission.gov.in/"
    },
    {
        "name": "PM Surya Ghar Muft Bijli Yojana",
        "category": "Energy",
        "audience": "Families",
        "description": "A rooftop solar programme for eligible residential electricity consumers.",
        "benefits": "Central financial assistance for eligible rooftop solar installations.",
        "eligibility": "Residential electricity consumers meeting scheme requirements.",
        "url": "https://pmsuryaghar.gov.in/"
    },
    {
        "name": "Atal Pension Yojana",
        "category": "Pension",
        "audience": "Workers",
        "description": "A pension scheme intended to provide old-age income security.",
        "benefits": "A guaranteed minimum monthly pension based on contribution and scheme rules.",
        "eligibility": "Eligible Indian citizens aged 18 to 40, subject to scheme conditions.",
        "url": "https://www.npscra.nsdl.co.in/"
    },
    {
        "name": "PM Jan Dhan Yojana",
        "category": "Banking",
        "audience": "Everyone",
        "description": "A financial inclusion programme promoting access to basic banking services.",
        "benefits": "Access to basic savings accounts and eligible financial services.",
        "eligibility": "Individuals eligible to open a bank account under applicable banking rules.",
        "url": "https://pmjdy.gov.in/"
    },
    {
        "name": "Stand-Up India",
        "category": "Business",
        "audience": "Entrepreneurs",
        "description": "A scheme promoting entrepreneurship among women and SC/ST communities.",
        "benefits": "Bank loans for eligible greenfield enterprises under scheme guidelines.",
        "eligibility": "Eligible women and SC/ST entrepreneurs establishing a greenfield enterprise.",
        "url": "https://www.standupmitra.in/"
    }
]

# ==================================================
# COLOUR THEME AND STYLING
# ==================================================

st.markdown("""
<style>

/* MAIN APPLICATION BACKGROUND */

.stApp {
    background-color: #F3F6FA;
    color: #172B4D !important;
}

/* MAIN TEXT */

html, body, [class*="css"] {
    color: #172B4D;
}

h1, h2, h3, h4, h5, h6 {
    color: #102A43 !important;
}

p, label, li {
    color: #243B53 !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background-color: #102A43 !important;
}

section[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* HERO SECTION */

.hero {
    background: linear-gradient(120deg, #102A43, #147D83);
    padding: 42px 25px;
    border-radius: 18px;
    text-align: center;
    margin-bottom: 25px;
}

.hero h1 {
    color: #FFFFFF !important;
    font-size: 32px;
    font-weight: 800;
}

.hero p {
    color: #FFFFFF !important;
    font-size: 17px;
}

/* NOTICE BOX */

.notice {
    background-color: #DDF3F1;
    padding: 18px;
    border-radius: 12px;
    color: #102A43 !important;
    border-left: 5px solid #147D83;
}

/* BUTTONS */

.stButton button,
.stLinkButton a {
    background-color: #147D83 !important;
    color: #FFFFFF !important;
    border: none !important;
    border-radius: 9px !important;
    font-weight: 600 !important;
}

.stButton button:hover,
.stLinkButton a:hover {
    background-color: #102A43 !important;
    color: #FFFFFF !important;
}

/* INPUT BOXES */

.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: #FFFFFF !important;
    color: #172B4D !important;
    border-radius: 8px !important;
}

/* EXPANDER */

.streamlit-expanderHeader {
    background-color: #E6EEF5 !important;
    color: #102A43 !important;
    border-radius: 8px;
}

.streamlit-expanderContent {
    background-color: #FFFFFF !important;
}

/* METRICS */

[data-testid="stMetricValue"] {
    color: #147D83 !important;
    font-weight: 800 !important;
}

[data-testid="stMetricLabel"] {
    color: #102A43 !important;
}

/* FOOTER */

.footer {
    text-align: center;
    color: #52667A;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# LANGUAGE SELECTION
# ==================================================

if "language" not in st.session_state:
    st.session_state.language = "English"

selected_language = st.sidebar.selectbox(
    "Language / भाषा",
    ["English", "हिन्दी"],
    key="language_selector"
)

st.session_state.language = (
    "Hindi" if selected_language == "हिन्दी"
    else "English"
)

def t(key):
    return TEXT[st.session_state.language].get(key, key)

# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

st.sidebar.title(t("brand"))
st.sidebar.caption(t("caption"))

PAGES = [
    t("home"),
    t("explore"),
    t("eligibility"),
    t("ask"),
    t("about")
]

page = st.sidebar.radio(
    "Navigation / नेविगेशन",
    PAGES
)

st.sidebar.divider()

st.sidebar.caption(
    "A Student Initiative | India"
)

# ==================================================
# HOME PAGE
# ==================================================

if page == t("home"):

    st.markdown(
        f"""
        <div class="hero">
            <h1>{t("welcome")}</h1>
            <p>{t("notice")}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.header(t("access"))
    st.write(t("access_text"))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            t("entries"),
            len(SCHEMES)
        )

    with col2:
        st.metric(
            t("languages"),
            "2"
        )

    with col3:
        st.metric(
            t("free"),
            "✓"
        )

    st.divider()

    st.subheader(t("what"))
    st.write(t("what_text"))

    st.markdown(
        """
        <div class="notice">
            <b>Our Purpose</b><br>
            Helping citizens discover information about government
            welfare schemes in one simple platform.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.info(
        "This is an educational prototype using a sample database."
    )

# ==================================================
# EXPLORE SCHEMES
# ==================================================

elif page == t("explore"):

    st.title(t("explore_title"))

    search = st.text_input(t("search"))

    categories = sorted(
        set(scheme["category"] for scheme in SCHEMES)
    )

    selected_category = st.selectbox(
        t("category"),
        [t("all")] + categories
    )

    filtered_schemes = []

    for scheme in SCHEMES:

        searchable = (
            scheme["name"] + " " +
            scheme["category"] + " " +
            scheme["audience"] + " " +
            scheme["description"]
        ).lower()

        matches_search = search.lower() in searchable

        matches_category = (
            selected_category == t("all")
            or scheme["category"] == selected_category
        )

        if matches_search and matches_category:
            filtered_schemes.append(scheme)

    st.write(
        f"**{len(filtered_schemes)} {t('found')}**"
    )

    if not filtered_schemes:
        st.warning(t("no_results"))

    for scheme in filtered_schemes:

        with st.expander(scheme["name"]):

            st.write("**" + t("details") + "**")
            st.write(scheme["description"])

            st.write("**" + t("audience") + "**")
            st.write(scheme["audience"])

            st.write("**" + t("benefits") + "**")
            st.write(scheme["benefits"])

            st.write("**Eligibility**")
            st.write(scheme["eligibility"])

            st.link_button(
                t("official"),
                scheme["url"]
            )

# ==================================================
# ELIGIBILITY GUIDE
# ==================================================

elif page == t("eligibility"):

    st.title(t("eligibility_title"))
    st.write(t("eligibility_text"))

    audiences = sorted(
        set(scheme["audience"] for scheme in SCHEMES)
    )

    selected_audience = st.selectbox(
        t("select_audience"),
        [t("all_audiences")] + audiences
    )

    results = [
        scheme for scheme in SCHEMES
        if selected_audience == t("all_audiences")
        or scheme["audience"] == selected_audience
    ]

    st.write(f"**{len(results)} {t('found')}**")

    for scheme in results:

        with st.expander(scheme["name"]):

            st.write(scheme["description"])

            st.write("**Eligibility Information**")
            st.write(scheme["eligibility"])

            st.write("**Benefits**")
            st.write(scheme["benefits"])

            st.link_button(
                t("official"),
                scheme["url"]
            )

    st.warning(t("limitations_text"))

# ==================================================
# ASK MERA HAQ
# ==================================================

elif page == t("ask"):

    st.title(t("ask_title"))
    st.write(t("ask_text"))

    question = st.text_input(t("question"))

    if st.button(t("find")):

        if question.strip():

            results = []

            words = question.lower().split()

            for scheme in SCHEMES:

                searchable_text = (
                    scheme["name"] + " " +
                    scheme["category"] + " " +
                    scheme["audience"] + " " +
                    scheme["description"] + " " +
                    scheme["benefits"] + " " +
                    scheme["eligibility"]
                ).lower()

                if any(
                    word in searchable_text
                    for word in words
                    if len(word) > 2
                ):
                    results.append(scheme)

            if results:

                st.success(
                    f"{len(results)} relevant scheme(s) found."
                )

                for scheme in results:

                    with st.expander(scheme["name"]):

                        st.write(scheme["description"])

                        st.write("**Benefits**")
                        st.write(scheme["benefits"])

                        st.write("**Eligibility**")
                        st.write(scheme["eligibility"])

                        st.link_button(
                            t("official"),
                            scheme["url"]
                        )

            else:
                st.info(t("no_results"))

        else:
            st.warning("Please enter a question or keyword.")

    st.caption(
        "Note: This prototype uses keyword matching with a sample "
        "database. It is not a live AI chatbot."
    )

# ==================================================
# ABOUT PROJECT
# ==================================================

elif page == t("about"):

    st.title(t("about_title"))

    st.write(t("about_text"))

    st.divider()

    st.subheader(t("mission"))
    st.write(t("mission_text"))

    st.subheader(t("vision"))
    st.write(t("vision_text"))

    st.subheader(t("technology"))
    st.write(
        "Python | Streamlit | HTML | CSS"
    )

    st.subheader(t("limitations"))
    st.write(t("limitations_text"))

    st.link_button(
        t("official"),
        "https://www.myscheme.gov.in/"
    )

# ==================================================
# FOOTER
# ==================================================

st.divider()

st.markdown(
    f"""
    <div class="footer">
        {t("footer")}<br>
        Designed to promote awareness and accessibility.
    </div>
    """,
    unsafe_allow_html=True
)
