import urllib.parse

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
linkedin_sharer = "https://www.linkedin.com/sharing/share-offsite/"
wa_sharer = "https://wa.me/?text="
tg_sharer = "https://t.me/share/url"

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
    wa_message = f"Check out this awesome blog post: {page_title} {page_url}"
    tg_message = f"Check out this awesome blog post: {page_title} {page_url}"
    email_subject = f"Check out this blog post: {page_title}"
    email_body = f"Hi,\n\nI found this awesome blog post and thought you might like it:\n\n{page_title}\n{page_url}\n\nBest regards!"
    email_link = f"mailto:?subject={urllib.parse.quote(email_subject)}&body={urllib.parse.quote(email_body)}"

    encoded_x_message = urllib.parse.quote(x_message)
    encoded_fb_message = urllib.parse.quote(fb_message)
    encoded_li_message = urllib.parse.quote(li_message)
    encoded_wa_message = urllib.parse.quote(wa_message)
    encoded_tg_message = urllib.parse.quote(tg_message)
    encoded_url = urllib.parse.quote(page_url)

    share_md = f"""
---
<div style="text-align: center;" markdown="1">

:octicons-share-android-16: **Share on Social**

<a href="{x_intent}?text={encoded_x_message}" target="_blank" class="x-share" data-message="{x_message}" title="Share on X">
:simple-x:
</a>
<a href="{fb_sharer}?u={encoded_url}" target="_blank" class="fb-share" data-message="{fb_message}" title="Share on Facebook">
:simple-facebook:
</a>
<a href="{linkedin_sharer}?url={encoded_url}&summary={encoded_li_message}" target="_blank" class="li-share" data-message="{li_message}" title="Share on LinkedIn">
:material-linkedin:
</a>
<a href="{wa_sharer}{encoded_wa_message}" target="_blank" class="wa-share" data-message="{wa_message}" title="Share on WhatsApp">
:simple-whatsapp:
</a>
<a href="{tg_sharer}?url={encoded_url}&text={encoded_tg_message}" target="_blank" class="tg-share" data-message="{tg_message}" title="Share on Telegram">
:simple-telegram:
</a>
<a href="{email_link}" target="_blank" class="email-share" title="Share via Email">
:material-email:
</a>

:octicons-copy-16: **Copy/paste and Share**

<a href="javascript:void(0);" class="cp-share" data-message="Check out this awesome blog post: {page_title} {page_url}" title="Copy page URL to clipboard">
:simple-xiaohongshu: :simple-notion: :material-microsoft-teams: :simple-zoom: :simple-slack: :simple-discord: :simple-reddit: :simple-stackoverflow:
</a>
<script>
document.addEventListener('DOMContentLoaded', function() {{
  var shares = document.querySelectorAll('a');
  shares.forEach(function(link) {{
    link.addEventListener('click', function(e) {{
      if (link.classList.contains('cp-share')) {{
        // Copy only the page URL for the "Copy/paste and Share" button
        var message = link.getAttribute('data-message');
        var url = message.split(' ').pop(); // Extract the last part (URL)
        navigator.clipboard.writeText(url);
        alert('Page URL copied to clipboard! Paste it into your favorite app.');
      }} else if (link.classList.contains('fb-share') || link.classList.contains('li-share')) {{
        // Copy the full message for Facebook and LinkedIn
        var message = link.getAttribute('data-message');
        navigator.clipboard.writeText(message);
        alert('Message copied to clipboard! Paste it in the Social Platform dialog.');
      }}
    }});
  }});
}});
</script>
</div>
---
"""
    return markdown + share_md