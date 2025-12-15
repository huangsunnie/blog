# data_manager.py
import json
import os
import datetime

DATA_FILE = "articles_data.json"


def load_articles():
    """从文件加载文章数据"""
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # 确保数据格式正确
                if isinstance(data, list):
                    return data
        return []
    except Exception as e:
        print(f"加载文章数据失败: {e}")
        return []


def save_articles(articles):
    """保存文章数据到文件"""
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(articles, f, ensure_ascii=False, indent=2)
        return True
    except Exception as e:
        print(f"保存文章数据失败: {e}")
        return False


def add_article(article_data):
    """添加新文章"""
    articles = load_articles()

    # 确保文章有ID
    if 'id' not in article_data:
        # 获取下一个ID
        if articles:
            max_id = max([article.get('id', 0) for article in articles])
            article_data['id'] = max_id + 1
        else:
            article_data['id'] = 1

    articles.append(article_data)
    save_articles(articles)
    return article_data['id']


def delete_article(article_id):
    """删除文章"""
    articles = load_articles()
    new_articles = [article for article in articles if article['id'] != article_id]

    if len(new_articles) < len(articles):  # 如果有文章被删除
        save_articles(new_articles)
        return True
    return False


def delete_all_articles():
    """删除所有文章"""
    save_articles([])
    return True


def delete_articles_by_category(category):
    """删除指定分类的所有文章"""
    articles = load_articles()
    if category == "全部":
        save_articles([])
        return len(articles)
    else:
        new_articles = [article for article in articles if article['category'] != category]
        deleted_count = len(articles) - len(new_articles)
        save_articles(new_articles)
        return deleted_count


def get_articles_by_category(category):
    """根据分类获取文章"""
    articles = load_articles()

    if category == "全部":
        return sorted(articles, key=lambda x: x.get('date', ''), reverse=True)
    else:
        filtered = [article for article in articles if article.get('category') == category]
        return sorted(filtered, key=lambda x: x.get('date', ''), reverse=True)


def get_all_articles():
    """获取所有文章"""
    return load_articles()


def get_next_article_id():
    """获取下一个文章ID"""
    articles = load_articles()
    if articles:
        max_id = max([article.get('id', 0) for article in articles])
        return max_id + 1
    return 1


def initialize_example_articles():
    """初始化示例文章（只在第一次运行时）"""
    articles = load_articles()

    # 如果还没有文章，添加示例文章
    if not articles:
        example_articles = [
            {
                "id": 1,
                "title": "Vue 3.0 新特性完全解析",
                "date": "2024-03-20",
                "category": "技术博客",
                "read_time": "8分钟阅读",
                "likes": 42,
                "comments": 12,
                "excerpt": "详细介绍了Vue 3.0的新特性和使用技巧，包括Composition API、响应式系统改进等...",
                "content": "这是Vue 3.0新特性的详细内容...",
                "status": "已发布"
            },
            {
                "id": 2,
                "title": "React Hooks 最佳实践指南",
                "date": "2024-03-18",
                "category": "技术博客",
                "read_time": "10分钟阅读",
                "likes": 38,
                "comments": 8,
                "excerpt": "分享React Hooks在实际项目中的最佳实践和常见问题解决方案...",
                "content": "这是React Hooks最佳实践的详细内容...",
                "status": "已发布"
            },
            {
                "id": 3,
                "title": "周末咖啡馆的午后时光",
                "date": "2024-03-15",
                "category": "生活随笔",
                "read_time": "5分钟阅读",
                "likes": 56,
                "comments": 24,
                "excerpt": "在一个阳光明媚的午后，我坐在咖啡馆里，看着窗外人来人往，思绪飘向远方...",
                "content": "这是周末咖啡馆的详细内容...",
                "status": "已发布"
            },
            {
                "id": 4,
                "title": "TypeScript 类型系统深入理解",
                "date": "2024-03-10",
                "category": "技术博客",
                "read_time": "12分钟阅读",
                "likes": 45,
                "comments": 15,
                "excerpt": "深入解析TypeScript的类型系统，包括泛型、条件类型、映射类型等高级特性...",
                "content": "这是TypeScript类型系统的详细内容...",
                "status": "已发布"
            },
            {
                "id": 5,
                "title": "记录一次难忘的旅行经历",
                "date": "2024-03-05",
                "category": "生活随笔",
                "read_time": "7分钟阅读",
                "likes": 67,
                "comments": 18,
                "excerpt": "分享去年夏天的一次自驾游经历，沿途的美景和遇到的有趣的人和事...",
                "content": "这是旅行经历的详细内容...",
                "status": "已发布"
            }
        ]

        save_articles(example_articles)
        return example_articles

    return articles