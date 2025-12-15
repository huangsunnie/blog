# newpost.py
import streamlit as st
import datetime
from data import add_article


def show_new_post_form():
    """显示发布新文章表单"""

    # 获取当前选中的分类，如果没有则使用默认值
    selected_category = st.session_state.get('selected_category')

    with st.form("new_post_form", clear_on_submit=True):
        # 使用 Markdown 来确保样式一致
        st.markdown('<div style="font-size: 1.1rem; font-weight: 600; color: #333; margin-bottom: 0.5rem;">文章标题*</div>', unsafe_allow_html=True)
        title = st.text_input(
            "",
            placeholder="请输入文章标题...",
            help="标题应简洁明了，能准确反映文章内容",
            label_visibility="collapsed"
        )

        # 使用当前选中的分类作为默认值
        st.markdown(f'<div style="font-size: 1.1rem; font-weight: 600; color: #333; margin-bottom: 0.5rem;">文章分类: {selected_category}</div>', unsafe_allow_html=True)
        st.write("")  # 空行

        # 隐藏的输入，用于存储分类
        category = selected_category

        st.markdown('<div style="font-size: 1.1rem; font-weight: 600; color: #333; margin-bottom: 0.5rem;">文章内容*</div>', unsafe_allow_html=True)
        content = st.text_area(
            "",
            height=300,
            placeholder="请输入文章内容...",
            help="支持Markdown格式，可以插入代码块、图片等",
            label_visibility="collapsed"
        )

        submit_button = st.form_submit_button(
            "🚀 发布文章",
            type="primary",
            use_container_width=True
        )

    st.markdown('</div>', unsafe_allow_html=True)

    if submit_button:
        if validate_form(title, content):
            # 创建文章数据
            article_data = {
                "title": title,
                "category": category,
                "content": content,
                "excerpt": content[:150] + "..." if len(content) > 150 else content,
                "date": datetime.datetime.now().strftime("%Y-%m-%d"),
                "read_time": f"{max(1, len(content) // 300)}分钟阅读",
                "likes": 0,
                "comments": 0,
                "status": "已发布"
            }

            # 保存到文件
            article_id = add_article(article_data)

            if article_id:
                st.success(f"🎉 文章 '{title}' 已发布成功！")
                # 更新session_state中的分类为刚发布的文章分类
                st.session_state.selected_category = category
                st.session_state.show_new_post = False
                st.rerun()


def validate_form(title, content):
    """验证表单数据"""
    if not title:
        st.error("❌ 请输入文章标题")
        return False

    if not content:
        st.error("❌ 请输入文章内容")
        return False

    if len(content) < 50:
        st.warning("⚠️ 文章内容建议至少50字")
        return True  # 仍然允许提交，只是警告

    return True