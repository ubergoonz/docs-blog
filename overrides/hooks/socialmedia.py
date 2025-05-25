import urllib.parse

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
linkedin_sharer = "https://www.linkedin.com/sharing/share-offsite/"

x_owner = "@ubergoonz"
fb_owner = "@ubergoonz"
li_owner = "@lesliewang"

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if page.meta.get('template') != 'blog-post.html':
        return markdown

    page_url = config.site_url + page.url
    page_title = page.title

    x_message = f"Check out this awesome blog post by {x_owner}: {page_title} {page_url}"
    fb_message = f"Check out this awesome blog post by {fb_owner}: {page_title} {page_url}"
    li_message = f"Check out this awesome blog post by {li_owner}: {page_title} {page_url}"

    encoded_x_message = urllib.parse.quote(x_message)
    encoded_fb_message = urllib.parse.quote(fb_message)
    encoded_li_message = urllib.parse.quote(li_message)
    encoded_url = urllib.parse.quote(page_url)

    share_md = f"""
---
**Share this post**

<a href="{x_intent}?text={encoded_x_message}" target="_blank" class="x-share" data-message="{x_message}">
:simple-x:
</a>
<a href="{fb_sharer}?u={encoded_url}" target="_blank" class="fb-share" data-message="{fb_message}">
:simple-facebook:
</a>
<a href="{linkedin_sharer}?url={encoded_url}&summary={encoded_li_message}" target="_blank" class="li-share" data-message="{li_message}">
:material-linkedin:
</a>

<script>
document.addEventListener('DOMContentLoaded', function() {{
  var shares = document.querySelectorAll('a.fb-share, a.li-share');
  shares.forEach(function(link) {{
    link.addEventListener('click', function(e) {{
      navigator.clipboard.writeText(link.getAttribute('data-message'));
      setTimeout(function() {{
        alert('Message copied! Paste it in the share dialog.');
      }}, 100);
    }});
  }});
}});
</script>
---
"""
    return markdown + share_md