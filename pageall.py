import streamlit as st
from blog import show_home_page
from about import show_about_page
from categories import show_categories_page


class BlogLayout:
    """博客布局类"""

    def __init__(self):
        """初始化布局"""
        self.setup_page_config()
        self.apply_custom_styles()
        self.initialize_session_state()

    def setup_page_config(self):
        """设置页面配置"""
        st.set_page_config(
            page_title="个人博客",
            page_icon="📝",
            layout="wide"
        )

    def apply_custom_styles(self):
        """应用自定义样式"""
        st.markdown("""
        <style>
            /* 整体布局 */
            .main-content {
                padding: 1rem 2rem;
            }

            .sidebar-content {
                padding: 1rem;
            }

            /* 博客文章样式 */
            .blog-post {
                background-color: white;
                padding: 1.5rem;
                border-radius: 10px;
                margin-bottom: 1.5rem;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                border-left: 4px solid #4A90E2;
            }

            .blog-post h3 {
                color: #333;
                margin-top: 0;
                margin-bottom: 0.5rem;
            }

            .post-meta {
                color: #666;
                font-size: 0.9rem;
                margin-bottom: 1rem;
            }

            .category-tag {
                display: inline-block;
                background-color: #e6f7ff;
                padding: 0.2rem 0.8rem;
                border-radius: 12px;
                color: #1890ff;
                font-size: 0.85rem;
            }

            .read-time {
                color: #999;
                font-size: 0.85rem;
            }

            /* 分类按钮样式 */
            .category-btn {
                transition: all 0.3s ease;
            }

            /* 个人简介样式 */
            .profile-header {
                background: linear-gradient(135deg, #4A90E2, #7B68EE);
                padding: 2rem;
                border-radius: 10px;
                color: white;
                margin-bottom: 2rem;
            }

            .skill-bar {
                height: 8px;
                background-color: #f0f0f0;
                border-radius: 4px;
                margin: 0.5rem 0 1rem 0;
            }

            .skill-fill {
                height: 100%;
                background: linear-gradient(90deg, #4A90E2, #7B68EE);
                border-radius: 4px;
            }

            /* 文章管理样式 */
            .article-management {
                background-color: #f8f9fa;
                border-radius: 10px;
                padding: 1.5rem;
                margin-bottom: 2rem;
                border: 1px solid #dee2e6;
            }

            /* 发布表单样式 - 修改字体样式 */
            .publish-form {
                background-color: white;
                border-radius: 10px;
                padding: 2rem;
                margin-top: 2rem;
                box-shadow: 0 2px 15px rgba(0,0,0,0.1);
            }

            /* 统一发布表单中的字体样式 */
            .publish-form label {
                font-size: 1.1rem !important;
                font-weight: 600 !important;
                color: #333 !important;
                margin-bottom: 0.5rem !important;
            }

            /* 文章分类显示样式 */
            .publish-form .stMarkdown strong {
                font-size: 1.1rem !important;
                font-weight: 600 !important;
                color: #333 !important;
            }

            /* 表单输入框文字样式 */
            .publish-form textarea, 
            .publish-form input {
                font-size: 1rem !important;
                font-weight: 400 !important;
            }

            /* 表单帮助文本样式 */
            .publish-form .stTooltipIcon {
                font-size: 1rem !important;
            }
        </style>
        """, unsafe_allow_html=True)

    def initialize_session_state(self):
        """初始化session_state"""
        if 'current_page' not in st.session_state:
            st.session_state.current_page = "博客首页"
        if 'selected_category' not in st.session_state:
            st.session_state.selected_category = "全部"
        if 'show_new_post' not in st.session_state:
            st.session_state.show_new_post = False

    def create_layout(self):
        """创建整体布局"""
        # 左侧导航栏
        with st.sidebar:
            self.display_sidebar()

        # 右侧主内容区域
        with st.container():
            st.markdown('<div class="main-content">', unsafe_allow_html=True)
            self.show_current_page()
            st.markdown('</div>', unsafe_allow_html=True)

    def display_sidebar(self):
        """显示左侧导航栏"""
        st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)

        # 博客标题
        st.markdown("# 📝个人博客日志")
        st.markdown("---")

        # 导航菜单 - 只保留要求的三个菜单
        pages = ["博客首页", "个人简介", "文章分类"]

        # 使用单选按钮代替按钮，更符合常规导航体验
        selected_page = st.radio(
            "导航菜单",
            pages,
            index=pages.index(st.session_state.current_page) if st.session_state.current_page in pages else 0,
            label_visibility="collapsed"
        )

        # 更新当前页面状态
        if selected_page != st.session_state.current_page:
            st.session_state.current_page = selected_page
            if selected_page == "文章分类":
                st.session_state.selected_category = "全部"
                st.session_state.show_new_post = False  # 重置发布文章状态
            st.rerun()

        st.markdown("---")

    def show_current_page(self):
        """显示当前页面内容"""
        current_page = st.session_state.current_page

        if current_page == "博客首页":
            show_home_page()
        elif current_page == "个人简介":
            show_about_page()
        elif current_page == "文章分类":
            show_categories_page()
        else:
            show_home_page()  # 默认显示首页


def main():
    """主函数"""
    blog = BlogLayout()
    blog.create_layout()


if __name__ == "__main__":
    main()