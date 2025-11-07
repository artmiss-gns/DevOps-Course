# BIND DNS Server Configuration

Simple BIND9 DNS server setup for the `artmissco.com` domain.

## Files

- `named.conf.local` - Zone declaration
- `db.artmissco.com` - DNS zone file with records

## Quick Setup

### 1. Install BIND

**Ubuntu/Debian:**
```
sudo apt update
sudo apt install bind9 bind9utils bind9-doc
```

**CentOS/RHEL:**
```
sudo yum install bind bind-utils
```

### 2. Deploy Configuration

Copy the files to your BIND directory:
```
sudo cp named.conf.local /etc/bind/
sudo cp db.artmissco.com /etc/bind/
```
### 3. Verify Configuration

Check zone file syntax:
```
sudo named-checkzone artmissco.com /etc/bind/db.artmissco.com
sudo named-checkconf
```
### 4. Restart BIND

```
sudo systemctl restart bind9
sudo systemctl status bind9
```

## Testing

Test DNS resolution:
```
dig @localhost artmissco.com
dig @localhost www.artmissco.com
nslookup www.artmissco.com localhost
```

## Zone Configuration

**Domain:** artmissco.com  
**Nameserver:** ns1.artmissco.com (192.168.171.132)  
**Web servers:** 192.168.171.200, 192.168.171.201  

## DNS Records

- `@` → 192.168.171.200, 192.168.171.201
- `ns1` → 192.168.171.132
- `www` → 192.168.171.200, 192.168.171.201


## Notes

- Uses private IP addresses (192.168.x.x)
- TTL set to 86400 seconds (24 hours)
- Configured for internal/private network use
