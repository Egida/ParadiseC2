# ParadiseC2
A python botnet forked from <a href="https://github.com/wodxgod/PYbot">PYBot</a> which was discontinued, a completely remade version.

# Requirements
  <li>A VPS Server</li>
  <li>Any Linux Distro (I recommend Debian)</li>

# Installation
  <p>Install the required packages</p>
  <pre><code>sudo apt install bash wget && wget https://raw.githubusercontent.com/d3fe4ted/ParadiseC2/main/installation.sh && sudo bash installation.sh</code></pre>

# How to Setup
  <div><p>(Inside ParadiseC2 folder) Enter this command</p>
  <pre><code>screen python3 cnc.py (PORT)</pre></code>
  
  <div><p>Make sure you change the username and password in the <code>logins.txt</code> file.</p>
  <pre><code>root@d3fe4ted:~$ nano logins.txt
---- GNU nano 5.4 -----------------------------------------------------------
 root:root
 &nbsp;
 &nbsp;
 &nbsp;
 &nbsp;
 &nbsp;
 &nbsp;
 &nbsp;
 &nbsp;
 &nbsp;
 &nbsp;
 ^G Help          ^O Write Out     ^W Where Is      ^K Cut           ^T Execute       ^C Location      M-U Undo
 ^X Exit          ^R Read File     ^\ Replace       ^U Paste         ^J Justify       ^_ Go To Line    M-E Redo
  Once you changed these details press "CTRL + X" and then "Y" then "ENTER" on your keyboard</code></pre>
  
  <div><li>Use telnet with the IP of your server and port in another terminal or PuTTY</li>
  
# How to stop screen
  <p>How to kill screen process</p>
  <pre><code>screen -X -S 1 kill</code></pre>

# How to Setup Bots 
  <li>Change IP in bot.py to your server ip</li>
  <li>Go onto another machine (With permission)</li>
  <li>Copy and run bot.py; <code>screen python3 bot.py</code></li>

# Recommended Hosting
  <li><a href="https://www.cloudways.com/en/">Cloudways</a>
  <li><a href="https://crazyrdp.com/linux-vps-hosting/">CrazyRDP</a></li>
    <div></lu>
