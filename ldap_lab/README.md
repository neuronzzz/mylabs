# slapd所在目录
/opt/homebrew/Cellar/openldap/2.6.8/libexec/slapd

# lab的slapd命令。lab目前是失败了
sudo /opt/homebrew/Cellar/openldap/2.6.8/libexec/slapd -f /Users/ryanzhang/github/mylabs/slapd.conf -h "ldap://127.0.0.1/" 