import streamlit as st

# Definer skabelonen med pladsholdere
template = """
Explore the latest trends, innovations, and challenges within the {field}, with a specific focus on {geographical_area}. 
Extend this investigation to cover key sectors such as {sector_names}, examining how {strategies} are uniquely applied and evolved in these areas.

General {field} Focus:
Keywords to Monitor: {keywords}.
Countries of Interest: {countries}.

Specific Areas of Focus:
Assess the effectiveness and ROI of current {strategies} across various platforms or mediums.
Explore innovations in {tools} gaining traction.
Identify challenges in creating cohesive {experiences}.
Highlight case studies of successful {experiences}, detailing strategies and outcomes.

Sector-Specific Insights:
In addition to the general {field} overview, delve into sector-specific {experiences} and developments. For each sector, focus on:
How {field} trends are impacting the sector.
Unique {strategies} and their outcomes.
Innovations and challenges specific to the sector's {field}.
Successful case studies within each sector, emphasizing {field}'s role.

Objective:
To aggregate and summarize the most current and relevant information that aids in understanding the dynamic {field} landscape in {geographical_area}, alongside a deep dive into specific industry sectors. This research should offer insights into best practices, technological advancements, market trends, and the competitive environment, tailored to both a general and sector-specific audience.

Output Format:
Provide comprehensive summaries organized by themes - 'General {field} Trends,' 'Sector-Specific Insights,' and within each sector, sub-themes such as 'Innovations,' 'Challenges,' and 'Case Studies.' Each summary should encapsulate key findings, actionable insights, and include links to original articles or research sources for in-depth exploration. The tone should remain informative and concise, aimed at industry professionals seeking to navigate and excel in their {field} endeavours across diverse sources.
"""

# Streamlit interface
st.title("Tekstgenerering med Dynamiske Pladsholdere")

# Brugerinput til hver pladsholder
field = st.text_input("Industry or field", "Digital Strategi")
geographical_area = st.text_input("Geographical or Demographical Areas of Interest", "Europa")
sector_names = st.text_input("List sector name(s)", "Sundhed, Finans, Detailhandel")
strategies = st.text_input("Field-Specific Strategies or Practices", "Digital Transformation, Automatisering")
keywords = st.text_input("List of Relevant Keywords", "AI, Blockchain, Cloud Computing")
countries = st.text_input("List of Countries or Regions", "Tyskland, UK, Frankrig")
tools = st.text_input("Field-Specific Tools or Platforms", "CRM Systemer, AI-drevet Analyse")
experiences = st.text_input("Field-Specific Experiences or Strategies", "Brugeroplevelse, Brand Konsistens")

# Knap til at generere tekst
if st.button("Generer Tekst"):
    # Erstat pladsholdere med brugerinput
    generated_text = template.format(
        field=field,
        geographical_area=geographical_area,
        sector_names=sector_names,
        strategies=strategies,
        keywords=keywords,
        countries=countries,
        tools=tools,
        experiences=experiences
    )
    # Vis den genererede tekst
    st.subheader("Genereret Tekst")
    st.write(generated_text)