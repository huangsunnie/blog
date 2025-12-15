import streamlit as st


def show_about_page():
    """显示个人简介页面"""
    st.markdown("""
    <div class="profile-header">
        <h1 style="color: white; margin-bottom: 0.5rem;">👤 个人简介</h1>
        <p style="color: rgba(255,255,255,0.9); font-size: 1.1rem;">技术爱好者 | 终身学习者 | 博客作者</p>
    </div>
    """, unsafe_allow_html=True)

    # 基本信息
    col1, col2 = st.columns([1, 2])

    with col1:
        # 头像
        st.image("https://via.placeholder.com/250x250/4A90E2/FFFFFF?text=Blogger",
                 caption="", use_container_width=True)

        # 基本信息卡片
        with st.container():
            st.markdown("### 📋 基本信息")
            st.markdown("**🎂 年龄:** 28岁")
            st.markdown("**📍 地点:** 上海")
            st.markdown("**🎓 学历:** 计算机硕士")
            st.markdown("**💼 职业:** 全栈工程师")

    with col2:
        st.markdown("### 🌟 关于我")
        st.markdown("""
        你好！我是 Alex，一名充满激情的全栈开发者。从事软件开发已有6年时间，
        专注于Web技术栈和云原生应用开发。

        我相信技术的力量可以改变世界，也享受通过代码创造价值的乐趣。
        在我的博客中，我不仅分享技术知识，也记录生活感悟和成长思考。

        **🎯 我的使命:**
        - 通过技术解决实际问题
        - 分享知识，帮助他人成长
        - 持续学习，保持好奇心
        - 在技术与人之间架起桥梁
        """)

    st.markdown("---")

    # 技术栈
    display_skills_section()

    # 工作经历
    display_experience_section()

    # 联系方式
    display_contact_section()


def display_skills_section():
    """显示技能部分"""
    st.subheader("💻 技术栈")

    skills = [
        {"name": "Python/Flask/Django", "level": 90},
        {"name": "JavaScript/React/Vue", "level": 85},
        {"name": "Docker/Kubernetes", "level": 80},
        {"name": "AWS/云服务", "level": 75},
        {"name": "数据库设计", "level": 85},
        {"name": "系统架构", "level": 80}
    ]

    cols = st.columns(2)
    for idx, skill in enumerate(skills):
        with cols[idx % 2]:
            st.markdown(f"**{skill['name']}**")
            st.markdown(f"""
            <div class="skill-bar">
                <div class="skill-fill" style="width: {skill['level']}%"></div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown(f"{skill['level']}%")
            st.write("")


def display_experience_section():
    """显示工作经历"""
    st.subheader("📈 工作经历")

    experiences = [
        {
            "company": "科技先锋有限公司",
            "position": "高级全栈工程师",
            "period": "2021-至今",
            "description": "负责核心产品的架构设计和开发，带领团队完成多个重要项目。"
        },
        {
            "company": "创新软件公司",
            "position": "后端开发工程师",
            "period": "2019-2021",
            "description": "参与企业级应用开发，专注于API设计和性能优化。"
        },
        {
            "company": "数字创业公司",
            "position": "全栈开发工程师",
            "period": "2017-2019",
            "description": "从0到1参与产品开发，负责前后端全链路开发工作。"
        }
    ]

    for exp in experiences:
        with st.container():
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown(f"**{exp['company']}**")
                st.markdown(f"*{exp['position']}*")
                st.markdown(exp['description'])
            with col2:
                st.markdown(f"`{exp['period']}`")
            st.markdown("---")


def display_contact_section():
    """显示联系方式"""
    st.subheader("📞 联系方式")

    contact_cols = st.columns(4)

    with contact_cols[0]:
        st.markdown("**📧 邮箱**")
        st.markdown("alex@example.com")

    with contact_cols[1]:
        st.markdown("**🐙 GitHub**")
        st.markdown("github.com/alexchen")

    with contact_cols[2]:
        st.markdown("**💼 LinkedIn**")
        st.markdown("linkedin.com/in/alexchen")

    with contact_cols[3]:
        st.markdown("**🐦 微博**")
        st.markdown("@alex_blogger")