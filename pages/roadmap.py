import streamlit as st
from resources import ROADMAP_RESOURCES
from career_roadmaps import AI_ROADMAPS


# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="Learning Roadmap",
    page_icon="🛣️",
    layout="wide"
)

# =====================================
# LOAD CSS
# =====================================

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =====================================
# HIDE STREAMLIT
# =====================================

st.markdown("""
<style>
#MainMenu{visibility:hidden;}
header{visibility:hidden;}
footer{visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# =====================================
# USER DATA
# =====================================

career = st.session_state.get(
    "dream_career",
    "Machine Learning Engineer"
)


name = st.session_state.get(
    "name",
    "User"
)

# =====================================
# HEADER
# =====================================

st.markdown(f"""
<div class="user-header">

<div class="badge">
🛣 AI Learning Journey
</div>

<h1 class="user-title">
Personalized Learning Roadmap
</h1>

<h3 class="user-subtitle">
Welcome <b>{name}</b> 👋<br>
Your goal is to become a <b>{career}</b>.
</h3>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================
# ROADMAP DATA
# =====================================

# =====================================
# DYNAMIC ROADMAP
# =====================================

if career not in AI_ROADMAPS:
    st.error(f"No roadmap available for {career}")
    st.stop()

selected = AI_ROADMAPS[career]
roadmap = []

for i, data in enumerate(selected):

    roadmap.append({

        "week": f"Week {i+1}",

        "icon": data[0].split()[0],

        "title": " ".join(data[0].split()[1:]),

       "desc": (
    f"Learn {data[0]} from beginner to professional level "
    "through practical projects, hands-on labs, and real-world applications."
),

        "duration": data[1],

        "difficulty": data[2]

    })


# =====================================
# ROADMAP UI
# =====================================

st.markdown("## 📚 Your Learning Journey")
completed = 0

for item in roadmap:
    if st.session_state.get(f"{career}_{item['week']}_{item['title']}", False):
        completed += 1

progress = completed / len(roadmap)
st.session_state["roadmap_progress"] = progress

st.progress(progress)

st.caption(f"{completed} of {len(roadmap)} modules completed")

for item in roadmap:

    with st.container(border=True):

        st.subheader(f"{item['week']} • {item['icon']} {item['title']}")

        st.write(item["desc"])

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Estimated Time", item["duration"])

        with col2:
            st.metric("Difficulty", item["difficulty"])

        # Resources
        resources = ROADMAP_RESOURCES.get(item["title"])

        if resources:

            b1, b2, b3, b4 = st.columns(4)

            with b1:
                st.link_button(
                    "📺 YouTube",
                    resources["youtube"],
                    use_container_width=True
                )

            with b2:
                st.link_button(
                    "📖 Documentation",
                    resources["docs"],
                    use_container_width=True
                )

            with b3:
                st.link_button(
                    "🎓 Free Course",
                    resources["course"],
                    use_container_width=True
                )

            with b4:
                st.link_button(
                    "💻 GitHub",
                    resources["github"],
                    use_container_width=True
                )

        else:
           st.warning(
    f"No curated resources found yet for **{item['title']}**."
)

        st.checkbox(
            "✅ Mark as Completed",
            key=f"{career}_{item['week']}_{item['title']}"
        )

    st.write("")
    st.divider()

if st.button(
    "📂 View Recommended Projects",
    use_container_width=True
):
    st.switch_page("pages/projects.py")