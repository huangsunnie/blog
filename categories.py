# categories.py
import streamlit as st
from data import get_articles_by_category, delete_articles_by_category, delete_article, initialize_example_articles
from newpost import show_new_post_form


def show_categories_page():
    """显示文章分类页面"""
    # 初始化示例文章（如果文件不存在）
    if 'articles_initialized' not in st.session_state:
        initialize_example_articles()
        st.session_state.articles_initialized = True

    # 检查是否显示发布新文章表单
    if st.session_state.get('show_new_post', False):
        display_new_post_page()
    else:
        display_categories_main_page()


def display_categories_main_page():
    """显示分类主页面"""
    # 大标题
    st.markdown(
        '<div style="font-size: 2.5rem; font-weight: bold; color: #333; margin-bottom: 1.5rem; text-align: center; padding-bottom: 1rem;">📝 我的个人博客</div>',
        unsafe_allow_html=True
    )

    # 发布新文章按钮
    if st.button("📤 发布新文章",
                 use_container_width=True,
                 type="primary"):
        st.session_state.show_new_post = True
        st.rerun()



    # 分类选择器
    st.markdown("#### 🔍 选择分类：")
    categories = ["全部", "技术博客", "生活随笔"]

    # 获取当前选中的分类，如果没有则使用"全部"
    selected_category = st.session_state.get('selected_category', '全部')

    selected_category = st.radio(
        "选择文章分类:",
        categories,
        horizontal=True,
        index=categories.index(selected_category) if selected_category in categories else 0,
        key="category_selector",
        label_visibility="collapsed"
    )

    # 更新选中的分类
    if selected_category != st.session_state.selected_category:
        st.session_state.selected_category = selected_category
        st.rerun()

    st.markdown("---")

    # 显示个人信息区域
    st.markdown("#### 👤 关于作者")
    st.markdown("""
    <div style="background-color: #f0f8ff; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #4A90E2;">
        <h4 style="margin-top: 0; color: #333;">大家好，我是前端开发者小A，热爱技术分享~</h4>
        <p style="color: #666;">在这里我会分享：</p>
        <ul style="color: #666;">
            <li>前端开发技术教程</li>
            <li>项目实战经验</li>
            <li>生活感悟与思考</li>
            <li>读书笔记与推荐</li>
        </ul>
        <p style="color: #666;">欢迎关注和交流！</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 显示选中分类的文章
    display_articles_by_category(selected_category)


def display_new_post_page():
    """显示发布新文章页面"""
    col1, col2 = st.columns([1, 5])
    with col1:
        if st.button("⬅️ 返回", use_container_width=True):
            st.session_state.show_new_post = False
            st.rerun()

    with col2:
        st.markdown(
            '<div style="font-size: 2rem; font-weight: bold; color: #333;">📤 发布新文章</div>',
            unsafe_allow_html=True
        )

    st.markdown("---")
    # 调用newpost.py中的函数
    show_new_post_form()


def display_articles_by_category(category):
    """显示选中分类的文章"""
    st.subheader(f"📖 {category}文章列表")

    # 从文件加载文章
    articles = get_articles_by_category(category)

    if articles:
        # 统计信息
        col1, col2 = st.columns([3, 1])
        with col1:
            st.info(f"当前查看 **{category}** 分类 (共 {len(articles)} 篇文章)")

        with col2:
            # 清空当前分类的文章
            if len(articles) > 0 and st.button("🗑️ 清空此分类", use_container_width=True,
                                               help=f"删除所有{category}文章"):
                deleted_count = delete_articles_by_category(category)
                if deleted_count > 0:
                    st.success(f"✅ 已删除{category}分类的{deleted_count}篇文章！")
                    st.rerun()

        # 显示文章列表（带删除按钮）
        for idx, article in enumerate(articles):
            display_article_card_with_delete(article, idx)
    else:
        st.info(f"**{category}** 分类下暂无文章，快去发布一篇吧！")

        if st.button("📝 现在去发布", type="primary"):
            st.session_state.show_new_post = True
            st.rerun()


def display_article_card_with_delete(article, index):
    """显示带删除按钮的文章卡片"""
    col_left, col_right = st.columns([9, 1])

    with col_left:
        st.markdown(f"""
        <div style="background-color: white; padding: 1.5rem; border-radius: 10px; 
                    margin-bottom: 1rem; box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    border-left: 4px solid #4A90E2;">
            <h3 style="margin-top: 0; color: #333;">{article['title']}</h3>
            <div style="color: #666; font-size: 0.9rem; margin-bottom: 1rem;">
                <span style="background-color: #e6f7ff; padding: 0.2rem 0.8rem; 
                      border-radius: 12px; color: #1890ff; font-size: 0.85rem;">
                    {article['category']}
                </span>
                <span style="margin: 0 10px;">•</span>
                <span>{article.get('date', '未知日期')}</span>
                <span style="margin: 0 10px;">•</span>
                <span>⏱️ {article.get('read_time', '未知')}</span>
            </div>
            <p style="color: #555; line-height: 1.6;">{article['excerpt']}</p>
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div style="color: #666;">
                    <span style="margin-right: 15px;">❤️ {article.get('likes', 0)}</span>
                    <span>💬 {article.get('comments', 0)}</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_right:
        # 删除按钮
        delete_key = f"delete_{article['id']}_{index}"
        if st.button("🗑️", key=delete_key, help="删除文章", use_container_width=True):
            if delete_article(article['id']):
                st.success(f"✅ 已删除文章: {article['title']}")
                st.rerun()