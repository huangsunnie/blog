import streamlit as st


def show_home_page():
    """显示博客首页"""
    st.title("🏠 博客首页")
    st.markdown("---")

    # 欢迎区域
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### ✨ 欢迎来到我的博客空间")
        st.markdown("这里记录了我的技术学习、生活感悟和读书心得，希望能与你分享交流。")

    with col2:
        # 博客统计
        st.metric("📄 文章总数", "42")
        st.metric("📊 分类数量", "5")
        st.metric("👥 访问人数", "1,234")

    st.markdown("---")

    # 最新文章
    st.subheader("📚 最新文章")
    display_latest_articles()

    # 推荐文章
    st.subheader("⭐ 推荐文章")
    display_featured_articles()


def display_latest_articles():
    """显示最新文章列表"""
    latest_articles = [
        {
            "id": 1,
            "title": "Streamlit深度实践：构建个人博客系统",
            "date": "2024-03-20",
            "category": "技术",
            "excerpt": "详细介绍了如何使用Streamlit框架快速构建一个功能完善的个人博客系统，包括页面布局、状态管理和数据持久化...",
            "read_time": "8分钟阅读",
            "likes": 42
        },
        {
            "id": 2,
            "title": "Python异步编程完全指南",
            "date": "2024-03-18",
            "category": "技术",
            "excerpt": "从基础概念到实际应用，全面讲解Python中的async/await、asyncio等异步编程技术...",
            "read_time": "12分钟阅读",
            "likes": 38
        },
        {
            "id": 3,
            "title": "春日京都：一场与樱花的邂逅",
            "date": "2024-03-15",
            "category": "旅行",
            "excerpt": "在樱花盛开的季节，漫步在京都的古街小巷，感受传统与现代的完美融合...",
            "read_time": "6分钟阅读",
            "likes": 56
        },
        {
            "id": 4,
            "title": "《原则》读书笔记与思考",
            "date": "2024-03-10",
            "category": "读书",
            "excerpt": "瑞·达利欧在《原则》中分享的生活和工作原则，对我的思维方式产生了深远影响...",
            "read_time": "10分钟阅读",
            "likes": 29
        }
    ]

    for article in latest_articles:
        display_article_card(article)


def display_featured_articles():
    """显示推荐文章"""
    featured_articles = [
        {
            "id": 5,
            "title": "深度学习入门：从零到一",
            "date": "2024-02-28",
            "category": "技术",
            "excerpt": "适合初学者的深度学习入门指南，包含基础概念、环境搭建和第一个神经网络实现...",
            "read_time": "15分钟阅读",
            "likes": 78
        },
        {
            "id": 6,
            "title": "高效工作流：我的时间管理法则",
            "date": "2024-02-20",
            "category": "生活",
            "excerpt": "分享我多年来总结的时间管理和工作效率提升方法，希望能帮助更多人...",
            "read_time": "7分钟阅读",
            "likes": 64
        }
    ]

    cols = st.columns(2)
    for idx, article in enumerate(featured_articles):
        with cols[idx]:
            display_article_card(article, compact=True)


def display_article_card(article, compact=False):
    """显示文章卡片"""
    if compact:
        st.markdown(f"""
        <div class="blog-post">
            <h4>{article['title']}</h4>
            <div class="post-meta">
                <span class="category-tag">{article['category']}</span>
                <span style="margin: 0 10px;">•</span>
                <span>{article['date']}</span>
            </div>
            <p>{article['excerpt'][:80]}...</p>
            <div style="display: flex; justify-content: space-between;">
                <span class="read-time">{article['read_time']}</span>
                <span>❤️ {article['likes']}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="blog-post">
            <h3>{article['title']}</h3>
            <div class="post-meta">
                <span class="category-tag">{article['category']}</span>
                <span style="margin: 0 10px;">•</span>
                <span>{article['date']}</span>
                <span style="margin: 0 10px;">•</span>
                <span class="read-time">{article['read_time']}</span>
            </div>
            <p>{article['excerpt']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <button style="background: none; border: 1px solid #4A90E2; color: #4A90E2; 
                        padding: 0.3rem 1rem; border-radius: 4px; cursor: pointer;">
                    阅读全文 →
                </button>
                <div>
                    <span style="margin-right: 15px;">❤️ {article['likes']}</span>
                    <span>💬 评论</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)