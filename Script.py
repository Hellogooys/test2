class script(object):
    START_TXT = """<b>π·π΄π»π»πΎ πΌπ π΅ππΈπ΄π½π³ {}
πΌπ π½π°πΌπ΄ γ<a href=https://t.me/CL_FILTER_BOT>ππ·πΎπΌπ°π ππ·π΄π»π±π</a>γ ,πΈπ²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π , πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ ππ΄π΄ πΌπ πΏπΎππ΄π π</b>"""
      
    OWNER_TXT = """<b>π° π·π΄π π·π΄ππ΄ ππΎπ π²π°π½ π²πΎπ½ππ°π²π πΌπ πΎππ½π΄π π°</b>"""
    
    HELP_TXT = """π·π΄π {}
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π."""
    
    ABOUT_TXT = """<b>β¬ πΌπ π½π°πΌπ΄: {}
β¬ π²ππ΄π°ππΎπ: <a href=https://t.me/NL_MP4>π½πΈπ·π°π°π»</a>
β¬ π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
β¬ π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
β¬ π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π±
β¬ π±πΎπ ππ΄πππ΄π: π·π΄ππΎπΊπ
β¬ π±ππΈπ»π³ πππ°πππ: v1.0.2 [ π±π΄ππ° ]</b>"""
    
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and ππ·πΎπΌπ°π ππ·π΄π»π±π will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ππ·πΎπΌπ°π ππ·π΄π»π±π should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ππ·πΎπΌπ°π ππ·π΄π»π±π supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
π»π―π¬πΊπ¬ π¨πΉπ¬ π»π―π¬ π¬πΏπ»πΉπ¨ π­π¬π¨πΌπ»πΌπΉπ¬ πΆπ­ π»π―πΆπ΄π¨πΊ πΊπ―π¬π³π©π 

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDb source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    
    ADMIN_TXT = """Help: <b>α΄α΄α΄ΙͺΙ΄ α΄α΄α΄α΄α΄Ι΄α΄s</b>

<b>NOTE:</b>

βοΈ α΄ΚΙͺs α΄α΄α΄α΄α΄Ι΄α΄s α΄Ι΄ΚΚ α΄‘α΄Κα΄ ?α΄Κ α΄α΄α΄ΙͺΙ΄ βοΈ

βοΈ α΄α΄α΄α΄ ?ΙͺΚα΄α΄Κ

Β» /delete - Reply Files

Β» /deleteall - Delete All Files

Β» /total - How Many Files Saved

Β» /channel - Add Channel List

βοΈ α΄α΄Ι΄α΄α΄Κ ?ΙͺΚα΄α΄Κ

Β» /add - add a new filter

Β» /filters - see your filters

Β» /connect - connect a chat

Β» /delfilter - delete a filter

Β» /delall_filters - delete all filters from chat

Β» /disconnect - disconnect a chat 

Β» /connections - see current connections
"""
    ADMIN_TXT2 = """βοΈ α΄α΄α΄α΄α΄Ι΄ α΄α΄α΄α΄α΄Ι΄α΄s

Β» /broadcast - Reply Any Media Or Message

Β» /logger - Get Bot Logs 

Β» /start - check alive

Β» /help - see helps 

Β» /about- see about

βοΈ Ι’Κα΄α΄α΄ α΄α΄α΄α΄α΄Ι΄α΄s

Β» /ban-ban user from group

Β» /tban - time set ban

Β» /unban - unban user from group

Β» /mute - Mute user from group

Β» /tmute - time set mute

Β» /unmute - unmute user from group

Β» /pin - pin message in group 

Β» /unpin - unpin message in group

Β» /purge - delete all messages in group"""
    
    STATUS_TXT = """<b>β¬ ππΎππ°π» π΅πΈπ»π΄π: <code>{}</code>
β¬ ππΎππ°π» πππ΄ππ: <code>{}</code>
β¬ ππΎππ°π» π²π·π°ππ: <code>{}</code>
β¬ πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
β¬ π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±</b>"""
    LOG_TEXT_G = """#πππ°ππ«π¨π?π©
    
<b>αβΊ ππ«π¨π?π© βͺΌ  {}(<code>{}</code>)</b>
<b>αβΊ ππ¨π­ππ₯ πππ¦πππ«π¬ βͺΌ <code>{}</code></b>
<b>αβΊ πππππ ππ² βͺΌ  {}</b>
"""
    LOG_TEXT_P = """#πππ°ππ¬ππ«
    
<b>αβΊ ππ - <code>{}</code></b>
<b>αβΊ πππ¦π - {}</b>
"""
