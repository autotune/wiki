#### GENERATE CSR WITH OPENSSL

### GENERATE PRIVATE KEY 

    openssl genrsa -out ~/mydomain.org.key 2048

### GENERATE CSR 

    openssl req -new -sha256 -key ~/domain.com.ssl/domain.com.key -out ~/domain.com.ssl/domain.com.csr
