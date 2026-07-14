import streamlit as st

st.set_page_config(
    page_title="Social Media Content Generator",
    page_icon="📱",
    layout="wide"
)

PROMPT_TEMPLATES = {
    "Instagram Caption": """
You are a professional social media content creator.

Create an engaging Instagram caption.

Topic: {topic}
Target Audience: {audience}
Tone: {tone}

Requirements:
- Catchy opening line
- 2-3 short paragraphs
- CTA at the end
- Include 10 relevant hashtags
""",
    "LinkedIn Post": """
You are a LinkedIn content strategist.

Write a professional LinkedIn post.

Topic: {topic}
Target Audience: {audience}
Tone: {tone}

Requirements:
- Strong hook
- Valuable insights
- Actionable takeaway
- CTA
""",
    "Twitter/X Post": """
You are a social media copywriter.

Write an engaging Twitter/X post.

Topic: {topic}
Target Audience: {audience}
Tone: {tone}

Requirements:
- Maximum 280 characters
- Include emojis if appropriate
- Include relevant hashtags
""",
    "Facebook Post": """
You are a Facebook marketing expert.

Create a Facebook post.

Topic: {topic}
Target Audience: {audience}
Tone: {tone}

Requirements:
- Friendly and engaging
- Storytelling style
- CTA
- Relevant hashtags
""",
    "YouTube Description": """
You are a YouTube SEO expert.

Write a YouTube video description.

Topic: {topic}
Target Audience: {audience}
Tone: {tone}

Requirements:
- SEO optimized
- Summary
- CTA
- Keywords
- Hashtags
"""
}

st.title("📱 Social Media Content Generator")
st.markdown("Generate AI prompts for creating social media content.")

platform = st.selectbox(
    "Select Platform",
    list(PROMPT_TEMPLATES.keys())
)

topic = st.text_input("Content Topic")

audience = st.text_input("Target Audience")

tone = st.selectbox(
    "Tone",
    [
        "Professional",
        "Friendly",
        "Casual",
        "Inspirational",
        "Humorous",
        "Persuasive"
    ]
)

if st.button("Generate Prompt"):

    if topic and audience:

        prompt = PROMPT_TEMPLATES[platform].format(
            topic=topic,
            audience=audience,
            tone=tone
        )

        st.success("Prompt Generated Successfully!")

        st.text_area(
            "Generated Prompt",
            prompt,
            height=350
        )

        st.download_button(
            "Download Prompt",
            prompt,
            file_name="social_media_prompt.txt"
        )

    else:
        st.warning("Please fill all fields.")

st.markdown("---")
st.caption("Developed using Python, Streamlit & Prompt Engineering")