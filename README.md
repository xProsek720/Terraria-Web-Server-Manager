# Terraria Web Server Manager
Web app that does Start and Stop for Ubuntu Terraria Server


1. Install all requirements:

```sudo apt get update & sudo apt get upgrade```

```sudo apt get install python3 python3-pip supervisor```

2. Make user account for terraria server:

```sudo adduser terraria-server```

3. Make terraria-server user sudoer without password:

```sudo usermod -aG sudo terraria-server```

4. Copy all of the files from GitHub Project!

```sudo chmod +x /usr/local/bin/terrariad```

```sudo chmod +x /home/terraria-server/server/TerrariaServer.bin.x86_64```

5. Open ports:

```sudo ufw allow 7777/tcp```

```sudo ufw allow 80```

6. To apply and run web app do cmd below:

```sudo service supervisor reload```
