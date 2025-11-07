$TTL    86400
@       IN      SOA     ns1.artmissco.com. admin.artmissco.com. (
                        2023060301 ; Serial (YYYYMMDDNN)
                        3600       ; Refresh
                        900        ; Retry
                        604800     ; Expire
                        86400 )    ; Minimum TTL
@       IN      NS      ns1.artmissco.com.
@       IN      A       192.168.171.200
@       IN      A       192.168.171.201
ns1     IN      A       192.168.171.132
www     IN      A       192.168.171.200
www     IN      A       192.168.171.201
