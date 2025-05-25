from textwrap import dedent
import urllib.parse

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
linkedin_sharer = "https://www.linkedin.com/sharing/share-offsite/"  # LinkedIn share URL
wa_sharer = "https://wa.me/?text="  # WhatsApp share URL
tg_sharer = "https://t.me/share/url?url="  # Telegram share URL
notion_url = "https://www.notion.so/"
onenote_url = "https://www.onenote.com/"
wechat_url = "https://web.wechat.com/"
xiaohongshu_url = "https://www.xiaohongshu.com/"

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if page.meta.get('template') != 'blog-post.html': # Only apply the social media tags to blog posts
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')
    wa_text = urllib.parse.quote(f"{page.title}\n{page_url}")
    tg_text = urllib.parse.quote(page.title)
    tg_url = f"{tg_sharer}{urllib.parse.quote(page_url)}&text={tg_text}"

    return markdown + dedent(f"""
    <div style="text-align: center;" markdown="1">


    :octicons-share-android-16: **Share on Socials** 

    [ :simple-x: ]({x_intent}?text={page_title}&url={page_url}){{ :target="_blank" }} 
    [ :material-facebook: ]({fb_sharer}?u={page_url}){{ :target="_blank" }} 
    [ :material-linkedin: ]({linkedin_sharer}?url={page_url}){{ :target="_blank" }}

    :octicons-share-android-16: **Share on others**

    [ :simple-whatsapp: ]({wa_sharer}{wa_text}){{ :target="_blank" }}
    [ :simple-telegram: ]({tg_url}){{ :target="_blank" }}
    [ :simple-wechat: ]({wechat_url}){{ :target="_blank" title="Copy post URL for WeChat" }}
    [ :simple-notion: ]({notion_url}){{ :target="_blank" title="Copy post URL for Notion" }}
    [ :material-microsoft-onenote: ]({onenote_url}){{ :target="_blank" title="Copy post URL for OneNote" }}
    [ :simple-xiaohongshu: ]({xiaohongshu_url}){{ :target="_blank" title="Copy post URL for Xiaohongshu" }}
    
    [Copy Link :material-share-all:](javascript:void(0); "Copy post URL")
    [Add to Bookmark :material-bookmark:](javascript:void(0); "Add to Bookmark")

    <script>
      document.addEventListener('DOMContentLoaded', function() {{
        var links = document.querySelectorAll('a[title="Copy post URL"], a[title="Add to Bookmark"], a[title="Copy post URL for Notion"], a[title="Copy post URL for OneNote"], a[title="Copy post URL for WeChat"], a[title="Copy post URL for Xiaohongshu"]');
        links.forEach(function(link) {{
          link.addEventListener('click', function(e) {{
            if (link.title === "Add to Bookmark") {{
              e.preventDefault();
              var title = document.title;
              var url = window.location.href;
              try {{
                if (window.sidebar && window.sidebar.addPanel) {{
                  // Firefox <=22
                  window.sidebar.addPanel(title, url, "");
                }} else if (window.external && ('AddFavorite' in window.external)) {{
                  // IE Favorites
                  window.external.AddFavorite(url, title);
                }} else {{
                  // Modern browsers
                  alert('Press Ctrl+D (Windows) or Cmd+D (Mac) to bookmark this page.');
                }}
              }} catch (err) {{
                alert('Press Ctrl+D (Windows) or Cmd+D (Mac) to bookmark this page.');
              }}
            }} else if (link.title === "Copy post URL for Notion") {{
              navigator.clipboard.writeText(window.location.href);
              alert('Link copied! Notion will open in a new tab. Paste the link into your Notion page.');
            }} else if (link.title === "Copy post URL for OneNote") {{
              navigator.clipboard.writeText(window.location.href);
              alert('Link copied! OneNote will open in a new tab. Paste the link into your OneNote page.');
            }} else if (link.title === "Copy post URL for WeChat") {{
              navigator.clipboard.writeText(window.location.href);
              alert('Link copied! WeChat Web will open in a new tab. Paste the link to share.');
            }} else if (link.title === "Copy post URL for Xiaohongshu") {{
              navigator.clipboard.writeText(window.location.href);
              alert('Link copied! Xiaohongshu will open in a new tab. Paste the link to share.');
            }} else {{
              e.preventDefault();
              navigator.clipboard.writeText(window.location.href);
              alert('Link copied! Open your app and paste to share.');
            }}
          }});
        }});
      }});
    </script>
    </div>
    """)