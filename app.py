import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import streamlit.components.v1 as components
from bertopic import BERTopic
import os

# Set the page configuration with light mode or custom theme
st.set_page_config(
    page_title="Climate Legislation Trends Dashboard",
    layout="wide",
    page_icon="🌿",
    initial_sidebar_state="expanded"
)

# Custom CSS for climate-related colors
st.markdown(
    """
    <style>
    /* Tab colors */
    .stTabs [data-baseweb="tab"] {
        background-color: transparent; /* No background color for tabs */
        color: white; /* Default tab text color */
        font-weight: bold; /* Emphasize text */
    }

    /* Hover color for all tabs */
    .stTabs [data-baseweb="tab"]:hover {
        color: #38761d; /* Greenish text on hover */
    }

    /* Active tab color */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        color: #0b6623; /* Forest Green for active tab */
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Dashboard Title
st.title("🌍 Exploring Climate-Related Legislation Trends")


# Tab Structure
tabs = st.tabs(["Overview", "Topic Trends", "Sponsorship Analysis", "Vote Trends", "Topic Correlations"])

# Tab 1: Overview
with tabs[0]:
    st.header("About Dashboard")
    st.write("This dashboard provides a comprehensive analysis of climate-related legislation trends, focusing on data from passed bills. It is designed to help policymakers, researchers, and stakeholders understand key patterns in climate legislation. With interactive visualizations, the dashboard offers insights into emerging topics, sponsorship dynamics, voting patterns, and topic relationships.")
    
    # Subtitle: Why BERTopic?
    st.subheader("Why BERTopic?")
    st.write("""
    BERTopic is an advanced topic modeling technique that uses embeddings and clustering to extract coherent topics from textual data. Unlike traditional models like LDA, BERTopic is capable of capturing nuanced patterns in textual data, making it particularly useful for analyzing legislative text.  
    **Example from Analysis**:
    - Using BERTopic, we identified the top 12 topics in climate-related bills. These topics provided valuable insights into recurring themes such as electric vehicles, environmental justice, tax credits, and emissions reduction.
    - The model also allowed us to trace topic trends and across states and party, helping us uncover key legislative focus areas.
    """)

    # Subtitle: Data Overview
    st.subheader("Data Overview")
    st.write("""
    The data for this analysis was collected using the LegiScan API, covering various states and legislative sessions. For this dashboard, we focused on the top states with the highest number of passed bills in their regular sessions.  
    **Top 10 States Analyzed**:
    - Arkansas (AR)
    - Virginia (VA)
    - Maryland (MD)
    - California (CA)
    - Illinois (IL)
    - New York (NY)
    - Tennessee (TN)
    - Hawaii (HI)
    - Louisiana (LA)
    - Oregon (OR)
    """)

    # Subtitle: Why IRA Focused?
    st.subheader("Why IRA Focused?")
    st.write("""
    The Inflation Reduction Act (IRA) of 2022 represents the largest climate investment in U.S. history, making it a pivotal milestone for climate-related legislation. The IRA focuses heavily on climate initiatives and tax credits designed to drive decarbonization and clean energy adoption.  
    **Key Highlights of IRA**:
    - **Investment**: A historic $369 billion allocated for energy security and climate change programs over 10 years.
    - **Tax Credits**: Substantial tax incentives for renewable energy projects, electric vehicles, and energy-efficient home upgrades.
    - **Climate Goals**: Expected to cut U.S. greenhouse gas emissions by approximately 40% below 2005 levels by 2030.
    - **Jobs**: Projected to create thousands of clean energy jobs across the country, boosting economic growth in green sectors.
    - **Equity Focus**: Emphasizes environmental justice by investing in underserved communities disproportionately affected by climate change.
    """)



# Tab 2: Topic Trends
with tabs[1]:
    st.header("Topic Trends")
    st.write("Explore the top 12 topics identified from passed climate-related bills. This section highlights the prominent themes in legislation using dynamic word clouds, offering a snapshot of the language and focus areas of these bills.")

    # Directory containing the word cloud HTML files
    wordcloud_dir = "wordclouds"

    # Get the list of HTML files in the directory
    wordcloud_files = sorted(
        [f for f in os.listdir(wordcloud_dir) if f.startswith("wordcloud_topic_") and f.endswith(".html")],
        key=lambda x: int(x.split("_")[-1].split(".")[0])  # Extract the topic number from the filename
    )

    # Display the word clouds in a 2-column, 6-row layout
    cols = st.columns(2)  # Create 2 columns
    for i, file in enumerate(wordcloud_files[:12]):  # Limit to 12 topics
        with cols[i % 2]:  # Alternate between the columns
            st.write(f"**Topic {i} Word Cloud**")
            # Embed the HTML file
            file_path = os.path.join(wordcloud_dir, file)
            with open(file_path, "r") as f:
                wordcloud_html = f.read()
            components.html(wordcloud_html, height=400) 

    # Topic Insights
    st.subheader("Key Insights")
    
    # Topic-Specific Focus
    st.markdown("### 🌱 **Topic-Specific Focus**")
    st.write("""
    - Focus on **waste management** and **recycling initiatives** as seen in terms like 'waste,' 'recycling,' and 'solid.'
    - Emphasis on **biodiversity conservation** with words like 'wildlife,' 'forest,' 'tree,' and 'habitat.'
    - Increasing attention to **renewable energy** portfolios and public utility regulations, with keywords like 'renewable' and 'utility.'
    """)

    # Geographic and Administrative References
    st.markdown("### 📍 **Geographic and Administrative References**")
    st.write("""
    - State-specific mentions like 'Arkansas' and 'Baltimore' indicate a focus on localized climate challenges.
    - Keywords such as 'section,' 'municipal,' and 'town' reflect efforts in **urban planning** and **local governance**.
    """)

    # Transportation and Emissions
    st.markdown("### 🚗 **Transportation and Emissions**")
    st.write("""
    - Terms like 'vehicle,' 'electric,' 'zeroemission,' and 'fleet' highlight legislative efforts to promote **clean transportation** and reduce emissions.
    """)

    # Fiscal and Policy Mechanisms
    st.markdown("### 💵 **Fiscal and Policy Mechanisms**")
    st.write("""
    - Emphasis on funding mechanisms and financial incentives, with terms such as 'appropriation,' 'fiscal,' and 'credit.'
    """)

    # Miscellaneous Themes
    st.markdown("### 🌐 **Miscellaneous Themes**")
    st.write("""
    - Wildlife management policies are reflected in terms like 'license,' 'fish,' and 'game.'
    """)      

# Tab 3: Sponsorship Analysis
with tabs[2]:  # Sponsorship Analysis Tab
    st.header("Sponsorship Analysis")
    st.write("Delve into the analysis of sponsorship patterns for the top 12 topics, broken down by party and state. This section provides insights into which parties and regions are leading the charge on climate-related legislation")
    
    # Display Sponsorship by Party
    st.subheader("Sponsorship Distribution by Party")
    st.image("sponsorship_by_party.png", use_column_width=True)
    st.write("""
    The chart above highlights the party-wise distribution of sponsored climate-related bills:
    - 🟦 **Democratic Sponsors**: A significant majority of the bills are sponsored by members of the Democratic Party, reflecting their strong focus on climate-related policies and legislation.
    - 🟩 **Republican Sponsors**: While fewer in number, Republican sponsors also contribute notably to climate-related legislation, indicating some level of bipartisan interest in addressing climate issues.
    - **Insight**: The higher sponsorship from Democrats aligns with their policy platforms prioritizing climate change and renewable energy investments. However, the participation of Republicans shows potential for bipartisan collaboration in specific areas like energy efficiency and conservation.
    """)

    # Display Sponsorship by State
    st.subheader("Sponsorship Distribution by State")
    st.image("sponsorship_by_state.png", use_column_width=True)
    st.write("""
    The chart above highlights the state-wise distribution of sponsored climate-related bills:
    - 🌟 **Arkansas** leads with the highest number of sponsored bills, showcasing a strong legislative push toward climate-related issues in this state.
    - 🌟 **California** and **Maryland** follow closely, reflecting their commitment to proactive climate legislation, likely influenced by their progressive environmental policies.
    - 🏞️ **Massachusetts**, **Illinois**, and **Oregon** also contribute significantly, indicating regional focus on renewable energy, conservation, and emissions reduction.
    - 🏙️ States like **New York** and **Virginia** are moderately active, reflecting their balanced approach to addressing climate challenges.
    - 🌴 States like **Hawaii** and **Louisiana** have fewer sponsored bills, potentially due to localized priorities or fewer legislative sessions.
    - 🛤️ States with the least activity, such as **New Jersey**, **Minnesota**, and **Tennessee**, highlight opportunities for increased legislative focus on climate issues.
    """)

    st.write("These insights provide a geographic overview of climate-related legislative efforts, emphasizing the leadership of certain states in addressing climate change while identifying areas for potential growth.")



# Tab 4: Vote Trends
with tabs[3]:
    st.header("Vote Trends")
    st.write("Analyze voting patterns for the top 12 topics, with a focus on bipartisan support and voting dynamics before and after the Inflation Reduction Act (IRA). This section uncovers shifts in voting behavior and party alliances on climate issues.")

    # Add the first visualization: Vote Trends Pre-/Post-IRA
    st.subheader("Vote Trends Pre-/Post-IRA")
    st.image("vote_trends_pre_post_ira_enhanced.png", caption="Vote Trends Pre-/Post-IRA for Top Topics", use_column_width=True)
    st.write("""
    The chart above illustrates the voting trends for climate-related bills before and after the passage of the Inflation Reduction Act (IRA):
    
    - 🟠 **Pre-IRA Voting Trends**:
        - Pre-IRA bills received higher numbers of "Yea" votes for most topics, reflecting strong historical support for climate-related legislation.
        - Key topics such as **Topic 0 (Appropriations)** and **Topic 2 (Property/Tax Credit)** show substantial "Yea" votes, indicating legislative prioritization of fiscal and infrastructure measures.
    
    - 🔵 **Post-IRA Voting Trends**:
        - Post-IRA trends show a noticeable decline in "Yea" votes for some topics, suggesting possible shifts in legislative focus or priorities.
        - Certain topics like **Topic 3 (Wildlife Management)** and **Topic 5 (Conservation/Parcel Management)** maintain relatively consistent support, demonstrating ongoing bipartisan interest in environmental and conservation efforts.

    - **Insights**:
        - The Inflation Reduction Act marks a turning point in legislative priorities, shifting focus toward tax credits, clean energy investments, and environmental equity.
        - Some decline in post-IRA voting may reflect changes in legislative dynamics or competing priorities for federal and state governments.
        - Topics related to conservation and natural resource management continue to receive steady support, showcasing their bipartisan appeal.

    """)

    # Add the second visualization: Bipartisan Support Barplot
    st.subheader("Bipartisan Support for Topics")
    st.image("enhanced_bipartisan_support_barplot.png", caption="Bipartisan Support for Topics (Yea Votes)", use_column_width=True)
    st.write("""
    The chart highlights the bipartisan support for top climate-related topics, showcasing voting patterns across political affiliations:
    
    - **Democratic (D)**:
        - Strong support across most topics, particularly for **Topic 1 (Energy and Appropriations)** and **Topic 5 (Conservation)**, with over 6,000 "Yea" votes each.
        - Democrats demonstrate consistent leadership in promoting climate-related legislation.

    - **Republican (R)**:
        - Significant contributions to certain topics, such as **Topic 0 (Appropriations)**, with over 13,500 "Yea" votes, reflecting bipartisan support for fiscal and budgetary measures related to climate.
        - Lower participation in other topics suggests a selective approach to climate policy.

    - **Independent (I)**:
        - Minimal contributions, with only a few "Yea" votes observed across topics, reflecting limited independent involvement in legislative climate efforts.

    - **Key Insights**:
        - 🌟 Topics related to fiscal measures (e.g., appropriations and tax incentives) receive notable bipartisan support, underscoring their universal appeal.
        - 🌱 Conservation and renewable energy remain areas with strong Democratic leadership and some bipartisan alignment.
        - 🔍 Topics with low Republican or Independent support may indicate polarized views or differing priorities in addressing specific climate challenges.

    """)

# Tab 5: Topic Correlations
with tabs[4]:  # Assuming this is the "Topic Correlations" tab
    st.header("Topic Correlations")
    st.write("Explore the relationships and co-occurrences between the top 12 topics from passed bills. This section uses a chord diagram to visually demonstrate how different themes interconnect and influence one another.")
    
    # Embed the saved HTML chord diagram
    chord_html_path = "topic_chord_diagram.html"
    with open(chord_html_path, 'r') as f:
        chord_diagram = f.read()
    components.html(chord_diagram, height=850, scrolling=True)

    st.write("""
    The chord diagram above highlights the interconnectedness of various topics within passed climate-related bills. Below are key insights based on the relationships:

    - **Strong Interdependencies**:
        - **Topic 0: Arkansas_Appropriation_Fiscal_Year** shows strong connections with other topics, particularly fiscal and resource management-related themes, indicating its central role in climate-related policymaking.
        
    - **Insights from the Green Highlights**:
        - Hovering over specific nodes in the chord diagram reveals the direct connections between a selected topic and its related counterparts.
        - For example, **Topic 5: Town_Parcel_Municipality_Land** shows no connections to any topics.

    - **Actionable Insight**:
        - These connections indicate opportunities for policymakers to address interconnected topics together for more holistic and impactful climate legislation. For instance, combining fiscal measures (**Topic 0**) with clean energy investments (**Topic 10**) could maximize the effectiveness of climate-related initiatives.
    """)

# Footer
st.sidebar.info("Developed by Vaishnavi Singh")
# Path to your QR code image
qr_code_path = "mentimeter_qr_code.png"  

# Add QR Code to the sidebar
st.sidebar.image(qr_code_path, caption="Scan the QR code for a short survey")
