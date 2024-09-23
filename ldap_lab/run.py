from ldap3 import Server, Connection, ALL

server = Server('ldap://127.0.0.1', port=389, get_info=ALL)
conn = Connection(server, user='cn=Manager,dc=example,dc=com', password='secret')

if conn.bind():
    print("成功连接到 LDAP 服务器")
else:
    print("连接失败")

conn.unbind()