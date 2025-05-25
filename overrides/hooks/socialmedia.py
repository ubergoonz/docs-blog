from textwrap import dedent
import urllib.parse
import re

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
linkedin_sharer = "https://www.linkedin.com/sharing/share-offsite/"  # LinkedIn share URL
wa_sharer = "https://wa.me/?text="  # WhatsApp share URL
tg_sharer = "https://t.me/share/url?url="  # Telegram share URL
notion_url = "https://www.notion.so/"
onenote_url = "https://www.onenote.com/"
wechat_url = "https://web.wechat.com/"
xiaohongshu_url = "https://www.xiaohongshu.com/"
line_sharer = "https://social-plugins.line.me/lineit/share?url="  # LINE share URL
include = re.compile(r"blog/[1-9].*")

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if page.meta.get('template') != 'blog-post.html': # Only apply the social media tags to blog posts
    #if not include.match(page.url):
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')


    return markdown + dedent(f"""
    <div style="text-align: center;" markdown="1">
    
    ---

    :octicons-share-android-16: **Share on Socials** 
    [:simple-x:]({x_intent}?text={page_title}&url={page_url}){{ :target="_blank" title="Share on X" }}
    [:simple-facebook:]({fb_sharer}?u={page_url}){{ :target="_blank" title="Share on Facebook" }}
    [:material-linkedin:]({linkedin_sharer}?url={page_url}){{ :target="_blank" title="Share on LinkedIn" }}
    [:simple-line:]({line_sharer}{urllib.parse.quote(page_url)}){{ :target="_blank" title="Share on LINE" }}
    [:simple-whatsapp:]({wa_sharer}{urllib.parse.quote(f"{page.title}\n{page_url}")}){{ :target="_blank" title="Share on WhatsApp" }}
    [:simple-telegram:]({tg_sharer}{urllib.parse.quote(page_url)}&text={urllib.parse.quote(page.title)}){{ :target="_blank" title="Share on Telegram" }}
    [:simple-wechat:]({wechat_url}){{ :target="_blank" title="Copy post URL for WeChat" }}
    [:simple-notion:]({notion_url}){{ :target="_blank" title="Copy post URL for Notion" }}
    [:material-microsoft-onenote:]({onenote_url}){{ :target="_blank" title="Copy post URL for OneNote" }}
    [:simple-xiaohongshu:]({xiaohongshu_url}){{ :target="_blank" title="Copy post URL for Xiaohongshu" }}

    :octicons-share-android-16: **Share on others**
    [Copy Link :material-share-all:](javascript:void(0); "Copy post URL")
    [Add to Bookmark :material-bookmark:](javascript:void(0); "Add to Bookmark")
    </div>
    """)